from Framework.Resposta import Resposta
from Models.Curso.Curso import Curso as ModelCurso

class RespostaVer(Resposta):

	def __init__(self,curso):
		self.corpo = ModelCurso(curso)
