from Framework.Resposta import Resposta
from Models.Matricula.Matricula import Matricula as ModelMatricula

class RespostaVer(Resposta):

	def __init__(self,matricula):
		self.corpo = ModelMatricula(Matricula)
