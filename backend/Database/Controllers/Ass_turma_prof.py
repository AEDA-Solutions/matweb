from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ass_turma_prof import Ass_turma_prof as ModelAss_turma_prof


class Ass_turma_prof(object):
		
	def pegarAss_turma_profs(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("SELECT * FROM ass_turma_prof %s" % (condicao), valores):
			associacoes.append(ModelAss_turma_prof(associacao))
		return associacoes
	
	def pegarAss_turma_prof(self, condicao, valores):
		return ModelAss_turma_prof(BancoDeDados().consultarUnico("SELECT * FROM ass_turma_prof %s" % (condicao), valores))
	
	def inserirAss_turma_prof(self, associacao):
		BancoDeDados().executar("INSERT INTO ass_turma_prof (id_turma,id_prof) VALUES (%s,%s) RETURNING id", (associacao.id_turma,associacao.id_prof))
		associacao.id = BancoDeDados().pegarUltimoIDInserido()
		return associacao
		
	def removerAss_turma_prof(self, associacao):
		BancoDeDados().executar("DELETE FROM ass_turma_prof WHERE id = %s", (str(associacao.id),))
		
	def alterarAss_turma_prof(self, associacao):
		SQL = "UPDATE ass_turma_prof SET id_turma=%s, id_prof = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (associacao.id_turma,associacao.id_prof,associacao.id))
