from Framework.Controller import Controller
from Database.Controllers.Curso import Curso as BDCurso
from Models.Curso.RespostaListar import RespostaListar
from Models.Curso.RespostaCadastrar import RespostaCadastrar
from Models.Curso.RespostaEditar import RespostaEditar
from Models.Curso.RespostaVer import RespostaVer
from Models.Curso.RespostaDeletar import RespostaDeletar
from Database.Models.Curso import Curso as ModelCurso


class Curso(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDCurso().pegarCursos("WHERE id_campus = %s AND id_grau = %s AND nome LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getIdCampus()),str(pedido_listar.getIdGrau()),"%"+pedido_listar.getNome().replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDCurso().pegarCurso("WHERE id = %s ", (str(pedido_ver.getId()),)))

	def Cadastrar(self,pedido_cadastrar):
		curso = ModelCurso()
		curso.setNome(pedido_cadastrar.getNome())
		curso.setCodigo(pedido_cadastrar.getCodigo())
		curso.setId_grau(pedido_cadastrar.getId_grau())
		curso.setId_campus(pedido_cadastrar.getId_campus())
		curso.setPermanencia_minima(pedido_cadastrar.getPermanencia_minima())
		curso.setPermanencia_maxima(pedido_cadastrar.getPermanencia_maxima())
		curso.setCreditos_formatura(pedido_cadastrar.getCreditos_formatura())
		curso.setCreditos_optativos_concentracao(pedido_cadastrar.getCreditos_optativos_concentracao())
		curso.setCreditos_optativos_conexa(pedido_cadastrar.getCreditos_optativos_conexa())
		curso.setCreditos_livres_maximo(pedido_cadastrar.getCreditos_livres_maximo())
		curso.setMec(pedido_cadastrar.getMec())
		return RespostaCadastrar(BDCurso().inserirCurso(curso))

	def Editar(self,pedido_editar):
		curso = BDCurso().pegarCurso("WHERE id = %s ", (pedido_editar.getId()))
		curso.setNome(pedido_editar.getNome())
		curso.setCodigo(pedido_editar.getCodigo())
		curso.setId_grau(pedido_editar.getId_grau())
		curso.setId_campus(pedido_editar.getId_campus())
		curso.setPermanencia_minima(pedido_editar.getPermanencia_minima())
		curso.setPermanencia_maxima(pedido_editar.getPermanencia_maxima())
		curso.setCreditos_formatura(pedido_editar.getCreditos_formatura())
		curso.setCreditos_optativos_concentracao(pedido_editar.getCreditos_optativos_concentracao())
		curso.setCreditos_optativos_conexa(pedido_editar.getCreditos_optativos_conexa())
		curso.setCreditos_livres_maximo(pedido_editar.getCreditos_livres_maximo())
		curso.setMec(pedido_editar.getMec())
		BDCurso().alterarCurso(curso)
		return RespostaEditar("Curso Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		curso = BDCurso().pegarCurso("WHERE id = %s ", (pedido_deletar.getId()))		
		BDCurso().removerCurso(curso)
		return RespostaDeletar("Curso Removido com sucesso!")
