from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Fluxo import Fluxo

class Turma(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.periodo = dados ['periodo']
			self.id_disciplina = dados ['id_disciplina']
      self.id_fluxo = dados ['id_fluxo']
			
	def getId(self):
		return self.id

	def setPeriodo(self,periodo):
		self.periodo = periodo

	def getPeriodo(self):
		return self.periodo
		
	def setId_disciplina(self,disciplina):
		self.id_disciplina = (Disciplina().pegarDisciplina('nome = %s',(disciplina))).getId()
	
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disciplina))).getNome()
    
  def setId_fluxo(self,fluxo):
		self.id_fluxo = (Fluxo().pegarFluxo('nome = %s',(fluxo))).getId()
	
	def getId_fluxo(self):
		return self.id_fluxo
		
	def getFluxo(self):
		return (Fluxo().pegarFluxo('id = %s',(self.id_fluxo))).getNome()  
