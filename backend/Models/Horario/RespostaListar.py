from Framework.Resposta import Resposta
from Models.Horario.Horario import Horario as ModelHorario
class RespostaListar(Resposta):

	def __init__(self,horarios):
		self.corpo = []
		for horario in horarios:
			self.corpo.append(ModelHorario(horario))