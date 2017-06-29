from Framework.Resposta import Resposta
from Models.Campus.Campus import Campus as ModelCampus

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem