from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
			self.id_disc_pre = self.corpo['id_disc_pre']
			self.grupo = self.corpo['grupo']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
		except:
			raise ErroNoHTTP(400)

	def getIdDisc_pre(self):
		return self.id_disc_pre

	def getGrupo(self):
		return self.Grupo

	def getPagina(self):
		return self.pagina

	def getQuantidade(self):
		return self.quantidade
