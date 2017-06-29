from Framework.BancoDeDados import BancoDeDados
from Database.Models.Resp_sala import Resp_sala as ModelResp_sala


class Resp_sala(object):
		
	def pegarMultiplosResp_sala(self, condicao, valores):
		resps_sala = []
		for resp_sala in BancoDeDados().consultarMultiplos("SELECT * FROM resp_sala %s" % (condicao), valores):
			resps_sala.append(ModelResp_sala(resp_sala))
		return resps_sala
	
	def pegarResp_sala(self, condicao, valores):
		return ModelResp_sala(BancoDeDados().consultarUnico("SELECT * FROM resp_sala %s" % (condicao), valores))
	
	def inserirResp_sala(self, resp_sala):
		BancoDeDados().executar("INSERT INTO resp_sala ( nome ) VALUES ( %s ) RETURNING id", (resp_sala.nome,))
		resp_sala.id = BancoDeDados().pegarUltimoIDInserido()
		return resp_sala
		
	def removerResp_sala(self, resp_sala):
		BancoDeDados().executar("DELETE FROM resp_sala WHERE id = %s", (str(resp_sala.id)))
		
	def alterarResp_sala(self, resp_sala):
		SQL = "UPDATE resp_sala SET nome = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (resp_sala.nome,resp_sala.id))
