class Horario(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.turno = dados ['turno']
			self.inicio = dados ['inicio']
			self.fim = dados ['fim']
			self.dia = dados ['dia']
						
	def getId(self):
		return self.id

	def setTurno(self,turno):
		self.turno = turno

	def getTurno(self):
		return self.turno

	def setInicio(self,inicio):
		self.inicio = inicio
		
	def getInicio(self):
		return self.inicio
		
	def setFim(self,fim):
		self.fim = fim
	
	def getFim(self):
		return self.fim
		
	def setDia(self,dia):
		self.dia = dia
	
	def getDia(self):
		return self.dia
