from Framework.Controller import Controller
from Database.Controllers.Prereq import Prereq as BDPrereq
from Models.Prereq.RespostaListar import RespostaListar

class Prereq(Controller):

      def Listar(self,pedido_listar):
             		      return RespostaListar(BDPrereq().pegarPrereqs("WHERE id_disc_pre = %s AND grupo LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdDisc_pre(),"%".pedido_listar.getCodigo().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))
