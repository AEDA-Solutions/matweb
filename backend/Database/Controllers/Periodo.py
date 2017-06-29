from Framework.BancoDeDados import BancoDeDados
from Database.Models.Periodo import Periodo as ModelPeriodo


class Periodo(object):
	
	def pegarPeriodos(self, condicao, valores):
		periodos = []
		for periodo in BancoDeDados().consultarMultiplos("SELECT * FROM periodo %s" % (condicao), valores):
			periodos.append(ModelPeriodo(periodo))
		return periodos
	
	def pegarPeriodo(self, condicao, valores):
		return ModelPeriodo(BancoDeDados().consultarUnico("SELECT * FROM periodo %s" % (condicao), valores))
	
	def inserirPeriodo(self, periodo):
		BancoDeDados().executar("INSERT INTO periodo (id_curso,periodo,creditos) VALUES (%s,%s,%s) RETURNING id", (periodo.id_curso,periodo.periodo,periodo.creditos))
		periodo.id = BancoDeDados().pegarUltimoIDInserido()
		return periodo
		
	def removerPeriodo(self, periodo):
		BancoDeDados().executar("DELETE FROM periodo WHERE id = %s", (str(periodo.id),))
		
	def alterarPeriodo(self, periodo):
		SQL = "UPDATE periodo SET id_curso = %s, periodo = %s, creditos = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (periodo.id_curso,periodo.periodo,periodo.creditos,periodo.id))
