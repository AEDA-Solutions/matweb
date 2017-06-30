# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Curriculo import Curriculo as BDCurriculo
from Models.Curriculo.RespostaListar import RespostaListar
from Database.Models.Curriculo import Curriculo as ModelCurriculo

class Curriculo(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDCurriculo().pegarMultiplosCurriculo("WHERE id_curso = %s LIMIT %s OFFSET %s",("%"+pedido_listar.getId_curso().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))
