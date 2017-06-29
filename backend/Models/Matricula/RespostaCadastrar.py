from Framework.Resposta import Resposta
from Models.Matricula.Matricula import Matricula as ModelMatricula

class RespostaCadastrar(Resposta):

	def __init__(self,matricula):
		self.corpo = ModelMatricula(matricula)
