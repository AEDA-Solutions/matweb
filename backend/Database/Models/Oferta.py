from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Ementa import Ementa

class Oferta(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.creditos = dados ['creditos']
			self.id_disciplina = dados ['id_disciplina']
			self.id_ementa = dados ['id_ementa']
			
	def getId(self):
		return self.id

	def setCreditos(self,creditos):
		self.creditos = creditos

	def getCreditos(self):
		return self.creditos
		
	def setId_disciplina(self,id_disciplina):
		self.id_disciplina = id_disciplina
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('where id = %s',(id_disciplina,))).getNome()
		
	def setId_ementa(self,id_ementa):
		self.id_ementa = id_ementa
	