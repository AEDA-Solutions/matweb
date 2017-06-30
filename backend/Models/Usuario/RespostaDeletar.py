from Framework.Resposta import Resposta
from Models.Usuario.Usuario import Usuario as ModelUsuario

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem