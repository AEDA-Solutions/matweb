from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ass_turma_sala_horario import Ass_turma_sala_horario as ModelAss_turma_sala_horario


class Ass_turma_sala_horario(object):
		
	def pegarAss_turma_sala_horarios(self, condicao, valores):
		associacoes = []
		for associacao in BancoDeDados().consultarMultiplos("SELECT * FROM ass_turma_sala_horario %s" % (condicao), valores):
			associacoes.append(ModelAss_turma_sala_horario(associacao))
		return associacoes
	
	def pegarAss_turma_sala_horario(self, condicao, valores):
		return ModelAss_turma_sala_horario(BancoDeDados().consultarUnico("SELECT * FROM ass_turma_sala_horario %s" % (condicao), valores))
	
	def inserirAss_turma_sala_horario(self, associacao):
		BancoDeDados().executar("INSERT INTO ass_turma_sala_horario (id_turma,id_sala,id_horario) VALUES (%s,%s,%s) RETURNING id", (associacao.id_turma,associacao.id_sala,associacao.id_horario))
		associacao.id = BancoDeDados().pegarUltimoIDInserido()
		return associacao
		
	def removerAss_turma_sala_horario(self, associacao):
		BancoDeDados().executar("DELETE FROM ass_turma_sala_horario WHERE id = %s", (str(associacao.id),))
		
	def alterarAss_turma_sala_horario(self, associacao):
		SQL = "UPDATE ass_turma_sala_horario SET id_turma=%s, id_sala = %s, id_horario = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (associacao.id_turma,associacao.id_sala,associacao.id_horario,associacao.id))
