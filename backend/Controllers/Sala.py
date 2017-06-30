from Framework.Controller import Controller
from Database.Controllers.Sala import Sala as BDSala
from Models.Sala.RespostaListar import RespostaListar
from Models.Sala.RespostaEditar import RespostaEditar
from Models.Sala.RespostaCadastrar import RespostaCadastrar
from Models.Sala.RespostaVer import RespostaVer
from Models.Sala.RespostaDeletar import RespostaDeletar
from Database.Models.Sala import Sala as ModelSala

class Sala(Controller):

	def Listar(self,pedido_listar):
		return RespostaListar(BDSala().pegarSalas("WHERE id_predio = %s AND codigo LIKE %s LIMIT %s OFFSET %s",(str(pedido_listar.getId_predio()),"%"+(str(pedido_listar.getCodigo())).replace(' ','%')+"%",str(pedido_listar.getQuantidade()),(str(pedido_listar.getQuantidade()*pedido_listar.getPagina())))))

	def Ver(self, pedido_ver):
		return RespostaVer(BDSala().pegarSala("WHERE id = %s ", (str(pedido_ver.getId()),)))

	def Cadastrar(self,pedido_cadastrar):
		sala = ModelSala()
		sala.setCodigo(pedido_cadastrar.getCodigo())
		sala.setId_resp_sala(pedido_cadastrar.getId_resp_sala())
		sala.setId_predio(pedido_cadastrar.getId_predio())
		return RespostaCadastrar(BDSala().inserirSala(sala))

	def Editar(self,pedido_editar):
		sala = BDSala().pegarSala("WHERE id = %s ", (str(pedido_editar.getId()),))
		sala.setCodigo(pedido_editar.getCodigo())
		sala.setId_resp_sala(pedido_editar.getId_resp_sala())
		sala.setId_predio(pedido_editar.getId_predio())
		BDSala().alterarSala(sala)
		return RespostaEditar("Sala Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		sala = BDSala().pegarSala("WHERE id = %s ", (str(pedido_deletar.getId()),))		
		BDSala().removerSala(sala)
		return RespostaDeletar("Sala Removido com sucesso!")  
