from Framework.Resposta import Resposta

class RespostaListar(Resposta):

	def __init__(self,prereqs):
		self.corpo = []
		for prereq in prereqs:
			self.corpo.append(prereq)
