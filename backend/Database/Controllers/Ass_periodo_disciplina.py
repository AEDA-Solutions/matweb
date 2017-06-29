from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ass_periodo_disciplina import Ass_periodo_disciplina as ModelAss_periodo_disciplina
from Database.Models.Fluxo import Fluxo


class Ass_periodo_disciplina(object):
		
	def pegarAss_periodo_disciplinas(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("SELECT * FROM ass_periodo_disciplina %s" % (condicao), valores):
			associacoes.append(ModelAss_periodo_disciplina(associacao))
		return associacoes
	
	def pegarAss_periodo_disciplina(self, condicao, valores):
		return ModelAss_periodo_disciplina(BancoDeDados().consultarUnico("SELECT * FROM ass_periodo_disciplina %s" % (condicao), valores))
	
	def inserirAss_periodo_disciplina(self, associacao):
		BancoDeDados().executar("INSERT INTO ass_periodo_disciplina (id_disciplina,id_periodo) VALUES (%s,%s) RETURNING id", (associacao.id_disciplina,associacao.id_periodo))
		associacao.id = BancoDeDados().pegarUltimoIDInserido()
		return associacao
		
	def removerAss_periodo_disciplina(self, associacao):
		BancoDeDados().executar("DELETE FROM ass_periodo_disciplina WHERE id = %s", (str(associacao.id),))
		
	def alterarAss_periodo_disciplina(self, associacao):
		SQL = "UPDATE ass_periodo_disciplina SET id_disciplina=%s, id_periodo = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (associacao.id_disciplina,associacao.id_periodo,associacao.id))
		
	def pegarResumoAss(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("select periodo.periodo, periodo.creditos as creditos_periodo, (select nome from disciplina where id=ass_periodo_disciplina.id_disciplina) as nome_disciplina, (select creditos from disciplina where id=ass_periodo_disciplina.id_disciplina) as creditos_disciplina from periodo inner join ass_periodo_disciplina on ass_periodo_disciplina.id_periodo=periodo.id %s" % (codicao),(valores))
			associacoes.append(Fluxo(associacao))
		return associacoes