from Framework.Resposta import Resposta
from Models.Usuario.Usuario import Usuario as ModelUsuario

class RespostaEntrar(Resposta):

	def __init__(self,token=None,usuario=None):
		self.corpo = { 'token' : token , 'usuario' : ModelUsuario(usuario) }