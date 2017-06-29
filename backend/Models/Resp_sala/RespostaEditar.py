from Framework.Resposta import Resposta
from Models.Resp_sala.Resp_sala import Resp_sala as ModelResp_sala

class RespostaEditar(Resposta):

	def __init__(self,mensagem):
		
			self.corpo = mensagem