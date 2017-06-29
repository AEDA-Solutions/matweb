from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.nome = self.corpo['nome']
			self.codigo = self.corpo['codigo']
			self.sigla = self.corpo['sigla']
			self.id_campus = self.corpo['id_campus']
		except:
			raise ErroNoHTTP(400)

	def getId(self):
		return self.id

	def getNome(self):
		return self.nome

	
	def getCodigo(self):
		return self.codigo

		
	def getSigla(self):
		return self.sigla
		
		
	def getId_campus(self):
		return self.id_campus
		
	
