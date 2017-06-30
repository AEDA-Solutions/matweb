class Matricula(object):
	def __init__(self,matricula):
		self.id = matricula.getId()
		self.id_disciplina = matricula.getId_disciplina()
		self.id_usuario = matricula.getId_usuario()
		self.id_turma = matricula.getTurma()
		self.status = matricula.getStatus()
