class Usuario(object):

	def __init__(self,usuario):
		self.id = usuario.getId()
		self.nome = usuario.getNome()
		self.matricula = usuario.getMatricula()
#		self.identidade = usuario.getIdentidade()
		self.cpf = usuario.getCpf()
		self.perfil = usuario.getPerfil()
		self.senha = usuario.getSenha(
		self.email = usuario.getEmail()
		self.sexo = usuario.getSexo()
		self.nome_pai = usuario.getNome_pai()
		self.nome_mae = usuario.getNome_mae()
#		self.id_raca_cor = usuario.getId_raca_cor()
#		self.id_nivel = usuario.getId_nivel()
		self.ano_conclusao = usuario.getAno_conclusao()
#		self.cep = usuario.getCep()
#		self.numero_lote = usuario.getNumero_lote()
#		self.complemento = usuario.getComplemento()
#		self.numero_telefone = usuario.getNumero_telefone()
#		self.tipo_escola = usuario.getTipo_escola()