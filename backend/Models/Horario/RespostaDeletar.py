from Framework.Resposta import Resposta
from Models.Horario.Horario import Horario as ModelHorario

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem