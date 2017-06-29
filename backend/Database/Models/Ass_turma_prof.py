from Database.Controllers.Turma import Turma
from Database.Controllers.Usuario import Usuario
from Database.Controllers.Disciplina import Disciplina

class Ass_turma_prof(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_turma = dados ['id_turma']
			self.id_prof = dados ['id_prof']
			
	def getId(self):
		return self.id

	def setId_turma(self,turma,disciplina):
		id_disciplina= (Disciplina().pegarDisciplina('nome = %s',(disciplina,))).getId()
		self.id_turma = (Turma().pegarTurma('letra = %s AND id_disciplina = %s',(turma,id_disciplina))).getId()

	def getId_turma(self):
		return self.id_turma
		
	def getTurma(self):
		return (Turma().pegarTurma('id = %s',(self.id_turma,))).getLetra()

	def setId_prof(self,professor):
		self.id_prof = (Usuario().pegarUsuario('nome = %s',(professor,))).getId()
		
	def getId_prof(self):
		return self.id_prof
	
	def getUsuario(self):
		return (Usuario().pegarUsuario('id = %s',(self.id_prof,))).getNome()
		
	