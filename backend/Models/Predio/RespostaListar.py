from Framework.Resposta import Resposta
from Models.Predio.Predio import Predio as ModelPredio
class RespostaListar(Resposta):

	def __init__(self,predios):
		self.corpo = []
		for predio in predios:
			self.corpo.append(ModelPredio(predio))
