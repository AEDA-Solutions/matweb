from Database.Controllers.Curso import Curso
from Database.Controllers.Opcao import Opcao

class Fluxo(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.periodo_inicio = dados ['periodo_inicio']
			self.periodo_fim = dados ['periodo_fim']
			self.id_curso = dados ['id_curso']
		        self.id_opcao = dados ['id_opcao']
	
	def getId(self):
		return self.id

	def setPeriodo_inicio(self,periodo_inicio):
		self.periodo_inicio = periodo_inicio

	def getPeriodo_inicio(self):
		return self.periodo_inicio

	def setPeriodo_fim(self,periodo_fim):
		self.periodo_fim = periodo_fim

	def getPeriodo_fim(self):
		return self.periodo_fim

	def setId_curso(self,curso):
		self.id_curso = (Curso().pegarCurso('nome = %s',(curso))).getId()
		
	def getId_curso(self):
		return self.id_curso
		
	def getCurso(self):
		return (Curso().pegarCurso('id = %s',(self.id_curso))).getNome()
	
	def setId_opcao(self,opcao):
		self.id_opcao = (Opcao().pegarOpcao('nome = %s',(opcao))).getId()
		
	def getId_opcao(self):
		return self.id_opcao
		
	def getOpcao(self):
		return (Opcao().pegarOpcao('id = %s',(self.id_opcao))).getNome()
	
	
