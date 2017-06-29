from Framework.Resposta import Resposta
from Models.Fluxo.Fluxo import Fluxo as ModelFluxo

class RespostaListar(Resposta):

	def __init__(self,fluxos):
		self.corpo = []
		for fluxo in fluxos:
			self.corpo.append(ModelFluxo(fluxo))