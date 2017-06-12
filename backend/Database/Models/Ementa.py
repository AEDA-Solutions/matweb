
class Ementa(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.arquivo = dados ['arquivo']
			self.id_disciplina = dados ['id_disciplina']
			self.id_ementa = dados ['id_ementa']
			
	def getId(self):
		return self.id

	def setArquivo(self,arquivo):
		self.arquivo = arquivo

	def getArquivo(self):
		return self.arquivo
		
