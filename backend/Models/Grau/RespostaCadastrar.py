from Framework.Resposta import Resposta
from Models.Grau.Grau import Grau as ModelGrau

class RespostaCadastrar(Resposta):

	def __init__(self,grau):
		self.corpo = ModelGrau(grau)
