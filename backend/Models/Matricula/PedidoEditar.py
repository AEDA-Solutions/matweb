from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
		        self.id = self.corpo['id']
			self.nome = self.corpo['nome']
			self.ano = self.corpo['ano']
			self.id_disciplina = self.corpo['id_disciplina']
			self.id_usuario = self.corpo['id_usuario']
			self.periodo = self.corpo['periodo']
		except:
			raise ErroNoHTTP(400)
			

	def getId(self):
		return self.id
	
	
	def getNome(self):
		return self.nome

	
	def getAno(self):
		return self.ano

		
	def getId_disciplina(self):
		return self.id_disciplna
		
		
	def getId_usuario(self):
		return self.id_usuario
		
		
	def getPeriodo(self):
		return self.periodo
