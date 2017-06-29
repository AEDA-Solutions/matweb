class Fluxo(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id_periodo = dados ['id_periodo']
			self.id_disciplina = dados ['id_disciplina']
			self.nome_disciplina = dados ['nome_disciplina']
			self.creditos_disciplina = dados ['creditos_disciplina']
	
	def setId_periodo(self,id_periodo):
		self.id_periodo = id_periodo
		
	def getId_periodo(self):
		return self.id_periodo
		
	def setId_disciplina(self,id_disciplina):
		self.id_disciplina = id_disciplina
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def setNome_disciplina(self,nome_disciplina):
		self.nome_disciplina = nome_disciplina
		
	def getNome_disciplina(self):
		return self.nome_disciplina
		
	def setCreditos_disciplina(self,creditos_disciplina):
		self.creditos_disciplina = credidos_disciplina
		
	def getCreditos_disciplina(self):
		return self.creditos_disciplina	
