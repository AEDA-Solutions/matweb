from Framework.Resposta import Resposta
from Models.Curso import Curso as ModelCurso

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		
			self.corpo = mensagem
