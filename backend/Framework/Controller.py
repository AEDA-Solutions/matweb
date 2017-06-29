import importlib

class Controller(object):

	def getPedido(self,funcao,variaveis_do_ambiente):
			modulo_do_pedido = importlib.import_module("Models.{}.Pedido{}".format(funcao['modulo'],funcao['metodo']))
			return getattr(modulo_do_pedido, "Pedido{}".format(funcao['metodo']))(variaveis_do_ambiente)

	def executar(self,funcao,variaveis_do_ambiente):
		if hasattr(self, funcao['metodo']) and callable(getattr(self, funcao['metodo'])):
			return getattr(self, funcao['metodo'])(self.getPedido(funcao,variaveis_do_ambiente))
		else:
			raise ErroNoHTTP(404)