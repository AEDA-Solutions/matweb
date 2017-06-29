from Framework.Resposta import Resposta
from Models.Predio.Predio import Predio as ModelPredio

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		
			self.corpo = mensagem
