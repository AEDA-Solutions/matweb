from Framework.Resposta import Resposta
from Models.Disciplina.Disciplina import Disciplina as ModelDisciplina

class RespostaCadastrar(Resposta):

	def __init__(self,disciplina):
		self.corpo = ModelDisciplina(disciplina)
