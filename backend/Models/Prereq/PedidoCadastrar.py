from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.disciplina = dados ['come']			
			self.grupo = dados ['grupo']
			self.prereq = dados ['prereq']
		except:
			raise ErroNoHTTP(400)
				

	def getGrupo(self):
		return self.grupo		
	
	def getDisciplina(self):
		return self.disciplina
		
	def getPrereq(self):
		return self.prereq
