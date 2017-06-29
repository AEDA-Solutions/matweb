class Horario(object):
	def __init__(self,horario,sala):
		self.id = horario.getId()
		self.inicio = str(horario.getInicio())
		self.fim = str(horario.getFim())
		self.dia = horario.getDia()
		self.sala = sala
