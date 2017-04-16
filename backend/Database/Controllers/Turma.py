from Framework.BancoDeDados import BancoDeDados
from Database.Models.Turma import Turma as ModelTurma


class Turma(object):
		
	def pegarTurmas(self, condicao, valores):
		turmas = []
		for turma in BancoDeDados().consultarMultiplos("SELECT * FROM turma %s" % (condicao), valores):
			turmas.append(ModelTurma(turma))
		return turmas
	
	def pegarTurma(self, condicao, valores):
		return ModelTurma(BancoDeDados().consultarUnico("SELECT * FROM turma %s" % (condicao), valores))
	
	def inserirTurma(self, turma):
		BancoDeDados().executar("INSERT INTO turma (letra, id_disciplina ) VALUES (%s,%s) RETURNING id", (turma.letra,turma.id_disciplina))
		turma.id = BancoDeDados().pegarUltimoIDInserido()
		return turma
		
	def removerTurma(self, turma):
		BancoDeDados().executar("DELETE FROM turma WHERE id = %s", (str(turma.id)))
		
	def alterarTurma(self, turma):
		SQL = "UPDATE turma SET letra = %s, id_disciplina = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (turma.letra,turma.id_disciplina,turma.id))
