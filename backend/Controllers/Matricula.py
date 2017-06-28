from Framework.Controller import Controller
from Database.Controllers.Matricula import Curso as BDMatricula
from Models.Matricula.RespostaListar import RespostaListar
from Models.Matricula.RespostaCadastrar import RespostaCadastrar
from Models.Matricula.RespostaEditar import RespostaEditar
from Models.Matricula.RespostaVer import RespostaVer
from Models.Matricula.RespostaDeletar import RespostaDeletar
from Database.Models.Matricula import Matricula as ModelMatricula


class Curso(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDMatricula().pegarMatriculas("WHERE id_usuario = %s AND id_disciplina = %s AND nome LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdUsuario()),str(pedido_listar.getIdDisciplina()),"%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDMatricula().pegarMatricula("WHERE id = %s ", (str(pedido_ver.getId()),)))

	def Cadastrar(self,pedido_cadastrar):
		curso = ModelMatricula()
		curso.setNome(pedido_cadastrar.getNome())
		curso.setId_usuario(pedido_cadastrar.getId_usuario())
		curso.setId_disciplina(pedido_cadastrar.getId_disciplina())
		curso.setPeriodo(pedido_cadastrar.getPeriodo())
		curso.setAno(pedido_cadastrar.getAno())
		return RespostaCadastrar(BDMatricula().inserirMatricula(matricula))

	def Editar(self,pedido_editar):
		matricula = BDMatricula().pegarMatricula("WHERE id = %s ", (pedido_editar.getId()))
		curso.setNome(pedido_editar.getNome())
		curso.setId_disciplina(pedido_editar.getId_disciplina())
		curso.setId_usuario(pedido_editar.getId_usuario())
		curso.setPeriodo(pedido_editar.getPeriodo())
		curso.setAno(pedido_editar.getAno())
		BDMatricula().alterarMatricula(matricula)
		return RespostaEditar("Matricula Editada com sucesso!")

	def Deletar(self,pedido_deletar):
		matricula = BDMatricula().pegarMatricula("WHERE id = %s ", (pedido_deletar.getId()))		
		BDMatricula().removerMatricula(matricula)
		return RespostaDeletar("Matricula Removida com sucesso!")
