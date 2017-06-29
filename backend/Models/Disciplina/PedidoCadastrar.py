from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.id_departamento= self.corpo['id_departamento']
			self.nome = self.corpo['nome']
			self.codigo = self.corpo['codigo']

		except:
			raise ErroNoHTTP(400)
		
	def getId_departamento(self):
		return self.id_departamento

	def getNome(self):
		return self.nome
		
	def getCodigo(self):
		return self.codigo
