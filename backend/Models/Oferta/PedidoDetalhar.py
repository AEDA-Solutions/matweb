from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoDetalhar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoDetalhar, self).__init__(variaveis_do_ambiente)
		try:
			self.id_disciplina = self.corpo['id_disciplina']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
		except:
			raise ErroNoHTTP(400)

	def getId_disciplina(self):
		return self.id_disciplina

	def getPagina(self):
		return self.pagina

	def getQuantidade(self):
		return self.quantidade
