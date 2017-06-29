from Framework.BancoDeDados import BancoDeDados
from Database.Models.Grau import Grau as ModelGrau


class Grau(object):
		
	def pegarGraus(self, condicao, valores):
		graus = []
		for grau in BancoDeDados().consultarMultiplos("SELECT * FROM grau %s" % (condicao), valores):
			graus.append(ModelGrau(grau))
		return graus
	
	def pegarGrau(self, condicao, valores):
		return ModelGrau(BancoDeDados().consultarUnico("SELECT * FROM grau %s" % (condicao), valores))
	
	def inserirGrau(self, grau):
		BancoDeDados().executar("INSERT INTO grau (nome) VALUES (%s) RETURNING id", (str(grau.nome),))
		grau.id = BancoDeDados().pegarUltimoIDInserido()
		return grau
		
	def removerGrau(self, grau):
		BancoDeDados().executar("DELETE FROM grau WHERE id = %s", (str(grau.id)))
		
	def alterarGrau(self, grau):
		SQL = "UPDATE grau SET nome = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (grau.nome,grau.id))
