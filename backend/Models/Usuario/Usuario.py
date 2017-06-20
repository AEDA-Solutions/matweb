class Usuario(object):

	def __init__(self,usuario):
		self.id = usuario.getId()
		self.nome = usuario.getNome()
		self.matricula = usuario.getMatricula()
		self.cpf = usuario.getCpf()
		self.perfil = usuario.getPerfil()
		self.email = usuario.getEmail()
		self.sexo = usuario.getSexo()
		self.nome_pai = usuario.getNome_pai()
		self.nome_mae = usuario.getNome_mae()
		self.ano_conclusao = usuario.getAno_conclusao()
		self.identidade = usuario.getIdentidade()