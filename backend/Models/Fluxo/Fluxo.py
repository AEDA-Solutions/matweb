class Fluxo(object):
	def __init__(self,fluxo):
		self.periodo = fluxo.getPeriodo()
		self.creditos_periodo = fluxo.getCreditos_periodo()
		self.nome_disciplina = fluxo.getNome_disciplina()
		self.creditos_disciplina = fluxo.getCreditos_disciplina()