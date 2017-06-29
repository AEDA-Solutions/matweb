from Framework.Resposta import Resposta
from Models.Grau.Grau import Grau as ModelGrau

class RespostaVer(Resposta):

	def __init__(self,grau):
		self.corpo = ModelGrau(grau)
