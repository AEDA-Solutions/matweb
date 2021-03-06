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
		BancoDeDados().executar("INSERT INTO matricula (id_disciplina,id_turma,id_usuario,status) VALUES (%s,%s,%s,%s) RETURNING id", (matricula.id_disciplina,matricula.id_turma,matricula.id_usuario,matricula.status))
		matricula.id = BancoDeDados().pegarUltimoIDInserido()
		return matricula
		
	def removerMatricula(self, matricula):
		BancoDeDados().executar("DELETE FROM matricula WHERE id = %s", (str(matricula.id)))
		
	def alterarMatricula(self, matricula):
		SQL = "UPDATE matricula SET id_disciplina = %s, id_turma = %s, id_usuario = %s, status = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (matricula.id_disciplina,matricula.id_turma,matricula.id_usuario,matricula.status,matricula.id))
