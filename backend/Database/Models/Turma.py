from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Professor import Professor

class Turma(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.letra = dados ['letra']
			self.id_disciplina = dados ['id_disciplina']
			self.vagas = dados['vagas']
			self.ocupadas = dados['ocupadas']
			self.restantes = dados['restantes']
			self.turno = dados['turno']
			self.id_professor = dados['id_professor']
			
	def getId(self):
		return self.id

	def setLetra(self,letra):
		self.letra = letra

	def getLetra(self):
		return self.letra
		
	def setVagas(self,vagas):
		self.vagas = vagas
	
	def getVagas(self):
		return self.vagas
	
	def setOcupadas(self,ocupadas):
		self.ocupadas = ocupadas
		
	def getOcupadas(self):
		return self.ocupadas
		
	def setRestantes(self,restantes):
		self.restantes = restantes
		
	def getRestantes(self):
		return self.restantes
		
	def setTurno(self,turno):
		self.turno = turno
		
	def getTurno(self):
		return self.turno
		
	def setId_disciplina(self,disciplina):
		self.id_disciplina = (Disciplina().pegarDisciplina('nome = %s',(disciplina,))).getId()
	
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disciplina,))).getNome()
		
	def setId_professor(self,professor):
		self.id_professor = (Professor().pegarProfessor('nome = %s',(professor,))).getId()
	
	def getId_professor(self):
		return self.id_professor
		
	def getProfessor(self):
		return (Professor().pegarProfessor('where id = %s',(self.id_professor,))).getNome()
