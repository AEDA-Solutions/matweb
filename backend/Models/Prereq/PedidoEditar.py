from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
						
			self.grupo = dados ['grupo']
			self.id_disc_pre = dados ['id_disc_pre']
		except:
			raise ErroNoHTTP(400)
				

	def getGrupo(self):
		return self.grupo		
	
	
	def getId_disc_pre(self):
		return self.id_disc_pre
		
	def getDisc_pre(self):
		return (Disciplina().pegarDisciplina('id = %s',(self.id_disc_pre,))).getNome()
