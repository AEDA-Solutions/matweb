from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
			self.quantidade = self.corpo['quantidade']
			self.pagina = self.corpo['pagina']
			self.nome = self.corpo['nome']
			
		except:
			raise ErroNoHTTP(400)

	def getNome(self):
		return self.nome
	
	def getQuantidade(self):
		return self.quantidade
	
	def getPagina(self):
	        return self.pagina
