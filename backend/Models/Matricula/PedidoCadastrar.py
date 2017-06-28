from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.ano = self.corpo['ano']
			self.nome = self.corpo['nome']
			self.periodo = self.corpo['periodo']
			self.id_disciplina = self.corpo['id_disciplina']
			self.id_usuario = self.corpo['id_usuario']
		except:
			raise ErroNoHTTP(400)
	
	def getNome(self):
		return self.nome
	
	def getAno(self):
		return self.ano
		
	def getId_disciplina(self):
		return self.id_disciplina
		
	def getId_usuario(self):
		return self.id_usuario
	
	def getPeriodo(self):
                return self.periodo
