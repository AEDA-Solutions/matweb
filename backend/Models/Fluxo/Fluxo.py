class Fluxo(object):
	def __init__(self,fluxo):
		self.id_periodo = fluxo.getId_periodo()
		self.id_disciplina = fluxo.getId_disciplina()
		self.nome_disciplina = fluxo.getNome_disciplina()
		self.creditos_disciplina = fluxo.getCreditos_disciplina()