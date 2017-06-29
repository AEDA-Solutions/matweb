from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoListar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoListar, self).__init__(variaveis_do_ambiente)