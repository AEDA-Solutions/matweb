from Framework.BancoDeDados import BancoDeDados
from Database.Models.Escopo_disciplina import Escopo_disciplina as ModelEscopo_disciplina


class Escopo_disciplina(object):
		
	def pegarMultiplosEscopo_disciplina(self, condicao, valores):
		escopo_disciplina = []
		for escopo in BancoDeDados().consultarMultiplos("SELECT * FROM escopo_disciplina %s" % (condicao), valores):
			escopo_disciplina.append(ModelEscopo_disciplina(escopo))
		return escopo_disciplina
	
	def pegarEscopo_disciplina(self, condicao, valores):
		return ModelEscopo_disciplina(BancoDeDados().consultarUnico("SELECT * FROM escopo_disciplina %s" % (condicao), valores))
	
	def inserirEscopo_disciplina(self, escopo_disciplina):
		BancoDeDados().executar("INSERT INTO escopo_disciplina ( nome ) VALUES ( %s ) RETURNING id", (escopo_disciplina.nome,))
		escopo_disciplina.id = BancoDeDados().pegarUltimoIDInserido()
		return escopo_disciplina
		
	def removerEscopo_disciplina(self, escopo_disciplina):
		BancoDeDados().executar("DELETE FROM escopo_disciplina WHERE id = %s", (str(escopo_disciplina.id),))
		
	def alterarEscopo_disciplina(self, escopo_disciplina):
		SQL = "UPDATE escopo_disciplina SET nome = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (escopo_disciplina.nome,escopo_disciplina.id))
