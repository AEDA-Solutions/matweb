from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.id_disciplina = self.corpo['id_disciplina']
			self.id_usuario = self.corpo['id_usuario']
			self.id_turma = self.corpo['id_turma']
			self.status = self.corpo['status']
		except:
			raise ErroNoHTTP(400)
	
	def getId_disciplina(self):
		return self.id_disciplina
	
	def getId_turma(self):
		return self.id_turma
		
	def getId_usuario(self):
		return self.id_usuario
	
	def getStatus(self):
		return self.status
