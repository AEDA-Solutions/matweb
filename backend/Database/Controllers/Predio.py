from Framework.BancoDeDados import BancoDeDados
from Database.Models.Predio import Predio as ModelPredio


class Predio(object):
		
	def pegarPredios(self, condicao, valores):
		predios = []
		for predio in BancoDeDados().consultarMultiplos("SELECT * FROM predio %s" % (condicao), valores):
			predios.append(ModelPredio(predio))
		return predios
	
	def pegarPredio(self, condicao, valores):
		return ModelPredio(BancoDeDados().consultarUnico("SELECT * FROM predio %s" % (condicao), valores))
	
	def inserirPredio(self, predio):
		BancoDeDados().executar("INSERT INTO predio (nome, sigla, latitude, longitude, id_campus) VALUES (%s,%s,%s,%s,%s) RETURNING id", (predio.nome,predio.sigla,predio.latitude,predio.longitude,predio.id_campus))
		predio.id = BancoDeDados().pegarUltimoIDInserido()
		return predio
		
	def removerPredio(self, predio):
		BancoDeDados().executar("DELETE FROM predio WHERE id = %s", (str(predio.id)))
		
	def alterarPredio(self, predio):
		SQL = "UPDATE predio SET nome = %s, sigla = %s, latitude = %s, longitude = %s, id_campus = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (predio.nome,predio.sigla,predio.latitude,predio.longitude,predio.id_campus,predio.id))
