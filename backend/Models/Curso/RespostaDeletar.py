from Framework.Resposta import Resposta
from Models.Curso.Curso import Curso as ModelCurso

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
