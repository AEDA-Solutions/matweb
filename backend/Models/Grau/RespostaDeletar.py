from Framework.Resposta import Resposta
from Models.Grau.Grau import Grau as ModelGrau

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
