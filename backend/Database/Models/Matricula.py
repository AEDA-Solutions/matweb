from Database.Controllers.Grau import Grau
from Database.Controllers.Campus import Campus

class Curso(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			self.id_usuario = dados ['id_usuario']
			self.id_disciplina = dados ['id_disciplina']
		        self.ano = dados ['ano']
                        self.periodo = dados ['periodo']
			
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome
		
	def setId_usuario(self,id_usuario):
		self.id_usuario = id_usuario
		
	def getId_usuario(self):
		return self.id_usuario
		
	def getUsuario(self):
		return (Usuario().pegarUsuario('id = %s',(self.id_usuario))).getNome()
	
	def setId_disciplina(self,id_disciplina):
		self.id_disclipina = id_disciplina
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disciplina))).getDisciplina()
	
	def setPeriodo(self,periodo):
		self.periodo = periodo

	def getPeriodo(self):
		return self.periodo
	
	def setAno(self,ano):
		self.ano = ano
	
	def getAno(self):
		return self.ano
