from Framework.BancoDeDados import BancoDeDados
from Database.Models.Campus import Campus as ModelCampus


class Campus(object):
		
	def pegarMultiplosCampus(self, condicao, valores):
		campus = []
		for campi in BancoDeDados().consultarMultiplos("SELECT * FROM campus %s" % (condicao), valores):
			campus.append(ModelCampus(campi))
		return campus
	
	def pegarCampus(self, condicao, valores):
		return ModelCampus(BancoDeDados().consultarUnico("SELECT * FROM campus %s" % (condicao), valores))
	
	def inserirCampus(self, campus):
		BancoDeDados().executar("INSERT INTO campus ( nome ) VALUES ( %s ) RETURNING id", (campus.nome,))
		campus.id = BancoDeDados().pegarUltimoIDInserido()
		return campus
		
	def removerCampus(self, campus):
		BancoDeDados().executar("DELETE FROM campus WHERE id = %s", (str(campus.id)))
		
	def alterarCampus(self, campus):
		SQL = "UPDATE campus SET nome = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (campus.nome,campus.id))
