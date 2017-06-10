from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
			self.id_predio = self.corpo['id_predio']
			self.codigo = self.corpo['codigo']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
		except:
			raise ErroNoHTTP(400)

	def getId_predio(self):
		return self.id_predio

	def getCodigo(self):
		return self.codigo

	def getPagina(self):
		return self.pagina

	def getQuantidade(self):
		return self.quantidade
