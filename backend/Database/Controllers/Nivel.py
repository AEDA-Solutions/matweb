class Nivel(object):
		
	def pegarNiveis(self, condicao, valores):
		nivel = []
		for nivel in BancoDeDados().consultarMultiplos("SELECT * FROM nivel %s" % (condicao), valores):
			nivel.append(ModelNivel(nivel))
		return nivel
	
	def pegarNivel(self, condicao, valores):
		return ModelNivel(BancoDeDados().consultarUnico("SELECT * FROM nivel %s" % (condicao), valores))
	
	def inserirNivel(self, nivel):
		BancoDeDados().executar("INSERT INTO nivel ( nome ) VALUES ( %s ) RETURNING id", (nivel.nome))
		nivel.id = BancoDeDados().pegarUltimoIDInserido()
		return nivel
		
	def removerNivel(self, nivel):
		BancoDeDados().executar("DELETE FROM nivel WHERE id = %s", (str(nivel.id)))
		
	def alterarNivel(self, nivel):
		SQL = "UPDATE nivel SET nome = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (nivel.nome,nivel.id))
