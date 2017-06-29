from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
			self.id_fluxo = self.corpo['id_fluxo']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
		except:
			raise ErroNoHTTP(400)

	def getId_fluxo(self):
		return self.id_fluxo

	def getPagina(self):
		return self.pagina

	def getQuantidade(self):
		return self.quantidade