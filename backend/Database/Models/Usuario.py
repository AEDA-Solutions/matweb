class Usuario(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados['id']
			self.nome = dados['nome']
			self.matricula = dados['matricula']
			self.cpf = dados['cpf']
			self.perfil = dados['perfil']
			self.email = dados['email']
			self.sexo = dados['sexo']
			self.nome_pai = dados['nome_pai']
			self.nome_mae = dados['nome_mae']
			self.ano_conclusao = dados['ano_conclusao']
			self.identidade = dados['identidade']
			self.senha = dados['senha']

	def getId(self):
		return self.id

	def setCpf(self,cpf):
		self.cpf = cpf
		
	def getCpf(self):
		return self.cpf

	def setMatricula(self,matricula):
		self.matricula = matricula
		
	def getMatricula(self):
		return self.matricula

	def setPerfil (self,perfil):
		self.perfil = perfil
		
	def getPerfil (self):
		return self.perfil

	def setNome(self,nome):
		self.nome = nome

	def getNome(self):
		return self.nome

	def getSenhaHashed(self):
		return self.senha

	def setSenhaHashed(self,senha):
		self.senha = senha

	def getEmail(self):
		return self.email
	
	def setEmail(self,email):
		self.email = email

	def getSexo(self):
		return self.sexo

	def setSexo(self,sexo):
		self.sexo = sexo

	def getNome_pai(self):
		return self.nome_pai

	def setNome_pai(self,nome_pai):
		self.nome_pai = nome_pai

	def getNome_mae(self):
		return self.nome_mae

	def setNome_mae(self,nome_mae):
		self.nome_mae = nome_mae

	def getAno_conclusao(self):
		return self.ano_conclusao

	def setAno_conclusao(self,ano_conclusao):
		self.ano_conclusao = ano_conclusao

	def setIdentidade(self,identidade):
		self.identidade = identidade
		
	def getIdentidade(self):
		return self.identidade
