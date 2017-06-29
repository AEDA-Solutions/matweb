from Database.Controllers.Curso import Curso
from Database.Controllers.Opcao import Opcao
from Database.Controllers.Nivel import Nivel

class Curriculo(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.mec = dados['mec']
			self.credito_periodo_minimo = dados['credito_periodo_minimo']
			self.credito_periodo_maximo = dados['credito_periodo_maximo']
			self.limite_permanencia_minimo = dados['limite_permanencia_minimo']
			self.limite_permanencia_maximo = dados['limite_permanencia_maximo']
			self.creditos_exigidos = dados['creditos_exigidos']
			self.creditos_exigidos_em_tese = dados['creditos_exigidos_em_tese']
			self.creditos_tc = dados['creditos_tc']
			self.creditos_ac = dados['creditos_ac']
			self.creditos_dc = dados['creditos_dc']
			self.id_curso = dados['id_curso']
			self.id_opcao = dados['id_opcao']
			self.id_nivel = dados['id_nivel']
						
				
	def getId(self):
		return self.id
		
	def setMec(self,mec):
		self.mec = mec
	
	def getMec(self):
		return self.mec

	def setCredito_periodo_minimo(self,credito_periodo_minimo):
		self.credito_periodo_minimo = credito_periodo_minimo

	def getCredito_periodo_minimo(self):
		return self.credito_periodo_minimo

	def setCredito_periodo_maximo(self,credito_periodo_maximo):
		self.credito_periodo_maximo = credito_periodo_maximo

	def getCredito_periodo_maximo(self):
		return self.credito_periodo_maximo

	def setLimite_permanencia_minimo(self,limite_permanencia_minimo):
		self.limite_permanencia_minimo = limite_permanencia_minimo
		
	def getLimite_permanencia_minimo(self):
		return self.limite_permanencia_minimo
	
	def setLimite_permanencia_maximo(self,limite_permanencia_maximo):
		self.limite_permanencia_maximo = limite_permanencia_maximo
		
	def getLimite_permanencia_maximo(self):
		return self.limite_permanencia_maximo
		
	def setCreditos_exigidos(self,creditos_exigidos):
		self.creditos_exigidos = creditos_exigidos
	
	def getCreditos_exigidos(self)
		return self.creditos_exigidos
	
	def setCreditos_exigidos_em_tese(self,creditos_exigidos_em_tese):
		self.creditos_exigidos_em_tese = creditos_exigidos_em_tese
	
	def getCreditos_exigidos_em_tese(self)
		return self.creditos_exigidos_em_tese
		
	def setCreditos_exigidos_tc(self,creditos_exigidos_tc):
		self.creditos_exigidos_tc = creditos_exigidos_tc
	
	def getCreditos_exigidos_tc(self)
		return self.creditos_exigidos_tc
		
	def setCreditos_exigidos_ac(self,creditos_exigidos_ac):
		self.creditos_exigidos_ac = creditos_exigidos_ac
	
	def getCreditos_exigidos_ac(self)
		return self.creditos_exigidos_ac
		
	def setCreditos_exigidos_dc(self,creditos_exigidos_dc):
		self.creditos_exigidos_dc = creditos_exigidos_dc
	
	def getCreditos_exigidos_dc(self)
		return self.creditos_exigidos_dc	
			
	def setId_curso(self,curso):
		self.id_curso = (Curso().pegarCurso('nome = %s',(curso))).getId()
		
	def getId_curso(self):
		return self.id_curso
		
	def getCurso(self):
		return (Curso().pegarCurso('id = %s',(self.id_curso))).getNome()
	
	def setId_opcao(self,opcao):
		self.id_opcao = (Opcao().pegarOpcao('nome = %s',(opcao))).getId()
		
	def getId_opcao(self):
		return self.id_opcao
		
	def getOpcao(self):
		return (Opcao().pegarOpcao('id = %s',(self.id_opcao))).getNome()
	
	def setId_nivel(self,nivel):
		self.id_nivel = (Nivel().pegarNivel('nome = %s',(nivel))).getId()
		
	def getId_nivel(self):
		return self.id_nivel
		
	def getNivel(self):
		return (Nivel().pegarNivel('id = %s',(self.id_nivel))).getNome()
