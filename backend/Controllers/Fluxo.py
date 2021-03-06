from Framework.Controller import Controller
from Database.Controllers.Ass_periodo_disciplina import Ass_periodo_disciplina as BDAssociacao
from Models.Fluxo.RespostaListar import RespostaListar


class Fluxo(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDAssociacao().pegarResumoAss("WHERE periodo.id_curso = %s" % (pedido_listar.getId_curso(),),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))