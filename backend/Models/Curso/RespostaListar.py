from Framework.Resposta import Resposta
from Models.Curso.Curso import Curso as ModelCurso
class RespostaListar(Resposta):

	def __init__(self,cursos):
		self.corpo = []
		for curso in cursos:
			self.corpo.append(ModelCurso(curso))
