from Database.Controllers.Turma import Turma
from Database.Controllers.Usuario import Usuario
from Database.Controllers.Disciplina import Disciplina

class Ass_aluno_turma(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_turma = dados ['id_turma']
			self.id_aluno = dados ['id_aluno']
			
	def getId(self):
		return self.id

	def setId_turma(self,turma,disciplina):
		id_disciplina= (Disciplina().pegarDisciplina('nome = %s',(disciplina,))).getId()
		self.id_turma = (Turma().pegarTurma('letra = %s AND id_disciplina = %s',(turma,id_disciplina))).getId()

	def getId_turma(self):
		return self.id_turma
		
	def getTurma(self):
		return (Turma().pegarTurma('id = %s',(self.id_turma,))).getLetra()

	def setId_aluno(self,aluno):
		self.id_aluno = (Usuario().pegarUsuario('nome = %s',(aluno,))).getId()
		
	def getId_aluno(self):
		return self.id_aluno
	
	def getUsuario(self):
		return (Usuario().pegarUsuario('id = %s',(self.id_aluno,))).getNome()
