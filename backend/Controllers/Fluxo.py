from Framework.Controller import Controller
from Database.Controllers.Ass_periodo_disciplina import Ass_periodo_disciplina as BDAssociacao
from Models.Fluxo.RespostaListar import RespostaListar


class Fluxo(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDAssociacao().pegarResumoAss("WHERE id_periodo = %s" % (pedido_listar.getId_periodo(),),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))