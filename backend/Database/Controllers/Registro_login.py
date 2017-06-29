from Framework.BancoDeDados import BancoDeDados
from Database.Models.Registro import Registro_login as ModelRegistro


class Registro_login(object):
		
	def pegarRegistro(self, condicao, valores):
		registro = []
		for registro in BancoDeDados().consultarMultiplos("SELECT * FROM registro_login %s" % (condicao), valores):
			registro.append(ModelRegistro(registro))
		return registro
	
	def pegarRegistro(self, condicao, valores):
		return ModelRegistro(BancoDeDados().consultarUnico("SELECT * FROM registro_login %s" % (condicao), valores))
	
	def inserirRegistro(self, registro):
		BancoDeDados().executar("INSERT INTO registro_login (id, token, id_usuario, ip, entrada) VALUES (%s,%s,%s,%s,%s) RETURNING id", (registro.id, registro.token, registro.id_usuario, registro.ip, registro.entrada))
		registro.id = BancoDeDados().pegarUltimoIDInserido()
		return registro
		
	def removerRegistro(self, registro):
		BancoDeDados().executar("DELETE FROM registro_login WHERE id = %s", (str(registro.id)))
		
	def alterarRegistro(self, registro):
		SQL = "UPDATE registro_login SET token = %s, id_usuario = %s, ip = %s, entrada = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (registro.token, registro.id_usuario, registro.ip, registro.entrada, registro.id))
