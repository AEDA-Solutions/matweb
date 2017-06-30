from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.id_disciplina = self.corpo['id_disciplina']
			self.id_usuario = self.corpo['id_usuario']
			self.status = self.corpo['status']
		except:
			raise ErroNoHTTP(400)
			

	def getId(self):
		return self.id
	
	def getId_disciplina(self):
		return self.id_disciplna
		
	def getId_usuario(self):
		return self.id_usuario
		
	def getStatus(self):
		return self.status
