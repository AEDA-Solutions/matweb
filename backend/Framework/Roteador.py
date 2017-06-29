from ErroNoHTTP import ErroNoHTTP
import importlib
import sys, traceback

class Roteador(object):

	def __init__(self,variaveis_do_ambiente):
		self.variaveis_do_ambiente = variaveis_do_ambiente
		try:
			self.realizarChecagens()
			self.executar()
		except ErroNoHTTP as erro_no_http:
			self.resposta = erro_no_http

	def checarMetodo(self):
		if(self.variaveis_do_ambiente['REQUEST_METHOD'] != "POST"):
			raise ErroNoHTTP(405)

	def checarTipoDeConteudo(self):
		if(self.variaveis_do_ambiente['CONTENT_TYPE'] != "application/json; charset=UTF-8"):
			raise ErroNoHTTP(415)

	def checarTamanhoDoCorpoDoPedido(self):	
		try:
			if(int(self.variaveis_do_ambiente['CONTENT_LENGTH']) <= 0):
				raise ErroNoHTTP(411)
		except ValueError:
			raise ErroNoHTTP(411)

	def checarURL(self,api):
		if(api != "api"):
			raise ErroNoHTTP(404)

	def ChecarTamanhoDaURL(self,caminho):
		if(len(caminho) < 4):
			raise ErroNoHTTP(404)

	def realizarChecagens(self):
		self.checarMetodo()
		self.checarTipoDeConteudo()
		self.checarTamanhoDoCorpoDoPedido()

	def getFuncao(self):
		self.funcao = {}
		caminho = self.variaveis_do_ambiente['PATH_INFO'].split('/')
		self.ChecarTamanhoDaURL(caminho)
		self.funcao['metodo'] = caminho[-1]
		self.funcao['controle'] = caminho[-2]
		self.checarURL(caminho[1])
		del caminho[-1]
		del caminho[1]
		del caminho[0]
		self.funcao['modulo'] = ".".join(caminho)

	def executar(self):
		self.getFuncao()
		try:
			controle = getattr(importlib.import_module("Controllers.{}".format(self.funcao['modulo'])), self.funcao['controle'])()
		except ImportError:
			traceback.print_exc(file=open("../frontend/log.txt",'w'))
			traceback.print_exc(file=sys.stdout)
			raise ErroNoHTTP(404)
		self.resposta = controle.executar(self.funcao,self.variaveis_do_ambiente)

	def getStatusDaResposta(self):
		return self.resposta.getStatus()

	def getCorpoDaResposta(self):
		return self.resposta.getCorpo()

	def getCabecalhoDaResposta(self):
		return self.resposta.getCabecalho()
