from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoDetalhar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
			self.nome = self.corpo['nome']
			self.id = self.corpo['id_curso']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
		except:
			raise ErroNoHTTP(400)
        
	def getNome(self):
		return self.nome
		
	def getId(self):
		return self.id
	
	def getPagina(self):
		return self.pagina
	
	def getQuantidade(self):
		return self.quantidade

	
