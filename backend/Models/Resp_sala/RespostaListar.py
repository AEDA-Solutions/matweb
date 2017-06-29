from Framework.Resposta import Resposta
from Models.Resp_sala.Resp_sala import Resp_sala as ModelResp_sala
class RespostaListar(Resposta):

	def __init__(self,resp_salas):
		self.corpo = []
		for resp_sala in resp_salas:
			self.corpo.append(ModelResp_sala(resp_sala))
