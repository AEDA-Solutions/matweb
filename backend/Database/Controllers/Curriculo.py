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
		BancoDeDados().executar("INSERT INTO curriculo (mec,credito_periodo_minimo,credito_periodo_maximo,limite_permanencia_minimo,limite_permanencia_maximo,creditos_exigidos,creditos_exigidos_em_tese,creditos_exigidos_tc,creditos_exigidos_ac,creditos_exigidos_dc,id_curso,id_opcao,id_nivel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id", (curriculo.mec,curriculo.credito_periodo_minimo,curriculo.credito_periodo_maximo,curriculo.limite_permanencia_minimo,curriculo.limite_permanencia_maximo,curriculo.creditos_exigidos,curriculo.creditos_exigidos_em_tese,curriculo.creditos_exigidos_tc,curriculo.creditos_exigidos_ac,curriculo.creditos_exigidos_dc,curriculo.id_curso,curriculo.id_opcao,curriculo.id_nivel))
		curriculo.id = BancoDeDados().pegarUltimoIDInserido()
		return curriculo
		
	def removerCurriculo(self, curriculo):
		BancoDeDados().executar("DELETE FROM curriculo WHERE id = %s", (str(curriculo.id)))
		
	def alterarCurriculo(self, curriculo):
		SQL = "UPDATE curriculo SET mec = %s, credito_periodo_minimo = %s, credito_periodo_maximo = %s, limite_permanencia_minimo = %s, limite_permanencia_maximo = %s, creditos_exigidos = %s, creditos_exigidos_em_tese = %s, creditos_exigidos_tc = %s, creditos_exigidos_ac = %s, creditos_exigidos_dc = %s, id_curso = %s, id_opcao = %s, id_nivel = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (curriculo.mec,curriculo.credito_periodo_minimo,curriculo.credito_periodo_maximo,curriculo.limite_permanencia_minimo,curriculo.limite_permanencia_maximo,curriculo.creditos_exigidos,curriculo.creditos_exigidos_em_tese,curriculo.creditos_exigidos_tc,curriculo.creditos_exigidos_ac,curriculo.creditos_exigidos_dc,curriculo.id_curso,curriculo.id_opcao,curriculo.id_nivel))
