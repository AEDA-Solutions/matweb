from Framework.Resposta import Resposta
from Models.Curriculo.Curriculo import Curriculo as ModelCurriculo
class RespostaListar(Resposta):

	def __init__(self,curriculos):
		self.corpo = []
		for curriculo in curriculos:
			self.corpo.append(ModelCurriculo(curriculo))