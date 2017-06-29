from Database.Controllers.RegistroLogin import RegistroLogin as DBRegistroLogin
from Database.Models.RegistroLogin import RegistroLogin as ModelRegistroLogin
import uuid

class Autenticacao(object):

	@staticmethod
	def getUsuarioPeloTokenEIpEValido(token,ip):
		token = DBRegistroLogin().pegarRegistro("WHERE token = %s AND ip = %s",(token,ip))
		if token is not None:
			return token.getUsuario()
		else:
			return None

	@staticmethod
	def gerarToken(usuario,ip):
		token = ModelRegistroLogin()
		token.setUsuario(usuario)
		token.setToken(uuid.uuid4().hex)
		token.setIp(ip)
		token = DBRegistroLogin().inserirRegistro(token)
		return token.getToken()

	@staticmethod
	def temAcesso(metodo,perfis):
		def metodo_com_acesso(self,pedido):
			usuario = Autenticacao.getUsuarioPeloTokenEIpEValido(pedido.variaveis_do_ambiente["AUTHORIZATION"])
			if usuario.getPerfil() in perfis:
				return metodo(self,pedido,usuario)
			else:
				ErroNoHTTP(403,"Acesso Negado!")
		return metodo_com_acesso