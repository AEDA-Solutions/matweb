class Curso(object):
	def __init__(self,curso):
		self.id = curso.getId()
		self.nome = curso.getNome()
		self.id_campus = curso.getId_campus()
                self.id_grau = curso.getId_grau()
                self.codigo = curso.getCodigo()
                self.permanencia_minima = curso.getPermanencia_minima()
                self.permanencia_maxima = curso.getPermanencia_maxima()
                self.creditos_formatura = curso.getCreditos_formatura()
                self.creditos_optativos_concentracao = curso.getCreditos_optativos_concentracao()
                self.creditos_optativos_conexa = curso.getCreditos_optativos_conexa()
                self.creditos_livres_maximo = curso.getCreditos_livres_maximo()
		self.mec = curso.getMec()

