import json
from Framework.ModelParaJson import ModelParaJson

class Resposta(object):

	def getStatus(self):
		return "200 OK"

	def getCabecalho(self):
		return [('Content-Type', 'application/json; charset=UTF-8'),('Content-Length', str(len(self.getCorpo())))]

	def getCorpo(self):
		return json.dumps(self, cls=ModelParaJson)