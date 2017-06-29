# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Campus import Campus as BDCampus
from Models.Campus.RespostaListar import RespostaListar
from Models.Campus.RespostaCadastrar import RespostaCadastrar
from Models.Campus.RespostaEditar import RespostaEditar
from Models.Campus.RespostaVer import RespostaVer
from Models.Campus.RespostaDeletar import RespostaDeletar
from Database.Models.Campus import Campus as ModelCampus

class Campus(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDCampus().pegarMultiplosCampus("WHERE nome LIKE %s LIMIT %s OFFSET %s",("%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDCampus().pegarCampus("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		campus = ModelCampus()
		campus.setNome(pedido_cadastrar.getNome())
		return RespostaCadastrar(BDCampus().inserirCampus(campus))

	def Editar(self,pedido_editar):
		campus = BDCampus().pegarCampus("WHERE id = %s ", (pedido_editar.getId()))
		campus.setNome(pedido_editar.getNome())
		BDCampus().alterarCampus(campus)
		return RespostaEditar("Campus Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		campus = BDCampus().pegarCampus("WHERE id = %s ", (pedido_deletar.getId()))		
		BDCampus().removerCampus(campus)
		return RespostaDeletar("Campus Removido com sucesso!")

