from Database.Controllers.Grau import Grau
from Database.Controllers.Campus import Campus

class Curso(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.codigo = dados ['codigo']
			self.id_campus = dados ['id_campus']
		        self.id_grau = dados ['id_grau']
                        self.permanencia_minima = dados ['permanencia_minima']
                        self.permanencia_maxima = dados ['permanencia_maxima']
                        self.creditos_formatura = dados ['creditos_formatura']
                        self.creditos_optativos_concentracao = dados ['creditos_optativos_concentracao']
                        self.creditos_optativos_conexa = dados ['creditos_optativos_conexa']
                        self.creditos_livres_maximo = dados ['creditos_livres_maximo']
			self.mec = dados ['mec']
			
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
		
	def setId_campus(self,id_campus):
		self.id_campus = id_campus
		
	def getId_campus(self):
		return self.id_campus
		
	def getCampus(self):
		return (Campus().pegarCampus('id = %s',(self.id_campus))).getNome()
	
	def setId_grau(self,id_grau):
		self.id_grau = id_grau
		
	def getId_grau(self):
		return self.id_grau
		
	def getGrau(self):
		return (Grau().pegarGrau('id = %s',(self.id_grau))).getNome()
	
	def setPermanencia_minima(self,permanencia_minima):
		self.permanencia_minima = permanencia_minima

	def getPermanencia_minima(self):
		return self.permanencia_minima
	
	def setPermanencia_maxima(self,permanencia_maxima):
		self.permanencia_maxima = permanencia_maxima
	
	def getPermanencia_maxima(self):
		return self.permanencia_maxima
	
	def setCreditos_formatura(self,creditos_formatura):
		self.creditos_formatura = creditos_formatura
	
	def getCreditos_formatura(self):
		return self.creditos_formatura

        def setCreditos_optativos_concentracao(self,creditos_optativos_concentracao):
		self.creditos_optativos_concentracao = creditos_optativos_concentracao
	
	def getCreditos_optativos_concentracao(self):
		return self.creditos_optativos_concentracao
	
	def setCreditos_optativos_conexa(self,creditos_optativos_conexa):
		self.creditos_optativos_conexa = creditos_optativos_conexa
	
	def getCreditos_optativos_conexa(self):
		return self.creditos_optativos_conexa
	
	def setCreditos_livres_maximo(self,creditos_livres_maximo):
		self.creditos_livres_maximo = creditos_livres_maximo
	
	def getCreditos_livres_maximo(self):
		return self.creditos_livres_maximo
	
	def setMec(self,mec):
		self.mec = mec
	
	def getMec(self):
		return self.mec
