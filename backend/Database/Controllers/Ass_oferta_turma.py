from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ass_oferta_turma import Ass_oferta_turma as ModelAss_oferta_turma


class Ass_oferta_turma(object):
		
	def pegarAss_oferta_turmas(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("SELECT * FROM ass_oferta_turma %s" % (condicao), valores):
			associacoes.append(ModelAss_oferta_turma(associacao))
		return associacoes
	
	def pegarAss_oferta_turma(self, condicao, valores):
		return ModelAss_oferta_turma(BancoDeDados().consultarUnico("SELECT * FROM ass_oferta_turma %s" % (condicao), valores))
	
	def inserirAss_oferta_turma(self, associacao):
		BancoDeDados().executar("INSERT INTO ass_oferta_turma (id_turma,id_oferta) VALUES (%s,%s) RETURNING id", (associacao.id_turma,associacao.id_oferta))
		associacao.id = BancoDeDados().pegarUltimoIDInserido()
		return associacao
		
	def removerAss_oferta_turma(self, associacao):
		BancoDeDados().executar("DELETE FROM ass_oferta_turma WHERE id = %s", (str(associacao.id),))
		
	def alterarAss_oferta_turma(self, associacao):
		SQL = "UPDATE ass_oferta_turma SET id_turma=%s, id_oferta = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (associacao.id_turma,associacao.id_oferta,associacao.id))
