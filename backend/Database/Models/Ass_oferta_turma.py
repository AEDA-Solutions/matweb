from Database.Controllers.Oferta import Oferta
from Database.Controllers.Turma import Turma

class Ass_oferta_turma(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_oferta = dados ['id_oferta']
			self.id_turma = dados ['id_turma']
			
	def getId(self):
		return self.id

	def setId_oferta(self,id_oferta):
		self.id_oferta = id_oferta

	def getId_oferta(self):
		return self.id_oferta
		
	def getOferta(self):
		return (Oferta().pegarOferta('where id = %s',(self.id_oferta,)))
		
	def setId_turma(self,id_turma):
		self.id_turma = id_turma
		
	def getId_turma(self):
		return self.id_turma
	
	def getTurma(self):
		return (Turma().pegarTurma('where id = %s',(self.id_turma,))).getLetra()