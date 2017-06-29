from Framework.Resposta import Resposta
from Models.Usuario.Usuario import Usuario as ModelUsuario

class RespostaCadastrar(Resposta):

	def __init__(self,usuario):
		self.corpo = ModelUsuario(usuario)