from Framework.Resposta import Resposta
from Models.Prereq.Prereq import Prereq as ModelPrereq
class RespostaListar(Resposta):

	def __init__(self,prereqs):
		self.corpo = []
		for prereq in prereqs:
			self.corpo.append(ModelPrereq(prereq))
