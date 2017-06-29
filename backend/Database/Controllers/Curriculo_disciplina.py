from Framework.BancoDeDados import BancoDeDados
from Database.Models.Curriculo_disciplina import Curriculo_disciplina as ModelCurriculo_disciplina


class Curriculo_disciplina(object):
	
	def pegarCurriculo_disciplina(self, condicao, valores):
		curriculo_disciplinas = []
		for curriculo_disciplina in BancoDeDados().consultarMultiplos("SELECT * FROM curriculo_disciplina %s" % (condicao), valores):
			curriculo_disciplinas.append(ModelCurriculo_disciplina(curriculo_disciplina))
		return curriculo_disciplinas
	
	def pegarCurriculo_disciplina(self, condicao, valores):
		return ModelCurriculo_disciplina(BancoDeDados().consultarUnico("SELECT * FROM curriculo_disciplina %s" % (condicao), valores))
	
	def inserirCurriculo_disciplina(self, curriculo_disciplina):
		BancoDeDados().executar("INSERT INTO curriculo_disciplina (obrigatorio,ciclo,grupo,id_disciplina,id_curriculo) VALUES (%s,%s,%s,%s,%s) RETURNING id", (curriculo_disciplina.obrigatorio,curriculo_disciplina.ciclo,curriculo_disciplina.grupo,curriculo_disciplina.id_disciplina,curriculo_disciplina.id_curriculo))
		curriculo_disciplina.id = BancoDeDados().pegarUltimoIDInserido()
		return curriculo_disciplina
		
	def removerCurriculo_disciplina(self, curriculo_disciplina):
		BancoDeDados().executar("DELETE FROM curriculo_disciplina WHERE id = %s", (str(curriculo_disciplina.id)))
		
	def alterarCurriculo_disciplina(self, curriculo_disciplina):
		SQL = "UPDATE curriculo_disciplina SET obrigatorio = %s, ciclo = %s, grupo = %s, id_disciplina = %s, id_curriculo = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (curriculo_disciplina.obrigatorio,curriculo_disciplina.ciclo,curriculo_disciplina.grupo,curriculo_disciplina.id_disciplina,curriculo_disciplina.id_curriculo))
