from Database.Controllers.Sala import Sala
from Database.Controllers.Turma import Turma
from Database.Controllers.Horario import Horario
from Database.Controllers.Disciplina import Disciplina

class Ass_turma_sala_horario(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_sala = dados ['id_sala']
			self.id_turma = dados ['id_turma']
			self.id_horario = dados ['id_horario']
			
	def getId(self):
		return self.id

	def setId_sala(self,id_sala):
		self.id_sala = id_sala

	def getId_sala(self):
		return self.id_sala
		
	def getSala(self):
		return (Sala().pegarSala('where id = %s',(self.id_sala,))).getCodigo()

	def setId_turma(self,id_turma):
		self.id_turma = id_turma
		
	def getId_turma(self):
		return self.id_turma
	
	def getTurma(self):
		return (Turma().pegarTurma('where id = %s',(self.id_turma,))).getLetra()
		
	def setId_horario(self,id_horaio):
		sel.if_horario = id_horario
		
	def getId_horario(self):
		return self.id_horario
		
	def getHorario(self):
		return (Horario().pegarHorario('where id = %s',(self.id_horario,)))