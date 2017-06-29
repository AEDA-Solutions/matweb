from Framework.Resposta import Resposta
from Models.Departamento.Departamento import Departamento as ModelDepartamento

class RespostaCadastrar(Resposta):

	def __init__(self,departamento):
		self.corpo = ModelDepartamento(departamento)