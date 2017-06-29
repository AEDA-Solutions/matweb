from Framework.Resposta import Resposta
from Models.Departamento.Departamento import Departamento as ModelDepartamento
class RespostaListar(Resposta):

	def __init__(self,departamentos):
		self.corpo = []
		for departamento in departamentos:
			self.corpo.append(ModelDepartamento(departamento))