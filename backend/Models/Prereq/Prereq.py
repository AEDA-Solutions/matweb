class Prereq(object):
	def __init__(self,associacao):
		self.disciplina = associacao.disciplina
		self.prereq = associacao.prereq
		self.grupo = associacao.grupo