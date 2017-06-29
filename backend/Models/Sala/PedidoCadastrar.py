from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.codigo = self.corpo['codigo']
			self.id_resp_sala = self.corpo['id_resp_sala']
			self.id_predio = self.corpo['id_predio'] 
		except:
			raise ErroNoHTTP(400)

	def getCodigo(self):
		return self.codigo
	
	def getId_resp_sala(self):
		return self.id_resp_sala
	
	def getId_predio(self):
		return self.id_predio

#abcd
#asdasdasds