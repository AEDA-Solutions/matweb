from Framework.BancoDeDados import BancoDeDados
from Database.Models.Horario import Horario as ModelHorario


class Horario(object):
		
	def pegarHorarios(self, condicao, valores, inicio=0, quantidade=0):
		horarios = []
		for horario in BancoDeDados().consultarMultiplos("SELECT * FROM horario WHERE %s" % (condicao), valores):
			horarios.append(ModelHorario(horario))
		return horarios
	
	def pegarHorario(self, condicao, valores):
		return ModelHorario(BancoDeDados().consultarUnico("SELECT * FROM horario WHERE %s" % (condicao), valores))
	
	def inserirHorario(self, horario):
		BancoDeDados().executar("INSERT INTO horario (turno,inicio,fim,dia) VALUES (%s,%s,%s,%s) RETURNING id", (horario.turno,horario.inicio,horario.fim,horario.dia))
		horario.id = BancoDeDados().pegarUltimoIDInserido()
		return horario
		
	def removerHorario(self, horario):
		BancoDeDados().executar("DELETE FROM horario WHERE id = %s", (str(horario.id)))
		
	def alterarHorario(self, horario):
		SQL = "UPDATE horario SET turno = %s, inicio = %s, fim = %s, dia = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (horario.turno,horario.inicio,horario.fim,horario.dia,horario.id))
