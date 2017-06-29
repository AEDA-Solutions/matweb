from Database.Controllers.Campus import Campus

class Departamento(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.codigo = dados ['codigo']
			self.sigla = dados ['sigla']
			self.id_campus = dados ['id_campus']
			
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def setCodigo(self,codigo):
		self.codigo = codigo
		
	def getCodigo(self):
		return self.codigo
		
	def setSigla(self,sigla):
		self.sigla = sigla
		
	def getSigla(self):
		return self.sigla
		
	def setId_campus(self,id_campus):
		self.id_campus = id_campus
		
	def getId_campus(self):
		return self.id_campus
		
	def getCampus(self):
		return  (Campus().pegarCampus('id = %s',(self.id_campus,))).getNome()
	