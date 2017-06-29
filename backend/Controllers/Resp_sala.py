from Framework.Controller import Controller
from Database.Controllers.Resp_sala import Resp_sala as BDResp_sala
from Models.Resp_sala.RespostaListar import RespostaListar

class Campus(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDResp_sala().pegarMultiplosResp_sala("WHERE nome LIKE %s LIMIT %s OFFSET %s",("%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))
