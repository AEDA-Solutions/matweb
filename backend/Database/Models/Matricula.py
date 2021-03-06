from Database.Controllers.Usuario import Usuario
from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Turma import Turma

class Curso(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_disciplina = dados ['id_disciplina']
			self.id_usuario = dados ['id_usuario']
			self.id_turma = dados ['id_turma']
			self.status = dados ['status']
			
	def getId(self):
		return self.id

	def setId_usuario(self,id_usuario):
		self.id_usuario = id_usuario
		
	def getId_usuario(self):
		return self.id_usuario
		
	def getUsuario(self):
		return (Usuario().pegarUsuario('where id = %s',(self.id_usuario))).getNome()
	
	def setId_disciplina(self,id_disciplina):
		self.id_disclipina = id_disciplina
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('where id = %s',(self.id_disciplina))).getDisciplina()
	
	def setStatus = (self,status):
		self.status = status
		
	def getStatus = (self):
		return self.status
		
	def setId_turma(self,id_turma):
		self.id_turma = id_turma
		
	def getId_turma(self):
		return self.id_turma
		
	def getTurma(self):
		return (Turma().pegarTurma('where id = %s',(self.id_turma,))).getLetra()
		
