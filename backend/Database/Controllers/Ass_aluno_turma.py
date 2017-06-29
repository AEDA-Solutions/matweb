from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ass_aluno_turma import Ass_aluno_turma as ModelAss_aluno_turma


class Ass_aluno_turma(object):
		
	def pegarAss_aluno_turmas(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("SELECT * FROM ass_aluno_turma %s" % (condicao), valores):
			associacoes.append(ModelAss_aluno_turma(associacao))
		return associacoes
	
	def pegarAss_aluno_turma(self, condicao, valores):
		return ModelAss_aluno_turma(BancoDeDados().consultarUnico("SELECT * FROM ass_aluno_turma %s" % (condicao), valores))
	
	def inserirAss_aluno_turma(self, associacao):
		BancoDeDados().executar("INSERT INTO ass_aluno_turma (id_turma,id_aluno) VALUES (%s,%s) RETURNING id", (associacao.id_turma,associacao.id_aluno))
		associacao.id = BancoDeDados().pegarUltimoIDInserido()
		return associacao
		
	def removerAss_aluno_turma(self, associacao):
		BancoDeDados().executar("DELETE FROM ass_aluno_turma WHERE id = %s", (str(associacao.id),))
		
	def alterarAss_aluno_turma(self, associacao):
		SQL = "UPDATE ass_aluno_turma SET id_turma=%s, id_aluno = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (associacao.id_turma,associacao.id_aluno,associacao.id))
