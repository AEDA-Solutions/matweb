from Framework.Resposta import Resposta
from Models.Disciplina.Disciplina import Disciplina as ModelDisciplina

class RespostaDeletar(Resposta):

	def __init__(self,mensagem):
		self.corpo = mensagem
