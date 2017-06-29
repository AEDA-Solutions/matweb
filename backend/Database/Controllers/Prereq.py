from Framework.BancoDeDados import BancoDeDados
from Database.Models.Prereq import Prereq as ModelPrereq


class Prereq(object):
		
	def pegarPrereqs(self, condicao, valores):
		prereqs = []
		for prereq in BancoDeDados().consultarMultiplos("SELECT * FROM prereq %s" % (condicao), valores):
			prereqs.append(ModelPrereq(prereq))
		return prereqs
	
	def pegarPrereq(self, condicao, valores):
		return ModelPrereq(BancoDeDados().consultarUnico("SELECT * FROM prereq %s" % (condicao), valores))
	
	def inserirPrereq(self, prereq):
		BancoDeDados().executar("INSERT INTO prereq (grupo, id_disc_pre ) VALUES (%s,%s) RETURNING id", (prereq.grupo,prereq.id_disc_pre))
		prereq.id = BancoDeDados().pegarUltimoIDInserido()
		return prereq
		
	def removerPrereq(self, prereq):
		BancoDeDados().executar("DELETE FROM prereq WHERE id = %s", (str(prereq.id)))
		
	def alterarPrereq(self, prereq):
		SQL = "UPDATE prereq SET grupo = %s, id_disc_pre = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (prereq.grupo,prereq.id_disc_pre,prereq.id))