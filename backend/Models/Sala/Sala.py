class Sala(object): 
	def __init__(self,sala):
		self.id = sala.getId()
		self.codigo = sala.getCodigo()
                self.id_resp_sala = sala.getId_resp_sala()
		self.id_predio = sala.getId_predio()
