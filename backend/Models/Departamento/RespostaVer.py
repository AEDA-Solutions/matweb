from Framework.Resposta import Resposta
from Models.Departamento.Departamento import Departamento as ModelDepartamento

class RespostaVer(Resposta):

	def __init__(self,departamento):
		self.corpo = ModelDepartamento(departamento)