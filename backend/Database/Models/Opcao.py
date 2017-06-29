from Database.Controllers.Curso import Curso

class Opcao(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.id_curso = dados ['id_curso']
			
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome
		
	def setId_curso(self,curso):
		self.id_curso = (Curso().pegarCurso('nome = %s',(curso))).getId()
		
	def getId_curso(self):
		return self.id_curso
		
	def getCurso(self):
		return (Curso().pegarCurso('id = %s',(self.id_curso,))).getNome()
