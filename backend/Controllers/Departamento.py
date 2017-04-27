# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Departamento import Departamento as BDDepartamento
from Models.Departamento.RespostaListar import RespostaListar
from Models.Departamento.RespostaCadastrar import RespostaCadastrar
from Models.Departamento.RespostaEditar import RespostaEditar
from Models.Departamento.RespostaVer import RespostaVer
from Models.Departamento.RespostaDeletar import RespostaDeletar
from Database.Models.Departamento import Departamento as ModelDepartamento


class Departamento(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDDepartamento().pegarDepartamentos("WHERE id_departamento = %s AND nome LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdDepartamento()),"%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDDepartamento().pegarDepartamentos("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		departamento = ModelDepartamento()
		departamento.setNome(pedido_cadastrar.getNome())
		return RespostaCadastrar(BDDepartamento().inserirDepartamento(departamento))

	def Editar(self,pedido_editar):
		departamento = BDDepartamento().pegarDepartamentos("WHERE id = %s ", (pedido_editar.getId()))
		departamento.setNome(pedido_editar.getNome())
		BDDepartamento().alterarDepartamento(departamento)
		return RespostaEditar("Departamento Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		departamento = BDDepartamento().pegarDepartamentos("WHERE id = %s ", (pedido_deletar.getId()))		
		BDDepartamento().removerDepartamento(departamento)
		return RespostaDeletar("Departamento Removido com sucesso!")

