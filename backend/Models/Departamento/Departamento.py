class Departamento(object):
	def __init__(self,departamento):
		self.id = departamento.getId()
		self.nome = departamento.getNome()
		self.id_campus = departamento.getId_campus()
		self.codigo = departamento.getCodigo()
		self.sigla = departamento.getSigla()
