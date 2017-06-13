from Models.Turma.Turma import Turma as ModelTurma

class Oferta(object):
	def __init__(self,oferta,turmas):
		self.id = oferta.getId()
		self.id_disciplina = oferta.getId_disciplina()
		self.disciplina = oferta.getDisciplina()
		self.id_ementa = oferta.getId_ementa()
		self.creditos = oferta.getCreditos()
		self.turmas = []
		for turma in turmas:
			self.turmas.append(turma)
