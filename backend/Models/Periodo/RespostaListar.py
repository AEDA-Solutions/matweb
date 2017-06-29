from Framework.Resposta import Resposta
from Models.Periodo.Periodo import Periodo as ModelPeriodo

class RespostaListar(Resposta):

	def __init__(self,periodos):
		self.corpo = []
		for periodo in periodos:
			self.corpo.append(ModelPeriodo(periodo))