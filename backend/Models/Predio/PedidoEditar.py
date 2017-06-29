from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']
			self.id_campus = self.corpo['id_campus']
			self.nome = self.corpo['nome']
			self.sigla = self.corpo['sigla']
			self.latitude = self.corpo['latitude']
			self.longitude = self.corpo['longitude']
			self.id_campus = self.corpo['id_campus']
		except:
			raise ErroNoHTTP(400)
		
	def getId(self):
		return self.id

	def getNome(self):
		return self.nome
		
	def getSigla(self):
		return self.sigla
		
	def getLatitude(self):
		return self.latitude
	
	def getLongitude(self):
		return self.longitude
	
	def getId_campus(self):
		return self.id_campus
