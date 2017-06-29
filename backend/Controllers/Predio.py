from Framework.Controller import Controller
from Database.Controllers.Predio import Predio as BDPredio
from Models.Predio.RespostaListar import RespostaListar
from Models.Predio.RespostaCadastrar import RespostaCadastrar
from Models.Predio.RespostaEditar import RespostaEditar
from Models.Predio.RespostaVer import RespostaVer
from Models.Predio.RespostaDeletar import RespostaDeletar
from Database.Models.Predio import Predio as ModelPredio

class Predio(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDPredio().pegarPredios("WHERE id_campus = %s AND nome LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdCampus(),"%"+pedido_listar.getNome().replace(' ','%')+"%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))

	def Ver(self, pedido_ver):     
		return RespostaVer(BDPredio().pegarPredio("WHERE id = %s ", (str(pedido_ver.getId()),)))

	def Cadastrar(self,pedido_cadastrar):
		predio = ModelPredio()
		predio.setNome(pedido_cadastrar.getNome())
		predio.setSigla(pedido_cadastrar.getSigla())
		predio.setLatitude(pedido_cadastrar.getLatitude())
		predio.setLongitude(pedido_cadastrar.getLongitude())
		predio.setId_campus(pedido_cadastrar.getId_campus())
		return RespostaCadastrar(BDPredio().inserirPredio(predio))

	def Editar(self,pedido_editar):
		predio = BDPredio().pegarPredio("WHERE id = %s ", (str(pedido_editar.getId()),))
		predio.setNome(pedido_editar.getNome())
		predio.setSigla(pedido_editar.getSigla())
		predio.setLatitude(pedido_editar.getLatitude())
		predio.setLongitude(pedido_editar.getLongitude())
		BDPredio().alterarPredio(predio)
		return RespostaEditar("Predio Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		predio = BDPredio().pegarPredio("WHERE id = %s ", (str(pedido_deletar.getId()),))		
		BDPredio().removerPredio(predio)
		return RespostaDeletar("Predio Removido com sucesso!")
