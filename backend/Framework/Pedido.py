from Framework.ErroNoHTTP import ErroNoHTTP
import json

class Pedido(object):

	def __init__(self,variaveis_do_ambiente):
		self.variaveis_do_ambiente = variaveis_do_ambiente
		try:
			self.corpo = json.loads(self.variaveis_do_ambiente['wsgi.input'].read(int(self.variaveis_do_ambiente['CONTENT_LENGTH'])))
		except:
			raise ErroNoHTTP(400)