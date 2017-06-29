class Periodo(object):
	def __init__(self,periodo):
		self.id = periodo.getId()
		self.periodo = periodo.getPeriodo()
		self.creditos = periodo.getCreditos()