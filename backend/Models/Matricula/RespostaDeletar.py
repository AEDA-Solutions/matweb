from Framework.Resposta import Resposta
from Models.Matricula.Matricula import Matricula as ModelMatricula

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
