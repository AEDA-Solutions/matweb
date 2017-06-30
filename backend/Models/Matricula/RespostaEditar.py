from Framework.Resposta import Resposta
from Models.Matricula import Matricula as ModelMatricula

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
