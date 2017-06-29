from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Curriculo import Curriculo

class Curriculo_disciplina(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.obrigatorio = dados['obrigatorio']
			self.ciclo = dados['ciclo']
			self.grupo = dados['grupo']
			self.id_disciplina = dados['id_disciplina']
			self.id_curriculo = dados['id_curriculo']						
				
	def getId(self):
		return self.id
	
	def setObrigatorio(self,obrigatorio):
		self.obrigatorio = obrigatorio
		
	def getObrigatorio(self):
		return self.obrigatorio
		
	def setCiclo(self,ciclo):
		self.ciclo = ciclo
		
	def getCiclo(self):
		return self.ciclo
		
	def setGrupo(self,grupo):
		self.grupo = grupo
		
	def getGrupo(self):
		return self.grupo
			
	def setId_disciplina(self,disciplina):
		self.id_disciplina = (Disciplina().pegarDisciplina('nome = %s',(disciplina))).getId()
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disciplina))).getNome()
	
	def setId_curriculo(self,curriculo):
		self.id_curriculo = (Curriculo().pegarCurriculo('nome = %s',(curriculo))).getId()
		
	def getId_curriculo(self):
		return self.id_curriculo
		
	def getCurriculo(self):
		return (Curriculo().pegarCurriculo('id = %s',(self.id_curriculo))).getNome()
