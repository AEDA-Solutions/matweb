from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Periodo import Periodo

class Ass_periodo_disciplina(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_disciplina = dados ['id_disciplina']
			self.id_periodo = dados ['id_periodo']
			
	def getId(self):
		return self.id

	def setId_disciplina(self,id_disciplina):
		self.id_disciplina = id_disciplina

	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('where id = %s',(self.id_disciplina,))).getNome()

	def setId_periodo(self,id_periodo):
		self.id_periodo = id_periodo
		
	def getId_periodo(self):
		return self.id_periodo
		
	def getPeriodo(self):
		return (Periodo().pegarPeriodo('where id = %s',(id_periodo,))).pegarPeriodo()
		
	