from Framework.Resposta import Resposta
from Models.Prereq.Prereq import Prereq as ModelPrereq

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		
			self.corpo = mensagem