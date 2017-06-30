from Database.Controllers.Curso import Curso
from Database.Controllers.Escopo_disciplina import Escopo_disciplina
from Database.Controllers.Disciplina import Disciplina

class Curriculo(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_curso = dados['id_curso']
			self.id_escopo_disciplina = dados ['id_escopo_disciplina']
			self.id_disciplina = dados ['id_disciplina']
				
	def getId(self):
		return self.id
		
	def setId_curso(self,curso):
		self.id_curso = (Curso().pegarCurso('nome = %s',(curso,))).getId()
		
	def getId_curso(self):
		return self.id_curso
		
	def getCurso(self):
		return (Curso().pegarCurso('where id = %s',(self.id_curso,))).getNome()
	
	def setId_escopo_disciplina(self,id_escopo_disciplina):
		self.id_escopo_disciplina = id_escopo_disciplina
		
	def getId_escopo_disciplina(self):
		return self.id_escopo_disciplina
		
	def getEscopo_disciplina(self):
		return (Escopo_disciplina().pegarEscopo_disciplina('where id = %s',(self.id_escopo_disciplina,))).getNome()
		
	def setId_disciplina(self,id_disciplina):
		self.id_disciplina = id_disciplina
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('where id = %s',(self.id_disciplina,))).getNome()