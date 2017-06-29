from Framework.Resposta import Resposta
from Models.Grau.Grau import Grau as ModelGrau
class RespostaListar(Resposta):

	def __init__(self,graus):
		self.corpo = []
		for grau in graus:
			self.corpo.append(ModelGrau(grau))
