from Framework.Resposta import Resposta
from Models.Sala.Sala import Sala as ModelSala

class RespostaCadastrar(Resposta):

	def __init__(self,sala):
		self.corpo = ModelSala(sala)
