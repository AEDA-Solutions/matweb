from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.codigo = self.corpo['codigo']
			self.id_resp_sala = self.corpo['id_resp_sala']
			self.id_predio = self.corpo['id_predio']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	def getCodigo(self):
		return self.codigo
	
	def getId_resp_sala(self):
		return self.id_resp_sala
	
	def getId_predio(self):
		return self.id_predio
