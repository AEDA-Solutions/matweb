from Framework.Resposta import Resposta
from Models.Usuario.Usuario import Usuario as ModelUsuario

class RespostaEntrar(Resposta):

	def __init__(self,usuarios):
		self.corpo = []
		for usuario in usuarios:
			self.corpo.append(ModelUsuario(usuario))