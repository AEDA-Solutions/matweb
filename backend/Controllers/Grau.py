# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Grau import Grau as BDGrau
from Models.Grau.RespostaListar import RespostaListar
from Models.Grau.RespostaCadastrar import RespostaCadastrar
from Models.Grau.RespostaEditar import RespostaEditar
from Models.Grau.RespostaVer import RespostaVer
from Models.Grau.RespostaDeletar import RespostaDeletar
from Database.Models.Grau import Grau as ModelGrau

class Grau(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDGrau().pegarGraus("WHERE nome LIKE %s LIMIT %s OFFSET %s",("%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDGrau().pegarGrau("WHERE id = %s ", (str(pedido_ver.getId()),)))

	def Cadastrar(self, pedido_cadastrar):
		grau = ModelGrau()
		grau.setNome(pedido_cadastrar.getNome())
		return RespostaCadastrar(BDGrau().inserirGrau(grau))

	def Editar(self,pedido_editar):
		grau = BDGrau().pegarGrau("WHERE id = %s ", (str(pedido_editar.getId()),))
		grau.setNome(pedido_editar.getNome())
		BDGrau().alterarGrau(grau)
		return RespostaEditar("Grau Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		grau = BDGrau().pegarGrau("WHERE id = %s ", (str(pedido_deletar.getId()),))		
		BDGrau().removerGrau(grau)
		return RespostaDeletar("Grau Removido com sucesso!")
