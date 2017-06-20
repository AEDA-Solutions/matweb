from Configuracao import Configuracao
import atexit
import psycopg2
import psycopg2.extras


class BancoDeDados(object):
	
	conexao = None
	cursor = None

	def __init__(self):
		if(BancoDeDados.conexao == None or BancoDeDados.cursor == None):
			self.abrir()
		elif(BancoDeDados.cursor.closed or BancoDeDados.conexao.closed != 0):
			self.fechar
			self.abrir()

	def abrir(self):
			BancoDeDados.conexao = psycopg2.connect(Configuracao().getConfiguracao('BancoDeDados')['StringDeConexao'])
			BancoDeDados.cursor = BancoDeDados.conexao.cursor(cursor_factory=psycopg2.extras.DictCursor)

	def consultarUnico(self,SQL,dados):
		BancoDeDados.cursor.execute(SQL,dados)
		return BancoDeDados.cursor.fetchone()
	
	def consultarMultiplos(self, SQL, dados):
		BancoDeDados.cursor.execute(SQL,dados)
		return BancoDeDados.cursor.fetchall()
			
	def executar(self, SQL, dados):
		BancoDeDados.cursor.execute(SQL,dados)
		BancoDeDados.conexao.commit()

	def pegarUltimoIDInserido(self):
		return BancoDeDados.cursor.fetchone()[0]

	@atexit.register
	def fechar():
		BancoDeDados.cursor.close()
		BancoDeDados.conexao.close()
