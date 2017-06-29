from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoCadastrar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoCadastrar, self).__init__(variaveis_do_ambiente)
		try:
			self.nome = self.corpo['nome']
			self.matricula = self.corpo['matricula']
			self.cpf = self.corpo['cpf']
			self.perfil = self.corpo['perfil']
			self.email = self.corpo['email']
			self.sexo = self.corpo['sexo']
			self.nome_pai = self.corpo['nome_pai']
			self.nome_mae = self.corpo['nome_mae']
			self.ano_conclusao = self.corpo['ano_conclusao']
			self.identidade = self.corpo['identidade']
			self.senha = self.corpo['senha']
		except:
			raise ErroNoHTTP(400)

	def getNome(self):
		return self.nome

	def getMatricula(self):
		return self.matricula

	def getCpf(self):
		return self.cpf

	def getPerfil(self):
		return self.perfil

	def getSenha(self):
		return self.senha

	def getEmail(self):
		return self.email

	def getSexo(self):
		return self.sexo

	def getNome_pai(self):
		return self.nome_pai		

	def getNome_mae(self):
		return self.nome_mae

	def getAno_conclusao(self):
		return self.ano_conclusao

	def getIdentidade(self):
		return self.identidade
