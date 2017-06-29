from Framework.Controller import Controller
from Database.Controllers.Turma import Turma as BDTurma
from Models.Turma.RespostaListar import RespostaListar

class Turma(Controller):

      def Listar(self,pedido_listar):
             		      return RespostaListar(BDTurma().pegarTurmas("WHERE id_disciplina = %s AND letra LIKE %s LIMIT %s OFFSET %s",(pedido_listar.getIdDisciplina(),"%".pedido_listar.getLetra().replace(' ','%')."%",pedido_listar.getQuantidade(),(pedido_listar.getQuantidade()*pedido_listar.getPagina()))))
