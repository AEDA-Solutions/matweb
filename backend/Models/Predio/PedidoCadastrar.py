from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.nome = self.corpo['nome']
			self.sigla = self.corpo['sigla']
			self.latitude = self.corpo['latitude']
			self.longitude = self.corpo['longitude']
		except:
			raise ErroNoHTTP(400)

	def getNome(self):
		return self.nome
		
	def getSigla(self):
		return self.sigla
		
	def getLatitude(self):
		return self.latitude
	
	def getLongitude(self):
		return self.longitude
