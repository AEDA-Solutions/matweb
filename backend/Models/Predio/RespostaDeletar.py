from Framework.Resposta import Resposta
from Models.Predio.Predio import Predio as ModelPredio

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
