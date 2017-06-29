class Predio(object):
	def __init__(self,predio):
		self.id = predio.getId()
		self.nome = predio.getNome()
                self.sigla = predio.getSigla()
		self.latitude = predio.getLatitude()
		self.longitude = predio.getLongitude()
		self.id_campus = predio.getId_campus()
