from Framework.Controller import Controller
from Database.Controllers.Sala import Sala as BDSala
from Models.Sala.RespostaListar import RespostaListar

class Sala(Controller):

      def Listar(self,pedido_listar):
            return RespostaListar(BDSala().pegarSalas("WHERE id_predio = %s AND codigo LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdPredio(),"%".pedido_listar.getCodigo().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))

      def Ver(self, pedido_ver):
		return RespostaVer(BDSala().pegarSala("WHERE id = %s ", (pedido_ver.getId())))

	def Cadastrar(self,pedido_cadastrar):
		sala = ModelSala()
		sala.setCodigo(pedido_cadastrar.getCodigo())
		return RespostaCadastrar(BDSala().inserirSala(sala))

	def Editar(self,pedido_editar):
		sala = BDSala().pegarSala("WHERE id = %s ", (pedido_editar.getId()))
		sala.setCodigo(pedido_editar.getCodigo())
		BDSala().alterarSala(sala)
		return RespostaEditar("Sala Editado com sucesso!")

	def Deletar(self,pedido_deletar):
		sala = BDSala().pegarSala("WHERE id = %s ", (pedido_deletar.getId()))		
		BDSala().removerSala(sala)
		return RespostaDeletar("Sala Removido com sucesso!")  
