# -*- coding: utf-8 -*-
from Framework.BancoDeDados import BancoDeDados
import scrapy
import re

class matweb(scrapy.Spider):
	name = "curso"
	
	def start_requests(self):
		urls = 'https://matriculaweb.unb.br/graduacao/curso_campus.aspx'
		yield scrapy.Request(url=urls, callback=self.parse)
		
	def parse(self,response):
		linhas = response.xpath('//table[@class="FrameCinza"]/tr[@class="PadraoMenor"]')
		for linha in linhas:
			indice = linha.xpath('td/text()').extract()[0]
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
			modalidade = linha.xpath('td[1]/text()').extract()[0]
			codigo = linha.xpath('td[2]/text()').extract()[0]
			curso = linha.xpath('td[3]/a/text()').extract()[0]
			turno = linha.xpath('td[4]/text()').extract()[0]
			print(modalidade,codigo,curso,turno)
			novaurl1 = 'https://matriculaweb.unb.br/graduacao/' + linha.xpath('td[3]/a/@href').extract()[0]
			idcurso = self.checarcurso(idcampus,codigo,curso,turno)
			if idcurso != 0:
				yield scrapy.Request(url=novaurl1, callback=lambda r, idcurso=idcurso:self.parse3(r, idcurso))


	def checarcurso(self,idcampus,codigo,curso,turno):
		idcurso = BancoDeDados().consultarUnico('select id from curso where nome = %s and id_campus = %s',(curso,idcampus))
		if idcurso is None:
			idcurso = self.gravacurso(idcampus,codigo,curso,turno)
		return idcurso
		
	def gravacurso(self,idcampus,codigo,curso,turno):
		BancoDeDados().executar('insert into curso (id_campus,codigo,nome,turno) values (%s,%s,%s,%s)',(idcampus,codigo,curso,turno))
		return BancoDeDados().consultarUnico('select id from curso where nome = %s',(curso,))
		
	def parse3(self,response,id_curso):
		id_grau = []
		tabela = response.xpath('//table[@class="FrameCinza"][@width="90%"]')
		try:
			fluxoUrl = tabela.xpath('tr[@class="PadraoMenor"]/td[@colspan="2"]/a[1]/@href').extract()[0]
			curriculoUrl = tabela.xpath('tr[@class="PadraoMenor"]/td[@colspan="2"]/a[2]/@href').extract()[0]
			permanencia_minima = tabela.xpath('//tr[@class="Padrao"][2]/td[@align="right"]/text()').extract()[0]
			permanencia_maxima = tabela.xpath('//tr[@class="Padrao"][3]/td[@align="right"]/text()').extract()[0]
			creditos_formatura = tabela.xpath('//tr[@class="Padrao"][4]/td[@align="right"]/text()').extract()[0]
			creditos_optativos_concentracao = tabela.xpath('//tr[@class="Padrao"][5]/td[@align="right"]/text()').extract()[0]
			creditos_optativos_conexa = tabela.xpath('//tr[@class="Padrao"][6]/td[@align="right"]/text()').extract()[0]
			creditos_livres_maximo = tabela.xpath('//tr[@class="Padrao"][7]/td[@align="right"]/text()').extract()[0]
			grau = tabela.xpath('//tr[@class="Padrao"][1]/td[2]/text()').extract()
			fluxourl = 'https://matriculaweb.unb.br/graduacao/' + fluxoUrl
			curriculourl = 'https://matriculaweb.unb.br/graduacao/' + curriculoUrl
			print(fluxourl)
			yield scrapy.Request(url=fluxourl, callback=lambda r, id_curso=id_curso:self.parse4(r, id_curso))
 			yield scrapy.Request(url=curriculourl, callback=lambda r, id_curso=id_curso:self.parse5(r, id_curso))
			try: 
				nomegrau = grau[0]
				id_grau = self.checagrau(nomegrau)
			except:
				print("================================================ ",grau)
			self.complementacurso(id_curso[0],id_grau,permanencia_minima,permanencia_maxima,creditos_formatura,creditos_optativos_concentracao,creditos_optativos_conexa,creditos_livres_maximo)
 		except:
 			print("faltou alguma coisa")
 			
 			
		
	def complementacurso(self,id_curso,id_grau,permanencia_minima,permanencia_maxima,creditos_formatura,creditos_optativos_concentracao,creditos_optativos_conexa,creditos_livres_maximo):
		if id_grau is None:
			BancoDeDados().executar('update curso set id_grau=%s,permanencia_minima=%s,permanencia_maxima=%s,creditos_formatura=%s,creditos_optativos_concentracao=%s,creditos_optativos_conexa=%s,creditos_livres_maximo=%s where id=%s',(id_grau,permanencia_minima,permanencia_maxima,creditos_formatura,creditos_optativos_concentracao,creditos_optativos_conexa,creditos_livres_maximo,id_curso))
		else:
			BancoDeDados().executar('update curso set permanencia_minima=%s,permanencia_maxima=%s,creditos_formatura=%s,creditos_optativos_concentracao=%s,creditos_optativos_conexa=%s,creditos_livres_maximo=%s where id=%s',(permanencia_minima,permanencia_maxima,creditos_formatura,creditos_optativos_concentracao,creditos_optativos_conexa,creditos_livres_maximo,id_curso))
		
	def checagrau(self,grau):
		id_grau = BancoDeDados().consultarUnico('select id from grau where nome = %s',(grau,))
		if id_grau is None:
			id_grau = self.gravagrau(grau)
		try:
			idgrau = id_grau[0]
		except:
			idgrau = None
		return idgrau
	
	def gravagrau(self,grau):
		BancoDeDados().executar('insert into grau (nome) values (%s)',(grau,))
		return BancoDeDados().consultarUnico('select id from grau where nome = %s',(grau,))


	def parse4(self,response,idcurso):
		print("===== Fluxo ======")
		tabelas = response.xpath('//table[@class="FrameCinza"][@width="95%"]')
		for tabela in tabelas:
			linhaperiodo = tabela.xpath('tr[@class="padraobranco"]/td/b')
			linhasmaterias = tabela.xpath('tr[@class="padraomenor"]')
			self.trataperiodo(linhaperiodo,idcurso[0],linhasmaterias)
			
	def trataperiodo(self,linha,idcurso,linhasmaterias):
		for coluna in linha:
			dado = coluna.xpath('text()').extract()
			for i in dado:
				if u"PERÍODO" in i:
					periodo = re.findall('\d+', i)
				else:
					creditos = re.findall('\d+', i)
			id_periodo = self.checaperiodo(periodo[0],creditos[0],idcurso)
			self.tratamaterias(linhasmaterias,id_periodo)
					
					
	def checaperiodo(self,periodo,creditos,idcurso):
		id_periodo = BancoDeDados().consultarUnico('select id from periodo where id_curso = %s and periodo = %s',(idcurso,periodo))
		if id_periodo is None:
			id_periodo = self.grava_periodo(periodo,creditos,idcurso)
		return id_periodo[0]
		
	def grava_periodo(self,periodo,creditos,idcurso):
		BancoDeDados().executar('insert into periodo (periodo,creditos,id_curso) values (%s,%s,%s)',(periodo,creditos,idcurso))
		return BancoDeDados().consultarUnico('select id from periodo where id_curso = %s and periodo = %s and creditos = %s',(idcurso,periodo,creditos))
					
	def tratamaterias(self,linhas,id_periodo):
		for coluna in linhas:
			codigo = coluna.xpath('td[3]/a/text()').extract()
			nome = coluna.xpath('td[4]/a/text()').extract()
			creditos = coluna.xpath('td[5]/text()').extract()
			self.checa_materia(codigo[0],nome[0],creditos[0],id_periodo)
	
	def checa_materia(self,codigo,nome,creditos,id_periodo):
		ids_disciplina = BancoDeDados().consultarMultiplos('select id from disciplina where codigo = %s',(codigo,))
		if ids_disciplina is not None:
			for id in ids_disciplina:
				self.atualiza_materia(id[0],creditos)
				self.checa_ass_periodo(id[0],id_periodo)
		else:
			id_disciplina = self.grava_materia(codigo,nome,creditos)
			self.checa_ass_periodo(id_disciplina[0],id_periodo)
	
	def checa_ass_periodo(self,id_disciplina,id_periodo):
		id_associacao = BancoDeDados().consultarUnico('select id from ass_periodo_disciplina where id_disciplina = %s and id_periodo = %s',(id_disciplina,id_periodo) )
		if id_associacao is None:
			BancoDeDados().executar('insert into ass_periodo_disciplina (id_disciplina,id_periodo) values(%s,%s)',(id_disciplina,id_periodo) )	
	
	def atualiza_materia(self,id,creditos):
		new_creditos = creditos.replace(" - ","-")
		#BancoDeDados().executar('update disciplina set creditos = %s where id = %s',(new_creditos,id))
		
	def grava_materia(self,codigo,nome,creditos):
		BancoDeDados().executar('insert into disciplina (nome,codigo,creditos) values (%s,%s,%s)',(nome,codigo,creditos))
		return BancoDeDados().consultarUnico('select id from disciplina where nome = %s and codigo = %s',(nome,codigo))
		
	def parse5(self,response,idcurso):
		print("+++++ Curriculo +++++")
		linhas = response.xpath('//table[@class="Frame"][@width="80%"]/tr')
		for linha in linhas:
			coluna_nomes = linha.xpath('td/b/text()').extract()
			coluna1 = linha.xpath('td[2]')
			coluna2 = linha.xpath('td[3]/text()').extract()
			self.tratalinha(coluna_nomes,coluna1,coluna2,idcurso)
			self.tratamaterias2(linha,idcurso[0])
			
	def tratalinha(self,coluna_nomes,coluna1,coluna2,idcurso):
		if coluna_nomes is not None:
			if u"Créditos por período:" in coluna_nomes:
				minimo = coluna1.xpath('nobr/text()').extract()
				print ('minimo por periodo ', re.findall('\d+', minimo[0]))
				print ('maximo por periodo ', re.findall('\d+', coluna2[0]))
				credito_periodo_minimo = re.findall('\d+', minimo[0])
				credito_periodo_maximo = re.findall('\d+', coluna2[0])
				self.checa_min_max_periodo(credito_periodo_minimo[0],credito_periodo_maximo[0],idcurso[0])
				
	def checa_min_max_periodo(self,minimo,maximo,idcurso):
		id_curso = BancoDeDados().consultarUnico('select id from curso where id = %s and credito_periodo_minimo = %s and credito_periodo_maximo = %s',(idcurso,minimo,maximo) )
		if id_curso is None:
			BancoDeDados().executar('update curso set credito_periodo_minimo = %s , credito_periodo_maximo = %s where id = %s',(minimo,maximo,idcurso))

	
	def tratamaterias2(self,linha,idcurso):
		planilhas = linha.xpath('td[@class="Padrao"]')
		for planilha in planilhas:
			title = planilha.xpath('b/font[@class="padrao"]/text()').extract()
			titlea = title[0].lstrip()
			titulo = titlea.rstrip()
			print(titulo," do curso ",idcurso)
			id_escopo = self.checa_escopo(titulo)
			disciplinas = planilha.xpath('table[@class="FrameCinza"]/tr')
			self.tratadisciplina(disciplinas,id_escopo,idcurso)
			
	def checa_escopo(self,titulo):
		id_escopo = BancoDeDados().consultarUnico('select id from escopo_disciplina where nome = %s',(titulo,))
		if id_escopo is None:
			BancoDeDados().executar('insert into escopo_disciplina (nome) values (%s)',(titulo,))
			id_escopo = BancoDeDados().consultarUnico('select id from escopo_disciplina where nome = %s',(titulo,))
		return id_escopo
			
	
	def tratadisciplina(self,disciplinas,id_escopo,idcurso):
		for disciplina in disciplinas:
			codigo = disciplina.xpath('td/a/b/text()').extract()
			creditos = disciplina.xpath('td[3]/text()').extract()
			id_disciplina = self.pesquisamateria(codigo,creditos)
			self.checacurriculo(idcurso,id_escopo[0],id_disciplina)
			
	def checacurriculo(self,idcurso,id_escopo,id_disciplina):
		id_curriculo = BancoDeDados().consultarUnico('select id from curriculo where id_curso = %s and id_escopo_disciplina = %s and id_disciplina = %s',(idcurso,id_escopo,id_disciplina) )
		if id_curriculo is None:
			BancoDeDados().executar('insert into curriculo (id_curso,id_escopo_disciplina,id_disciplina) values (%s,%s,%s)',(idcurso,id_escopo,id_disciplina))
		
	def pesquisamateria(self,codigo,creditos):
		for i in codigo:
			creditos = creditos[0].replace(" ","-")
			id_disciplina = BancoDeDados().consultarUnico("select id from disciplina where codigo = %s",(i,))
			if id_disciplina is not None:
				#BancoDeDados().executar('update disciplina set creditos = %s where codigo = %s',(creditos,i))
				return id_disciplina[0]		








