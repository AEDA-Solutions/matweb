from Framework.BancoDeDados import BancoDeDados
from Database.Models.Fluxo import Fluxo as ModelFluxo


class Fluxo(object):
	
	def pegarFluxo(self, condicao, valores):
		fluxos = []
		for fluxo in BancoDeDados().consultarMultiplos("SELECT * FROM fluxo %s" % (condicao), valores):
			fluxos.append(ModelFluxo(fluxo))
		return fluxos
	
	def pegarFluxo(self, condicao, valores):
		return ModelFluxo(BancoDeDados().consultarUnico("SELECT * FROM fluxo %s" % (condicao), valores))
	
	def inserirFluxo(self, fluxo):
		BancoDeDados().executar("INSERT INTO fluxo (periodo_inicio, periodo_fim, id_curso, id_opcao) VALUES (%s,%s,%s,%s) RETURNING id", (fluxo.periodo_inicio,fluxo.periodo_fim,fluxo.id_curso,fluxo.id_opcao))
		fluxo.id = BancoDeDados().pegarUltimoIDInserido()
		return fluxo
		
	def removerFluxo(self, fluxo):
		BancoDeDados().executar("DELETE FROM fluxo WHERE id = %s", (str(fluxo.id)))
		
	def alterarFluxo(self, fluxo):
		SQL = "UPDATE fluxo SET periodo_inicio = %s, periodo_fim = %s, id_curso = %s, id_opcao = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (fluxo.periodo_inicio,fluxo.periodo_fim,fluxo.id_curso,fluxo.id_opcao))
