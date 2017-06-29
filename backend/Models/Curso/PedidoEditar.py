from Framework.Pedido import Pedido
from Framework.ErroNoHTTP import ErroNoHTTP

class PedidoEditar(Pedido):

	def __init__(self,variaveis_do_ambiente):
		super(PedidoEditar, self).__init__(variaveis_do_ambiente)
		try:
		        self.id = self.corpo['id']
			self.nome = self.corpo['nome']
			self.codigo = self.corpo['codigo']
			self.id_grau = self.corpo['id_grau']
			self.id_campus = self.corpo['id_campus']
			self.permanencia_minima = self.corpo['permanencia_minima']
			self.permanencia_maxima = self.corpo['permanencia_maxima']
			self.creditos_formatura = self.corpo['creditos_formatura']
			self.creditos_optativos_conexa = self.corpo['creditos_optativos_conexa']
			self.creditos_optativos_concentracao = self.corpo['creditos_optativos_concentracao']
			self.creditos_livres_maximo = self.corpo['creditos_livres_maximo']
			self.mec = self.corpo['mec']
		except:
			raise ErroNoHTTP(400)
			

	def getId(self):
		return self.id
	
	
	def getNome(self):
		return self.nome

	
	def getCodigo(self):
		return self.codigo

		
	def getId_grau(self):
		return self.id_grau
		
		
	def getId_campus(self):
		return self.id_campus
		
		
	def getPermanencia_minima(self):
		return self.permanencia_minima
	
	
	def getPermanencia_maxima(self):
	        return self.permanencia_maxima
	
	
	def getCreditos_formatura(self):
		return self.creditos_formatura
	
	
	def getCreditos_optativos_conexa(self)
	        return self.creditos_optativos_conexa
	
	
        def getCreditos_optativos_concentracao(self)
	        return self.creditos_optativos_concentracao
	
	
	def getCreditos_livres_maximo(self)
	        return self.creditos_livres_maximo
	
	
	def getMec(self)
	        return self.mec
