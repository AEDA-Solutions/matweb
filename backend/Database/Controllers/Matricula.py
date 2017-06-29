from Framework.BancoDeDados import BancoDeDados
from Database.Models.Matricula import Matricula as ModelMatricula

class Matricula(object):
	
	def pegarMatriculas(self, condicao, valores):
		matriculas = []
		for curso in BancoDeDados().consultarMultiplos("SELECT * FROM matricula %s" % (condicao), valores):
			matriculas.append(ModelMatricula(matricula))
		return matriculas
	
	def pegarMatricula(self, condicao, valores):
		return ModelMatricula(BancoDeDados().consultarUnico("SELECT * FROM matricula %s" % (condicao), valores))
	
	def inserirMatricula(self, matricula):
		BancoDeDados().executar("INSERT INTO matricula (nome,id_disciplina,id_usuario,ano,periodo) VALUES (%s,%s,%s,%s,%s) RETURNING id", (matricula.nome,matricula.id_usuario,matricula.id_disciplina,matricula.ano,matricula.periodo))
		matricula.id = BancoDeDados().pegarUltimoIDInserido()
		return matricula
		
	def removerMatricula(self, matricula):
		BancoDeDados().executar("DELETE FROM matricula WHERE id = %s", (str(matricula.id)))
		
	def alterarMatricula(self, matricula):
		SQL = "UPDATE matricula SET nome = %s, id_disciplina = %s, id_usuario = %s, ano = %s, periodo = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (matricula.nome,matricula.id_usuario,matricula.id_disciplina,matricula.ano,matricula.periodo,matricula.id))
