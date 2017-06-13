from Framework.BancoDeDados import BancoDeDados
from Database.Models.Ementa import Ementa as ModelEmenta


class Ementa(object):
		
	def pegarEmentas(self, condicao, valores):
		ementas = []
		for ementa in BancoDeDados().consultarMultiplos("SELECT * FROM ementa %s" % (condicao), valores):
			ementas.append(ModelEmenta(ementa))
		return ementas
	
	def pegarEmenta(self, condicao, valores):
		return ModelEmenta(BancoDeDados().consultarUnico("SELECT * FROM ementa %s" % (condicao), valores))
	
	def inserirEmenta(self, ementa):
		BancoDeDados().executar("INSERT INTO ementa (arquivo) VALUES (%s) RETURNING id", (ementa.arquivo,))
		ementa.id = BancoDeDados().pegarUltimoIDInserido()
		return ementa
		
	def removerEmenta(self, ementa):
		BancoDeDados().executar("DELETE FROM ementa WHERE id = %s", (str(ementa.id),))
		
	def alterarEmenta(self, ementa):
		SQL = "UPDATE ementa SET arquivo = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (ementa.arquivo,ementa.id))
