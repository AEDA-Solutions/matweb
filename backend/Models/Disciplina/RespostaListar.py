from Framework.Resposta import Resposta
from Models.Disciplina.Disciplina import Disciplina as ModelDisciplina
class RespostaListar(Resposta):

	def __init__(self,disciplinas):
		self.corpo = []
		for disciplina in disciplinas:
			self.corpo.append(ModelDisciplina(disciplina))