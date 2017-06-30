from Framework.Resposta import Resposta
from Models.Matricula.Matricula import Matricula as ModelMatricula
class RespostaListar(Resposta):

	def __init__(self,matriculas):
		self.matricula = []
		for matricula in matriculas:
			self.corpo.append(ModelMatricula(matricula))
