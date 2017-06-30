class Curriculo(object):
	def __init__(self,curriculo):
		self.id = curriculo.getId()
		self.curso = curriculo.getCurso()
		self.escopo_disciplina = curriculo.getEscopo_disciplina()
		self.disciplina = curriculo.getDisciplina()
		