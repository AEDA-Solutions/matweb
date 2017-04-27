from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoDeletar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoDeletar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']			
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

