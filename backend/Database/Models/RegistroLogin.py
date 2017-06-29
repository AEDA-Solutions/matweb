class RegistroLogin(object):
	
	def __init__ (self,dados=None):
		if dados is not None:
			self.id = dados['id']
			self.token = dados['token']
			self.id_usuario = dados['id_usuario']
			self.ip = dados['ip']
			self.entrada = dados['entrada']
		
	def getId(self):
		return self.id

	def setToken(self,token):
		self.token = token
		
	def getToken(self):
		return self.token

	def setId_usuario (self,id_usuario):
		self.id_usuario = id_usuario

	def setUsuario(self,usuario):
		self.id_usuario = usuario.getId()

	def getId_usuario (self):
		return self.id_usuario

	def getUsuario(self):
		pass
		
	def getIp (self):
		return self.ip

	def setIp(self,ip):
		self.ip = ip

	def getEntrada(self):
		return self.entrada

	def setEntrada(self, entrada):
		self.entrada = entrada