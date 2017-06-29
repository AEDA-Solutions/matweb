import yaml

class Configuracao(object):

	configuracao = None

	def __init__(self):
		if Configuracao.configuracao == None:
			with open("Configuracao/configuracao.yml", 'r') as ymlfile:
				Configuracao.configuracao = yaml.load(ymlfile)

	def getConfiguracao(self,nome):
		return Configuracao.configuracao[nome]