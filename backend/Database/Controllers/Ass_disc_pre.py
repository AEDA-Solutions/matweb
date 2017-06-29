from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ass_disc_pre import Ass_disc_pre as ModelAss_disc_pre


class Ass_disc_pre(object):
		
	def pegarAss_disc_pres(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("SELECT * FROM ass_disc_pre %s" % (condicao), valores):
			associacoes.append(ModelAss_disc_pre(associacao))
		return associacoes
	
	def pegarAss_disc_pre(self, condicao, valores):
		return ModelAss_disc_pre(BancoDeDados().consultarUnico("SELECT * FROM ass_disc_pre %s" % (condicao), valores))
	
	def inserirAss_disc_pre(self, associacao):
		BancoDeDados().executar("INSERT INTO ass_disc_pre (id_disciplina,id_prereq) VALUES (%s,%s) RETURNING id", (associacao.id_disciplina,associacao.id_prereq))
		associacao.id = BancoDeDados().pegarUltimoIDInserido()
		return associacao
		
	def removerAss_disc_pre(self, associacao):
		BancoDeDados().executar("DELETE FROM ass_disc_pre WHERE id = %s", (str(associacao.id),))
		
	def alterarAss_disc_pre(self, associacao):
		SQL = "UPDATE ass_disc_pre SET id_disciplina=%s, id_prereq = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (associacao.id_disciplina,associacao.id_prereq,associacao.id))
