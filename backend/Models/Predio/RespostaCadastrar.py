from Framework.Resposta import Resposta
from Models.Predio.Predio import Predio as ModelPredio

class RespostaCadastrar(Resposta):

	def __init__(self,predio):
		self.corpo = ModelPredio(predio)
