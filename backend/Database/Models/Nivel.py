class Nivel(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.nome = dados ['nome']
			
	def getId(self):
		return self.id

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome
