from Framework.BancoDeDados import BancoDeDados
from Database.Models.Oferta import Oferta as ModelOferta


class Oferta(object):
		
	def pegarOfertass(self, condicao, valores):
		ofertas = []
		for oferta in BancoDeDados().consultarMultiplos("SELECT * FROM oferta %s" % (condicao), valores):
			ofertas.append(ModelOferta(oferta))
		return ofertas
	
	def pegarOferta(self, condicao, valores):
		return ModelOferta(BancoDeDados().consultarUnico("SELECT * FROM oferta %s" % (condicao), valores))
	
	def inserirOferta(self, oferta):
		BancoDeDados().executar("INSERT INTO oferta (creditos,id_disciplina,id_ementa) VALUES (%s,%s,%s) RETURNING id", (oferta.creditos,oferta.id_disciplina,oferta.id_ementa))
		oferta.id = BancoDeDados().pegarUltimoIDInserido()
		return oferta
		
	def removerOferta(self, oferta):
		BancoDeDados().executar("DELETE FROM oferta WHERE id = %s", (str(oferta.id),))
		
	def alterarOferta(self, oferta):
		SQL = "UPDATE oferta SET creditos = %s, id_disciplina = %s, id_ementa = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (oferta.creditos,oferta.id_disciplina,oferta.id_ementa,oferta.id))
