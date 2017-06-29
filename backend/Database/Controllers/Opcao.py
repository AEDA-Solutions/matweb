from Framework.BancoDeDados import BancoDeDados
from Database.Models.Opcao import Opcao as ModelOpcao


class Opcao(object):
	
	def pegarOpcoes(self, condicao, valores):
		opcoes = []
		for opcao in BancoDeDados().consultarMultiplos("SELECT * FROM opcao %s" % (condicao), valores):
			opcoes.append(ModelOpcao(opcao))
		return opcoes
	
	def pegarOpcao(self, condicao, valores):
		return ModelOpcao(BancoDeDados().consultarUnico("SELECT * FROM opcao %s" % (condicao), valores))
	
	def inserirOpcao(self, opcao):
		BancoDeDados().executar("INSERT INTO opcao (nome,id_curso) VALUES (%s,%s) RETURNING id", (opcao.nome,opcao.id_curso))
		opcao.id = BancoDeDados().pegarUltimoIDInserido()
		return opcao
		
	def removerOpcao(self, opcao):
		BancoDeDados().executar("DELETE FROM opcao WHERE id = %s", (str(opcao.id)))
		
	def alterarOpcao(self, opcao):
		SQL = "UPDATE opcao SET nome = %s, id_curso = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (opcao.nome,opcao.id_curso,opcao.id))
