from Framework.Resposta import Resposta
from Models.Usuario.Usuario import Usuario as ModelUsuario

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		
			self.corpo = mensagem