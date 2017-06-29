from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEntrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEntrar, self).__init__(variaveis_do_ambiente)
		try:
			self.usuario = self.corpo['usuario']
			self.senha = self.corpo['senha']
		except:
			raise ErroNoHTTP(400)

	def getLoginDoUsuario(self):
		return self.usuario

	def getSenhaDoUsuario(self):
		return self.senha