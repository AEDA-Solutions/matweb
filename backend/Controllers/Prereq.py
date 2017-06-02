# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Prereq import Prereq as BDPrereq
from Models.Prereq.RespostaListar import RespostaListar
from Models.Prereq.RespostaCadastrar import RespostaCadastrar
from Models.Prereq.RespostaEditar import RespostaEditar
from Models.Prereq.RespostaVer import RespostaVer
from Models.Prereq.RespostaDeletar import RespostaDeletar
from Database.Models.Prereq import Prereq as ModelPrereq

class Prereq(Controller):

      def Listar(self,pedido_listar):
             		      return RespostaListar(BDPrereq().pegarPrereqs("WHERE id_disc_pre = %s AND grupo LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdDisc_pre(),"%".pedido_listar.getCodigo().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))
	
	def Ver(self, pedido_ver):
		return RespostaVer(BDPrereq().pegarPrereqs("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		prereq = ModelPrereq()
		prereq.setNome(pedido_cadastrar.getNome())
		return RespostaCadastrar(BDPrereq().inserirPrereq(prereq))

	def Editar(self,pedido_editar):
		prereq = BDPrereq().pegarPrereqs("WHERE id = %s ", (pedido_editar.getId()))
		prereq.setNome(pedido_editar.getNome())
		BDPrereq().alterarPrereq(prereq)
		return RespostaEditar("Prereq Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		prereq = BDPrereq().pegarPrereqs("WHERE id = %s ", (pedido_deletar.getId()))		
		BDPrereq().removerPrereq(prereq)
		return RespostaDeletar("Prereq Removido com sucesso!")
