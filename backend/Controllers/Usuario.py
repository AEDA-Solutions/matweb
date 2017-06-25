# coding=utf-8
from Framework.Controller import Controller
from Framework.ErroNoHTTP import ErroNoHTTP
from Database.Controllers.Usuario import Usuario as BDUsuario
from Models.Usuario.RespostaEntrar import RespostaEntrar
from Models.Usuario.RespostaCadastrar import RespostaCadastrar
from Models.Usuario.RespostaListar import RespostaListar
from Models.Usuario.RespostaEditar import RespostaEditar
from Models.Usuario.RespostaDeletar import RespostaDeletar
from Database.Models.Usuario import Usuario as ModelUsuario
from Framework.Autenticacao import Autenticacao
import bcrypt

class Usuario(Controller):


	def Entrar(self,pedido_entrar):
		usuario = BDUsuario().pegarUsuario("WHERE matricula = %s OR cpf = %s",(pedido_entrar.getLoginDoUsuario(),pedido_entrar.getLoginDoUsuario()))
		if usuario is not None:
			if(bcrypt.hashpw(pedido_entrar.getSenhaDoUsuario().encode('utf-8'), usuario.getSenhaHashed().encode('utf-8')) == usuario.getSenhaHashed().encode('utf-8')):
				return RespostaEntrar(Autenticacao.gerarToken(usuario,pedido_entrar.variaveis_do_ambiente["REMOTE_ADDR"]),usuario)
			else:
				raise ErroNoHTTP(401,"Senha inválida!")
		else:
			raise ErroNoHTTP(401,"Usuário não encontrado!")

	def __gerarToken(self,usuario,pedido_entrar):
		return uuid.uuid4().hex

	def Sair(self,pedido_sair):
		pass

	def Listar(self,pedido_listar):
		usuarios = BDUsuario().pegarUsuarios("WHERE matricula = %s OR cpf = %s OR nome like %s",(pedido_listar.getUsuario(),pedido_listar.getUsuario(),"%"+pedido_listar.getUsuario()+"%"))
		return RespostaListar(usuarios)

	def TrataPedido(self,pedido,usuario):
		usuario.setNome(pedido.getNome())
		usuario.setMatricula(pedido.getMatricula())		
		usuario.setCpf(pedido.getCpf())
		usuario.setPerfil(pedido.getPerfil())
		usuario.setEmail(pedido.getEmail())
		usuario.setSexo(pedido.getSexo())
		usuario.setNome_pai(pedido.getNome_pai())
		usuario.setNome_mae(pedido.getNome_mae())
		usuario.setAno_conclusao(pedido.getAno_conclusao())
		usuario.setIdentidade(pedido.getIdentidade())
		usuario.setSenhaHashed(bcrypt.hashpw(pedido.getSenha().encode('utf-8'), bcrypt.gensalt()))
		return usuario
	
	def Cadastrar(self,pedido_cadastrar):
		usuario = BDUsuario()
		usuario = self.TrataPedido(pedido_cadastrar,usuario)
		return RespostaCadastrar(BDUsuario().inserirUsuario(usuario))


	def Ver(self,pedido_ver):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_ver.getId()))
		if usuario is not None:
			return None
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")

	def Editar(self,pedido_editar):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_editar.getId(),))
		if usuario is not None:
			usuario = self.TrataPedido(pedido_editar,usuario)
			BDUsuario().alterarUsuario(usuario)
			return RespostaEditar("Usuário Alterado com Sucesso")
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")
			

	def AlterarSenha(self,pedido_alterar_senha):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s",(pedido_alterar_senha.getId()))
		if usuario is not None:
			usuario.setSenhaHashed(bcrypt.hashpw(pedido_alterar_senha.getNovaSenha().encode('utf-8'), bcrypt.gensalt()))
			BDUsuario().alterarUsuario(usuario)
		else:
			raise ErroNoHTTP(404,"Usuário inexistente!")
			
	def Deletar(self,pedido_deletar):
		usuario = BDUsuario().pegarUsuario("WHERE id = %s ", (pedido_deletar.getId(),))		
		BDUsuario().removerUsuario(usuario)
		return RespostaDeletar("Campus Removido com sucesso!")

