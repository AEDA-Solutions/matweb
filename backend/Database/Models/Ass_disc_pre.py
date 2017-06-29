from Database.Controllers.Disciplina import Disciplina
from Database.Controllers.Prereq import Prereq

class Ass_disc_pre(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_disciplina = dados ['id_disciplina']
			self.id_prereq = dados ['id_prereq']
			
	def getId(self):
		return self.id

	def setId_disciplina(self,disciplina):
		self.id_disciplina = (Disciplina().pegarDisciplina('nome = %s',(disciplina,))).getId()

	def getId_disciplina(self):
		return self.id_disciplina
		
	def getDisciplina(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disciplina,))).getNome()

	def setId_prereq(self,disciplina_requisito,grupo):
		id_disc_pre = (Disciplina().pegarDisciplina('nome = %s',(disciplina_requisito,))).getId()
		self.id_prereq = (Prereq().pegarPrereq('id_disc_pre = %s AND grupo = %s',(id_disc_pre,grupo))).getId()
		
	def getId_prereq(self):
		return self.id_prereq
		
	