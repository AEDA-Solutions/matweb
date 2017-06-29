from Framework.Resposta import Resposta
from Models.Resp_sala.Resp_sala import Resp_sala as ModelResp_sala

class RespostaCadastrar(Resposta):

	def __init__(self, resp_sala):
		self.corpo = ModelHorario(resp_sala)