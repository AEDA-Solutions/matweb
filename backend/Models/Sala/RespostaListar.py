from Framework.Resposta import Resposta
from Models.Sala.Sala import Sala as ModelSala
class RespostaListar(Resposta):

	def __init__(self,salas):
		self.corpo = []
		for sala in salas:
			self.corpo.append(ModelSala(sala))
