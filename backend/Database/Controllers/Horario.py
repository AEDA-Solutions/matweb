from Framework.BancoDeDados import BancoDeDados
from Database.Models.Horario import Horario as ModelHorario


class Horario(object):
		
	def pegarHorarios(self, condicao, valores):
		horarios = []
		for horario in BancoDeDados().consultarMultiplos("SELECT * FROM horario %s" % (condicao), valores):
			horarios.append(ModelHorario(horario))
		return horarios
	
	def pegarHorario(self, condicao, valores):
		return ModelHorario(BancoDeDados().consultarUnico("SELECT * FROM horario %s" % (condicao), valores))
	
	def inserirHorario(self, horario):
		BancoDeDados().executar("INSERT INTO horario (inicio,fim,dia) VALUES (%s,%s,%s) RETURNING id", (horario.inicio,horario.fim,horario.dia))
		horario.id = BancoDeDados().pegarUltimoIDInserido()
		return horario
		
	def removerHorario(self, horario):
		BancoDeDados().executar("DELETE FROM horario WHERE id = %s", (str(horario.id)))
		
	def alterarHorario(self, horario):
		SQL = "UPDATE horario SET inicio = %s, fim = %s, dia = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (horario.inicio,horario.fim,horario.dia,horario.id))
