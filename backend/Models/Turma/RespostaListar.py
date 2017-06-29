from Framework.Resposta import Resposta
from Models.Turma.Turma import Turma as ModelTurma
class RespostaListar(Resposta):

	def __init__(self,turmas):
		self.corpo = []
		for turma in turmas:
			self.corpo.append(ModelTurma(turma))
