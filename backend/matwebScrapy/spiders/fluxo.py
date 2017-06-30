# -*- coding: utf-8 -*-
import scrapy
from Framework.BancoDeDados import BancoDeDados
import re

class matweb(scrapy.Spider):
	name = "fluxo"
	
	def start_requests(self):
		urls = 'https://matriculaweb.unb.br/graduacao/fluxo.aspx?cod=6009'
		yield scrapy.Request(url=urls, callback=self.parse)
		
	def parse(self,response):
		tabelas = response.xpath('//table[@class="FrameCinza"][@width="95%"]')
		for tabela in tabelas:
			linhaperiodo = tabela.xpath('tr[@class="padraobranco"]/td/b')
			linhasmaterias = tabela.xpath('tr[@class="padraomenor"]/td[3]/a')
			self.trataperiodo(linhaperiodo)
			self.tratamaterias(linhasmaterias)


	def trataperiodo(self,linha):
		for coluna in linha:
			dado = coluna.xpath('text()').extract()
			for i in dado:
				if u"PERÍODO" in i:
					periodo = re.findall('\d+', i)
					print("Período ",periodo)
				else:
					print("Créditos ",i)
					
	def tratamaterias(self,linhas):
		for coluna in linhas:
			dado = coluna.xpath('text()').extract()
			print(dado)