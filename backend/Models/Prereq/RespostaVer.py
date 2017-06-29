from Framework.Resposta import Resposta
from Models.Prereq.Prereq import Prereq as ModelPrereq

class RespostaVer(Resposta):

	def __init__(self,prereq):
		self.corpo = ModelPrereq(prereq)