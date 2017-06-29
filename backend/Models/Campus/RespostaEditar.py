from Framework.Resposta import Resposta
from Models.Campus.Campus import Campus as ModelCampus

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		
			self.corpo = mensagem