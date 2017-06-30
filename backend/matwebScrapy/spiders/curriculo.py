# -*- coding: utf-8 -*-
import scrapy
from Framework.BancoDeDados import BancoDeDados
import re

class matweb(scrapy.Spider):
	name = "curriculo"
	
	def start_requests(self):
		urls = 'https://matriculaweb.unb.br/graduacao/curriculo.aspx?cod=6131'
		yield scrapy.Request(url=urls, callback=self.parse)
		
	def parse(self,response):
		linhas = response.xpath('//table[@class="Frame"][@width="80%"]/tr')
		for linha in linhas:
			coluna_nomes = linha.xpath('td/b/text()').extract()
			coluna1 = linha.xpath('td[2]')
			coluna2 = linha.xpath('td[3]/text()').extract()
			self.tratalinha(coluna_nomes,coluna1,coluna2)
			self.tratamaterias(linha)
			
	def tratalinha(self,coluna_nomes,coluna1,coluna2):
		if coluna_nomes is not None:
			if u"Curso:" in coluna_nomes:
				print('Curso eh ',coluna2)
			if u"Habilitação:" in coluna_nomes:
				print("Habilitacao eh ",coluna2)
			if u"Nível:" in coluna_nomes:
				print("Nivel eh ",coluna2)
			if u"Reconhecida pelo MEC:" in coluna_nomes:
				print ("Reconhecida pelo MEC ",coluna1.xpath('text()').extract())
			if u"Duração:" in coluna_nomes:
				print ("Duracao ",coluna1.xpath('text()').extract())
			if u"Créditos por período:" in coluna_nomes:
				minimo = coluna1.xpath('nobr/text()').extract()
				print ('minimo por periodo ', re.findall('\d+', minimo[0]))
				print ('maximo por periodo ', re.findall('\d+', coluna2[0]))
			if u"Limite de Permanência" in coluna_nomes:
				print ('permanencia minima ',coluna1.xpath('text()').extract())
				print ('permanencia maxima ',coluna2)
			if u"Créditos exigidos:" in coluna_nomes:
				print ('creditos ',coluna1.xpath('text()').extract())
			if u"Módulo Livre:" in coluna_nomes:
				print ('modulo livre ',coluna1.xpath('text()').extract())
	
	def tratamaterias(self,linha):
		planilhas = linha.xpath('td[@class="Padrao"]')
		for planilha in planilhas:
			titulo = planilha.xpath('b/font[@class="padrao"]/text()').extract()
			print(titulo[0].lstrip())
			disciplinas = planilha.xpath('table[@class="FrameCinza"]/tr')
			self.tratadisciplina(disciplinas)
			
	
	def tratadisciplina(self,disciplinas):
		for disciplina in disciplinas:
			codigo = disciplina.xpath('td/a/b/text()').extract()
			self.pesquisamateria(codigo)
			creditos = disciplina.xpath('td[3]/text()').extract()
		
	def pesquisamateria(self,codigo):
		for i in codigo:
			disciplina = BancoDeDados().consultarMultiplos("select id from disciplina where codigo = %s",(i,))
			print(disciplina,codigo) 
		





















