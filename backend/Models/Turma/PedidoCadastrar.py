from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:    
	
			self.letra = self.corpo['letra']
			self.id_disciplina = self.corpo['id_dsciplina']
		except:
			raise ErroNoHTTP(400)

	def getLetra(self):
		return self.letra


	def getId_disciplina(self):
		return self.id_disciplina
