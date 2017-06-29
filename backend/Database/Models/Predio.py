from Database.Controllers.Campus import Campus

class Predio(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.sigla = dados ['sigla']
			self.latitude = dados ['latitude']
			self.longitude = dados ['longitude']
			self.id_campus = dados ['id_campus']
			
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def setSigla(self,sigla):
		self.sigla = sigla
		
	def getSigla(self):
		return self.sigla
		
	def setLatitude(self,latitude):
		self.latitude = latitude
	
	def getLatitude(self):
		return self.latitude
		
	def setLongitude(self,longitude):
		self.longitude = longitude
	
	def getLongitude(self):
		return self.longitude
		
	def setId_campus(self,id_campus):
		self.id_campus = id_campus
		
	def getId_campus(self):
		return self.id_campus
		
	def getCampus(self):
		return (Campus().pegarCampus('id = %s',(self.id_campus,))).getNome()