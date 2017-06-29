from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)
		try:
		        self.nome = self.corpo['nome']
	       	        self.id_usuario = self.corpo['id_usuario']
			self.id_disciplina = self.corpo['id_disciplina']
			self.pagina = self.corpo['pagina']
			self.quantidade = self.corpo['quantidade']
		except:
			raise ErroNoHTTP(400)
        
	
	def getNome(self):
		return self.nome
		
		
	def getIdUsuario(self):
		return self.id_usuario
	
	
	def getIdDisciplina(self):
	        return self.id_disciplina

	
	def getPagina(self):
	        return self.pagina
	
	
        def getQuantidade(self):
	        return self.quantidade
