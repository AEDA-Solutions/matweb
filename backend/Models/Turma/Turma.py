from Models.Horario.Horario import Horario as ModelHorario

class Turma(object):
	def __init__(self, turma, horarios):
		self.horarios = []
		self.id = turma.getId()
		self.letra = turma.getLetra()
		self.id_disciplina = turma.getId_disciplina()
		self.vagas = turma.getVagas()
		self.ocupadas = turma.getOcupadas()
		self.restantes = turma.getRestantes()
		self.id_professor = turma.getId_professor()
		self.professor = turma.getProfessor()
		self.turno = turma.getTurno()
		for horario in horarios:
			self.horarios.append(ModelHorario(horario))