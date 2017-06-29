from Database.Controllers.Predio import Predio
from Database.Controllers.Resp_sala import Resp_sala

class Sala(object):

	def __init__(self,dados=None):
		if dados is not None:
			self.id = dados ['id']
			self.id_resp_sala = dados ['id_resp_sala']
			self.codigo = dados ['codigo']
			self.id_predio = dados ['id_predio']
			
	def getId(self):
		return self.id

	def setId_resp_sala(self,id_resp_sala):
		self.id_resp_sala = id_resp_sala

	def getId_resp_sala(self):
		return self.id_resp_sala
		
	def getResp_sala(self):
		return (Resp_sala().pegarResp_sala('id = %s',(self.id_resp_sala,))).getNome()

	def setCodigo(self,codigo):
		self.codigo = codigo
		
	def getCodigo(self):
		return self.codigo
		
	def setId_predio(self,id_predio):
		self.id_predio = id_predio
		
	def getId_predio(self):
		return self.id_predio
		
	def getPredio(self):
		return (Predio().pegarPredio('id = %s',(self.id_predio,))).getNome()
	