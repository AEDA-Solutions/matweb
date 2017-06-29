class Fluxo(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.periodo = dados ['periodo']
			self.creditos_periodo = dados ['creditos_periodo']
			self.nome_disciplina = dados ['nome_disciplina']
			self.creditos_disciplina = dados ['creditos_disciplina']
	
	def getId(self):
		return self.id

	def setPeriodo(self,periodo):
		self.periodo = periodo
		
	def getPeriodo(self):
		return self.periodo
		
	def setCreditos_periodo(self,creditos_periodo):
		self.creditos_periodo = creditos_periodo
		
	def getCreditos_periodo(self):
		return self.creditos_periodo
		
	def setNome_disciplina(self,nome_disciplina):
		self.nome_disciplina = nome_disciplina
		
	def getNome_disciplina(self):
		return self.nome_disciplina
		
	def setCreditos_disciplina(self,creditos_disciplina):
		self.creditos_disciplina = credidos_disciplina
		
	def getCreditos_disciplina(self):
		return self.creditos_disciplina	
