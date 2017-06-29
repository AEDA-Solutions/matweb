from Framework.BancoDeDados import BancoDeDados
from Database.Models.Departamento import Departamento as ModelDepartamento


class Departamento(object):
		
	def pegarDepartamentos(self, condicao, valores):
		departamentos = []
		for departamento in BancoDeDados().consultarMultiplos("SELECT * FROM departamento %s" % (condicao), valores):
			departamentos.append(ModelDepartamento(departamento))
		return departamentos
	
	def pegarDepartamento(self, condicao, valores):
		return ModelDepartamento(BancoDeDados().consultarUnico("SELECT * FROM departamento %s" % (condicao), valores))
	
	def inserirDepartamento(self, departamento):
		BancoDeDados().executar("INSERT INTO departamento (nome,codigo,sigla,id_campus) VALUES (%s,%s,%s,%s) RETURNING id", (departamento.nome,departamento.codigo,departamento.sigla,departamento.id_campus))
		departamento.id = BancoDeDados().pegarUltimoIDInserido()
		return departamento
		
	def removerDepartamento(self, departamento):
		BancoDeDados().executar("DELETE FROM departamento WHERE id = %s", (str(departamento.id),))
		
	def alterarDepartamento(self, departamento):
		SQL = "UPDATE departamento SET nome = %s, codigo = %s, sigla = %s, id_campus = %s WHERE id = %s"
		BancoDeDados().executar(SQL, (departamento.nome,departamento.codigo,departamento.sigla,departamento.id_campus,departamento.id))
