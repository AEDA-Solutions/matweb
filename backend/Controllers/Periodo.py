from Framework.Controller import Controller
from Database.Controllers.Periodo import Periodo as BDPeriodo
from Models.Periodo.RespostaListar import RespostaListar


class Periodo(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDPeriodo().pegarPeriodos("WHERE id_curso = %s" % (pedido_listar.getId_curso(),),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))