from Framework.Controller import Controller
from Database.Controllers.Matricula import Matricula as BDMatricula
from Models.Matricula.RespostaListar import RespostaListar
from Models.Matricula.RespostaCadastrar import RespostaCadastrar
from Models.Matricula.RespostaEditar import RespostaEditar
from Models.Matricula.RespostaVer import RespostaVer
from Models.Matricula.RespostaDeletar import RespostaDeletar
from Database.Models.Matricula import Matricula as ModelMatricula


class Matricula(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDMatricula().pegarMatriculas("WHERE id_usuario = %s OR id_disciplina = %s LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdUsuario()),str(pedido_listar.getIdDisciplina()),"%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDMatricula().pegarMatricula("WHERE id = %s ", (str(pedido_ver.getId()),)))

	def Cadastrar(self,pedido_cadastrar):
		matricula = ModelMatricula()
		matricula.setId_usuario(pedido_cadastrar.getId_usuario())
		matricula.setId_disciplina(pedido_cadastrar.getId_disciplina())
		matricula.setStatus(pedido_cadastrar.getStatus())
		return RespostaCadastrar(BDMatricula().inserirMatricula(matricula))

	def Editar(self,pedido_editar):
		matricula = BDMatricula().pegarMatricula("WHERE id = %s ", (pedido_editar.getId()))
		matricula.setId_disciplina(pedido_editar.getId_disciplina())
		matricula.setId_usuario(pedido_editar.getId_usuario())
		matricula.setStatus(pedido_editar.getStatus())
		BDMatricula().alterarMatricula(matricula)
		return RespostaEditar("Matricula Editada com sucesso!")

	def Deletar(self,pedido_deletar):
		matricula = BDMatricula().pegarMatricula("WHERE id = %s ", (pedido_deletar.getId()))		
		BDMatricula().removerMatricula(matricula)
		return RespostaDeletar("Matricula Removida com sucesso!")
