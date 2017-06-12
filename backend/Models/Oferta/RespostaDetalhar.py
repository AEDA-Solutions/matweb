from Framework.Resposta import Resposta
from Models.Oferta.Oferta import Oferta as ModelOferta
class RespostaDetalhar(Resposta):

	def __init__(self,oferta,turmas):
		self.corpo = ModelOferta(oferta,turmas)
		