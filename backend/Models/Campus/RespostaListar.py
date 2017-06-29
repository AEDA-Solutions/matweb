from Framework.Resposta import Resposta
from Models.Campus.Campus import Campus as ModelCampus
class RespostaListar(Resposta):

	def __init__(self,campus):
		self.corpo = []
		for um_campus in campus:
			self.corpo.append(ModelCampus(um_campus))