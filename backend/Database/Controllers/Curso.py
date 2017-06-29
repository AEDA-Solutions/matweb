from Framework.BancoDeDados import BancoDeDados
from Database.Models.Curso import Curso as ModelCurso


class Curso(object):
	
	def pegarCursos(self, condicao, valores):
		cursos = []
		for curso in BancoDeDados().consultarMultiplos("SELECT * FROM curso %s" % (condicao), valores):
			cursos.append(ModelCurso(curso))
		return cursos
	
	def pegarCurso(self, condicao, valores):
		return ModelCurso(BancoDeDados().consultarUnico("SELECT * FROM curso %s" % (condicao), valores))
	
	def inserirCurso(self, curso):
		BancoDeDados().executar("INSERT INTO curso (nome,codigo,id_campus,id_grau,permanencia_minima,permanencia_maxima,creditos_formatura,creditos_optativos_concentracao,creditos_optativos_conexa,creditos_livres_maximo,mec) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id", (curso.nome,curso.codigo,curso.id_campus,curso.id_grau,curso.permanencia_minima,curso.permanencia_maxima,curso.creditos_formatura,curso.creditos_optativos_concentracao,curso.creditos_optativos_conexa,curso.creditos_livres_maximo, curso.mec))
		curso.id = BancoDeDados().pegarUltimoIDInserido()
		return curso
		
	def removerCurso(self, curso):
		BancoDeDados().executar("DELETE FROM curso WHERE id = %s", (str(curso.id)))
		
	def alterarCurso(self, curso):
		SQL = "UPDATE curso SET nome = %s, codigo = %s, id_grau = %s, id_campus = %s, permanencia_minima = %s, permanencia_maxima = %s, creditos_formatura = %s, creditos_optativos_concentracao = %s, creditos_optativos_conexa = %s, creditos_livres_maximo = %s, mec = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (curso.nome,curso.codigo,curso.id_campus,curso.id_grau,curso.permanencia_minima,curso.permanencia_maxima,curso.creditos_formatura,curso.creditos_optativos_concentracao,curso.creditos_optativos_conexa,curso.creditos_livres_maximo,curso.mec,curso.id))
