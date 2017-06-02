# coding=utf-8
from Framework.Controller import Controller
from Database.Controllers.Turma import Turma as BDTurma
from Models.Turma.RespostaListar import RespostaListar
from Models.Turma.RespostaCadastrar import RespostaCadastrar
from Models.Turma.RespostaEditar import RespostaEditar
from Models.Turma.RespostaVer import RespostaVer
from Models.Turma.RespostaDeletar import RespostaDeletar
from Database.Models.Turma import Turma as ModelTurma

class Turma(Controller):

      def Listar(self,pedido_listar):
            return RespostaListar(BDTurma().pegarTurmas("WHERE id_disciplina = %s AND letra LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdDisciplina(),"%".pedido_listar.getLetra().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))
	
	def Ver(self, pedido_ver):
		return RespostaVer(BDTurma().pegarTurmas("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		turma = ModelTurma()
		turma.setNome(pedido_cadastrar.getNome())
		return RespostaCadastrar(BDTurma().inserirTurma(turma))

	def Editar(self,pedido_editar):
		turma = BDTurma().pegarTurma("WHERE id = %s ", (pedido_editar.getId()))
		turma.setNome(pedido_editar.getNome())
		BDTurma().alterarTurma(turma)
		return RespostaEditar("Turma Editada com sucesso!")

	def Deletar(self,pedido_deletar):
		turma = BDTurma().pegarTurma("WHERE id = %s ", (pedido_deletar.getId()))		
		BDTurma().removerTurma(turma)
		return RespostaDeletar("Turma Removida com sucesso!")
