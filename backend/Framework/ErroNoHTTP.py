class ErroNoHTTP(BaseException):

	mensagens = {
		400 : "Bad Request",
		401 : "Unauthorized",
		404 : "Not Found",
		405 : "Method Not Allowed",
		411 : "Length Required",
		415 : "Unsupported Media Type",
		500 : "Internal Server Error",
	}

	def __init__(self,codigo,mensagem=None):
		self.codigo = codigo
		if mensagem is not None:
			self.mensagem = mensagem
		else:
			self.mensagem = self.mensagens[self.codigo]

	def getStatus(self):
		return str(self.codigo)+" "+self.mensagens[self.codigo]

	def getCabecalho(self):
		return [('Content-Type', 'application/json; charset=UTF-8'),('Content-Length', str(len(self.getCorpo())))]

	def getCorpo(self):
		return '{ "codigo" : '+str(self.codigo)+' , "mensagem" : "'+self.mensagem+'" }'

	def __str__(self):
		return self.getCorpo()
