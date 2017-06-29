from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
			self.id = self.corpo['id']		
			self.turno = self.corpo['turno']
			self.inicio = self.corpo['inicio']
			self.fim = self.corpo['fim']
			self.dia = self.corpo['dia']
		except:
			raise ErroNoHTTP(400)
			
	def getTurno(self):
		return self.turno

	
	def getInicio(self):
		return self.inicio
		
	
	def getFim(self):
		return self.fim
		
	
	def getDia(self):
		return self.dia

	
	def getId(self):
		return self.id
