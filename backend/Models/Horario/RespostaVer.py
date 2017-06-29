from Framework.Resposta import Resposta
from Models.Horario.Horario import Horario as ModelHorario

class RespostaVer(Resposta):

	def __init__(self,horario):
		self.corpo = ModelHorario(horario)