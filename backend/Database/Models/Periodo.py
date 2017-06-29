from Database.Controllers.Curso import Curso

class Periodo(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_curso = dados ['id_curso']
			self.periodo = dados ['periodo']
			self.creditos = dados ['creditos']
			
	def getId(self):
		return self.id

	def setId_curso(self,id_curso):
		self.id_curso = id_curso
		
	def getId_curso(self):
		return self.Id_curso
		
	def getCurso(self):
		return (Curso().pegarCurso('where id = %s', (self.id_curso,)).getNome()
	
	def setPeriodo(self,periodo):
		self.periodo = periodo
		
	def getPeriodo(self):
		return periodo
		
	def setCreditos(self,creditos):
		self.creditos = creditos
		
	def getCreditos(self):
		return self.creditos
		
	
			
	