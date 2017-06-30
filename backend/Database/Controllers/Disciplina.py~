from Framework.BancoDeDados import BancoDeDados
from Database.Models.Disciplina import Disciplina as ModelDisciplina


class Disciplina(object):
	
	def pegarDisciplinas(self, condicao, valores):
		disciplinas = []
		for disciplina in BancoDeDados().consultarMultiplos("SELECT * FROM disciplina %s" % (condicao), valores):
			disciplinas.append(ModelDisciplina(disciplina))
		return disciplinas
	
	def pegarDisciplina(self, condicao, valores):
		return ModelDisciplina(BancoDeDados().consultarUnico("SELECT * FROM disciplina %s" % (condicao), valores))
	
	def inserirDisciplina(self, disciplina):
		BancoDeDados().executar("INSERT INTO disciplina (nome,codigo,id_departamento) VALUES (%s,%s,%s) RETURNING id", (disciplina.nome,disciplina.codigo,disciplina.id_departamento))
		disciplina.id = BancoDeDados().pegarUltimoIDInserido()
		return disciplina
		
	def removerDisciplina(self, disciplina):
		BancoDeDados().executar("DELETE FROM disciplina WHERE id = %s", (str(disciplina.id),))
		
	def alterarDisciplina(self, disciplina):
		SQL = "UPDATE disciplina SET nome = %s, codigo = %s, id_departamento = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (disciplina.nome,disciplina.codigo,disciplina.id_departamento,disciplina.id))
