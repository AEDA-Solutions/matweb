from Framework.BancoDeDados import BancoDeDados
from Database.Models.Sala import Sala as ModelSala


class Sala(object):
		
	def pegarSalas(self, condicao, valores, inicio=0, quantidade=0):
		salas = []
		for sala in BancoDeDados().consultarMultiplos("SELECT * FROM sala WHERE %s" % (condicao), valores):
			salas.append(ModelSala(sala))
		return salas
	
	def pegarSala(self, condicao, valores):
		return ModelSala(BancoDeDados().consultarUnico("SELECT * FROM sala WHERE %s" % (condicao), valores))
	
	def inserirSala(self, sala):
		BancoDeDados().executar("INSERT INTO sala (resp_sala,codigo,id_predio) VALUES (%s,%s,%s) RETURNING id", (sala.resp_sala,sala.codigo,sala.id_predio))
		sala.id = BancoDeDados().pegarUltimoIDInserido()
		return sala
		
	def removerSala(self, sala):
		BancoDeDados().executar("DELETE FROM sala WHERE id = %s", (str(sala.id)))
		
	def alterarSala(self, sala):
		SQL = "UPDATE sala SET resp_sala = %s, codigo = %s, id_predio = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (sala.resp_sala,sala.codigo,sala.id))