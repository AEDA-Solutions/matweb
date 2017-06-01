from Framework.Controller import Controller
from Database.Controllers.Disciplina import Disciplina as BDDisciplina
from Database.Controllers.Ass_disc_pre import Ass_disc_pre
from Models.Prereq.RespostaListar import RespostaListar

class Prereq(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(Ass_disc_pre().pegarResumoAss("disciplina.id = %s",(BDDisciplina().pegarDisciplina("WHERE nome = %s",(pedido_listar.getDisciplina(),)))))
