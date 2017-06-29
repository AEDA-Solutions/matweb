from Framework.Resposta import Resposta
from Models.Departamento.Departamento import Departamento as ModelDepartamento

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem