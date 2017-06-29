from Framework.BancoDeDados import BancoDeDados
from Database.Models.Sala import Sala as ModelSala


class Sala(object):
		
	def pegarSalas(self, condicao, valores):
		salas = []
		for sala in BancoDeDados().consultarMultiplos("SELECT * FROM sala %s" % (condicao), valores):
			salas.append(ModelSala(sala))
		return salas
	
	def pegarSala(self, condicao, valores):
		return ModelSala(BancoDeDados().consultarUnico("SELECT * FROM sala %s" % (condicao), valores))
	
	def inserirSala(self, sala):
		BancoDeDados().executar("INSERT INTO sala (id_resp_sala,codigo,id_predio) VALUES (%s,%s,%s) RETURNING id", (sala.id_resp_sala,sala.codigo,sala.id_predio))
		sala.id = BancoDeDados().pegarUltimoIDInserido()
		return sala
		
	def removerSala(self, sala):
		BancoDeDados().executar("DELETE FROM sala WHERE id = %s", (str(sala.id),))
		
	def alterarSala(self, sala):
		SQL = "UPDATE sala SET id_resp_sala = %s, codigo = %s, id_predio = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (sala.id_resp_sala,sala.codigo,sala.id_predio,sala.id))
