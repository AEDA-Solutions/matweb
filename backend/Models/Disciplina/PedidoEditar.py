from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.id_departamento= self.corpo['id_departamento']
			self.nome = self.corpo['nome']
			self.codigo = self.corpo['codigo']
		except:
			raise ErroNoHTTP(400)

	def getId(self):
		return self.id

	def getId_departamento(self):
		return self.id_departamento

	def getNome(self):
		return self.nome
		
	def getCodigo(self):
		return self.codigo
