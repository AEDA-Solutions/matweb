from Framework.BancoDeDados import BancoDeDados
from Database.Models.Curriculo import Curriculo as ModelCurriculo


class Curriculo(object):
	
	def pegarCurriculos(self, condicao, valores):
		curriculos = []
		for curriculo in BancoDeDados().consultarMultiplos("SELECT * FROM curriculo %s" % (condicao), valores):
			curriculos.append(ModelCurriculo(curriculo))
		return curriculos
	
	def pegarCurriculo(self, condicao, valores):
		return ModelCurriculo(BancoDeDados().consultarUnico("SELECT * FROM curriculo %s" % (condicao), valores))
	
	def inserirCurriculo(self, curriculo):
		BancoDeDados().executar("INSERT INTO curriculo (id_curso,id_escopo_disciplina,id_disciplina) VALUES (%s,%s,%s) RETURNING id", (curriculo.id_curso,curriculo.id_escopo_disciplina,curriculo.id_disciplina))
		curriculo.id = BancoDeDados().pegarUltimoIDInserido()
		return curriculo
		
	def removerCurriculo(self, curriculo):
		BancoDeDados().executar("DELETE FROM curriculo WHERE id = %s", (str(curriculo.id)))
		
	def alterarCurriculo(self, curriculo):
		SQL = "UPDATE curriculo SET id_curso = %s, id_escopo_disciplina = %s, id_disciplina = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (curriculo.id_curso,curriculo.id_escopo_disciplina,curriculo.id_disciplina,curriculo.id_nivel))
