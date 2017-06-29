from Framework.Resposta import Resposta
from Models.Campus.Campus import Campus as ModelCampus

class RespostaVer(Resposta):

	def __init__(self,campus):
		self.corpo = ModelCampus(campus)