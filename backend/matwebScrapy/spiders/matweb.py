from Framework.BancoDeDados import BancoDeDados
import scrapy

class matweb(scrapy.Spider):
	name = "matweb"
	
	def start_requests(self):
		urls = 'https://matriculaweb.unb.br/graduacao/oferta_campus.aspx'
		yield scrapy.Request(url=urls, callback=self.parse)
		
	def parse(self,response):
		linhas = response.xpath('//table[@class="FrameCinza"]/tr[@class="PadraoMenor"]')
		for linha in linhas:
			indice = linha.xpath('td/text()').extract()
			dado = linha.xpath('td/a/text()').extract()
			self.checacampus(indice[0],dado[0])
			novaurl = 'https://matriculaweb.unb.br/graduacao/' + linha.xpath('td/a/@href').extract()[0]
			yield scrapy.Request(url=novaurl, callback=lambda r, indice=indice:self.parse2(r,indice))
			
	def salvacampus(self,indice,dado):
		BancoDeDados().executar('insert into campus (id,nome) values (%s,%s)',(indice,dado))
		
	def checacampus(self,indice,dado):
		existe = BancoDeDados().consultarUnico('select * from campus where id = %s', (indice,))
		if existe is None:
			self.salvacampus(indice,dado)
			
	def parse2(self,response,idcampus):
		linhas = response.xpath('//table[@class="FrameCinza"]/tr[@class="PadraoMenor"]')
		for linha in linhas:
			codigo = linha.xpath('td[1]/text()').extract()
			sigla = linha.xpath('td[2]/text()').extract()
			dado = linha.xpath('td/a/text()').extract()
			novaurl = 'https://matriculaweb.unb.br/graduacao/' + linha.xpath('td/a/@href').extract()[0]
			iddepart = self.checadepart(codigo[0],sigla[0],dado[0],idcampus[0])
			if iddepart != 0:
				yield scrapy.Request(url=novaurl, callback=lambda r, iddepart=iddepart:self.parse3(r, iddepart))
	
	def salvadepart(self,codigo,sigla,dado,idcampus):
		print(codigo,sigla,dado,idcampus)
		BancoDeDados().executar('insert into departamento (codigo,sigla,nome,id_campus) values (%s,%s,%s,%s)',(codigo,sigla,dado,idcampus))
		iddepart = BancoDeDados().consultarUnico('select id from departamento where nome = %s and id_campus = %s',(dado,idcampus))[0]
		return iddepart
		
	def checadepart(self,codigo,sigla,dado,idcampus):
		existe = BancoDeDados().consultarUnico('select id from departamento where nome = %s and id_campus = %s',(dado,idcampus))
		if existe is None:
			if idcampus == 2 and codigo != 638:
				return 0
			else:
				return self.salvadepart(codigo,sigla,dado,idcampus)
		else:
			return existe[0]
			
	def parse3(self,response,iddepart):
		linhas = response.xpath('//table[@class="FrameCinza"]/tr[@class="PadraoMenor"]')
		for linha in linhas:
			codigo = linha.xpath('td[@class="Padrao"]/b/text()').extract()
			dado = linha.xpath('td[2]/a/text()').extract()
			novaurl = 'https://matriculaweb.unb.br/graduacao/' + linha.xpath('td[2]/a/@href').extract()[0]
			ementaurl = 'https://matriculaweb.unb.br' + linha.xpath('td[3]/a/@href').extract()[0]
			iddisciplina = self.checadisciplina(codigo[0],dado[0],iddepart)
			yield scrapy.Request(url=ementaurl, callback=lambda r, iddisciplina=iddisciplina:self.parse5(r, iddisciplina))
			yield scrapy.Request(url=novaurl, callback=lambda r, iddisciplina=iddisciplina:self.parse4(r,iddisciplina))
	
	def parse5(self,response,iddisciplina):
		ementa = response.xpath('//table[@class="FrameCinza"][@width="90%"]').extract()[0]
		ementafilename = "../frontend/Arquivos/ementa-" + str(iddisciplina[0]) + ".html"
		ementafile = open(ementafilename,"w")
		ementafile.write(ementa.encode('utf-8'))
		ementafile.close()
		
	
	def checadisciplina(self,codigo,dado,iddepart):
		iddisciplina = BancoDeDados().consultarUnico('select id from disciplina where nome = %s and id_departamento = %s',(dado,iddepart))
		if iddisciplina is None:
			return self.salvadisciplina(codigo,dado,iddepart)
		else:
			return iddisciplina
	
	def salvadisciplina(self,codigo,dado,iddepart):
		print(codigo,dado,iddepart)
		BancoDeDados().executar('insert into disciplina (nome,codigo,id_departamento) values(%s,%s,%s)',(dado,codigo,iddepart))
		return BancoDeDados().consultarUnico('select * from disciplina where nome = %s and id_departamento = %s',(dado,iddepart))
		
	def parse4(self,response,iddisciplina):
		creditos = response.xpath('//table[@class="framecinza"][@width="70%"]//td[@width="30%"]//font/text()').extract()
		tabelas = response.xpath('//table[@class="framecinza"][@width="90%"]/tr[@bgcolor="#FFFFFF"]')
		self.trata_oferta(creditos,tabelas,iddisciplina[0])
		
	def trata_oferta(self,creditos,tabelas,id_disciplina):
		id_oferta = self.checa_oferta(creditos,tabelas,id_disciplina)
		self.trata_turma(tabelas,id_oferta,id_disciplina)
		
	def checa_oferta(self,creditos,tabelas,id_disciplina):
		id_oferta = BancoDeDados().consultarUnico('select id from oferta where id_disciplina = %s',(id_disciplina,))
		if id_oferta is None:
			id_oferta = self.grava_oferta(id_disciplina,creditos)
		return id_oferta[0]
		
	def grava_oferta(self,id_disciplina,creditos):
		id_ementa = self.checa_ementa(id_disciplina)
		BancoDeDados().executar('insert into oferta (id_disciplina,creditos,id_ementa) values (%s,%s,%s)',(id_disciplina,creditos[0],id_ementa))
		return BancoDeDados().consultarUnico('select id from oferta where id_disciplina = %s',(id_disciplina,))
	
	def checa_ementa(self,id_disciplina):
		arquivo = "Arquivos/ementa-" + str(id_disciplina) + ".html"
		id_ementa = BancoDeDados().consultarUnico('select id from ementa where arquivo = %s',(arquivo,))
		if id_ementa is None:
			id_ementa = self.grava_ementa(arquivo)
		return id_ementa[0]
		
	def grava_ementa(self,arquivo):
		BancoDeDados().executar('insert into ementa (arquivo) values (%s)',(arquivo,))
		return BancoDeDados().consultarUnico('select id from ementa where arquivo = %s',(arquivo,))
		
	def trata_turma(self,tabelas,id_oferta,id_disciplina):
		for tabela in tabelas:
			try:
				letra = tabela.xpath('td[@width="40"]/div[@class="titulo"]/font/b/text()').extract()[0]
				id_professor = self.checa_professor(tabela)
				vagas = tabela.xpath('td[@bgcolor="whitesmoke"]//tr[@class="padraomenor"]/td/b//text()').extract()
				turno = tabela.xpath('td[@width="40"][@nowrap]/div//text()').extract()
				id_turma = self.checa_turma(letra,id_professor,vagas,turno,id_disciplina,tabela)
				self.associa_oferta_turma(id_oferta,id_turma)
			except:
				print("vazio")
	
	def checa_turma(self,letra,id_professor,vagas,turno,id_disciplina,tabela):
		id_turma = BancoDeDados().consultarUnico('select id from turma where id_disciplina = %s and id_professor = %s and letra = %s',(id_disciplina,id_professor,letra))
		if id_turma is None:
			id_turma = self.grava_turma(letra,turno,id_disciplina,id_professor,vagas)
		dias = tabela.xpath('td[@class="padrao"]/div')
		for dia in dias:
			id_sala = self.checa_sala(dia)
			id_horario = self.checa_horario(dia)
			self.associa_turma_sala_horario(id_sala,id_horario,id_turma[0])			
		return id_turma[0]		
		
	def grava_turma(self,letra,turno,id_disciplina,id_professor,vagas):
		BancoDeDados().executar('insert into turma (id_disciplina,vagas,ocupadas,restantes,letra,id_professor,turno) values(%s,%s,%s,%s,%s,%s,%s)',(id_disciplina,vagas[0],vagas[1],vagas[2],letra,id_professor,turno[0]))
		return BancoDeDados().consultarUnico('select id from turma where id_disciplina = %s and id_professor = %s and letra = %s',(id_disciplina,id_professor,letra)) 
		
	def checa_sala(self,dia):
		sala = dia.xpath('i/text()').extract()[0]
		id_sala = BancoDeDados().consultarUnico('select id from sala where codigo = %s',(sala,))
		if id_sala is None:
			id_sala = self.grava_sala(sala)
		return id_sala[0]
	
	def grava_sala(self,sala):
		BancoDeDados().executar('insert into sala (codigo) values (%s)',(sala,))
		return BancoDeDados().consultarUnico('select id from sala where codigo = %s',(sala,))
		
	def checa_horario(self,dia):
		dia_semana = dia.xpath('b/text()').extract()[0]
		inicio = dia.xpath('font[@color="black"]/b/text()').extract()[0]
		fim = dia.xpath('font[@color="brown"]/text()').extract()[0]
		print(dia_semana,inicio,fim)
		id_horario = BancoDeDados().consultarUnico('select id from horario where inicio = %s and fim = %s and dia = %s',(inicio,fim,dia_semana))
		if id_horario is None:
			id_horario = self.grava_horario(dia_semana,inicio,fim)
		return id_horario[0]
	
	def grava_horario(self,dia,inicio,fim):
		BancoDeDados().executar('insert into horario (dia,inicio,fim) values (%s,%s,%s)',(dia,inicio,fim))
		return BancoDeDados().consultarUnico('select id from horario where dia = %s and inicio = %s and fim = %s',(dia,inicio,fim))
			
	def checa_professor(self,tabela):
		professor = tabela.xpath('td[@class="padraomenor"]/center/text()').extract()[0]
		id_professor = BancoDeDados().consultarUnico('select id from professor where nome = %s',(professor,))
		if id_professor is None:
			id_professor = self.grava_professor(professor)
		return id_professor[0]
	
	def grava_professor(self,professor):
		BancoDeDados().executar('insert into professor (nome) values (%s)',(professor,))
		return BancoDeDados().consultarUnico('select id from professor where nome = %s',(professor,))

	def associa_oferta_turma(self,id_oferta,id_turma):
		id_associacao = BancoDeDados().consultarUnico('select id from ass_oferta_turma where id_oferta=%s and id_turma=%s',(id_oferta,id_turma))
		if id_associacao is None:
			BancoDeDados().executar('insert into ass_oferta_turma (id_oferta,id_turma) values (%s,%s)',(id_oferta,id_turma))
		print("===================================== cheguei aqui ==========================================")
	
	def associa_turma_sala_horario(self,id_sala,id_horario,id_turma):
		id_associacao = BancoDeDados().consultarUnico('select id from ass_turma_sala_horario where id_turma=%s and id_sala=%s and id_horario=%s',(id_turma,id_sala,id_horario))
		if id_associacao is None:
			BancoDeDados().executar('insert into ass_turma_sala_horario (id_sala,id_horario,id_turma) values (%s,%s,%s)',(id_sala,id_horario,id_turma))	
		print("===================================== cheguei aqui ==========================================")	



















		
			