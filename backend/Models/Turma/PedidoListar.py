from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
			self.letra = self.corpo['letra']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
			self.id_disciplina = self.corpo['id_disciplina']
		except:
			raise ErroNoHTTP(400)

	def getIdDisciplina(self):
		return self.id_disciplina

	def getNome(self):
		return self.nome

	def getPagina(self):
		return self.pagina

	def getQuantidade(self):
		return self.quantidade
