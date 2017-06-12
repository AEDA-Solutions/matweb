# coding=utf-8
from Models.Oferta.RespostaDetalhar import RespostaDetalhar
from Framework.Controller import Controller
from Database.Controllers.Oferta import Oferta as BDOferta
from Database.Controllers.Ass_oferta_turma import Ass_oferta_turma as BDAssof
from Database.Controllers.Turma import Turma as BDTurma
from Database.Controllers.Ass_turma_sala_horario import Ass_turma_sala_horario as BDAssoc
from Database.Controllers.Sala import Sala as BDSala
from Database.Controllers.Horario import Horario as BDHorario
from Models.Horario.Horario import Horario as ModelHorario
from Models.Turma.Turma import Turma as ModelTurma


class Oferta(Controller):

	def Detalhar(self,pedido_detalhar):
		oferta = BDOferta().pegarOferta('where id_disciplina = %s',(str(pedido_detalhar.getId_disciplina())))
		turmas = self.buscaturmas(oferta)
		return RespostaDetalhar(oferta,turmas)

	
	def buscaturmas(self,oferta):
		associacoes = BDAssof().pegarAss_oferta_turmas('where id_oferta = %s',(str(oferta.getId())))
		self.turmas = []
		for associacao in associacoes:
			turma = BDTurma().pegarTurma('where id = %s',(str(associacao.getId_turma()),))
			horarios = self.buscahorarios(turma)
			self.turmas.append(ModelTurma(turma,horarios))
		return self.turmas
			
			
	def buscahorarios(self,turma):
		associacoes = BDAssoc().pegarAss_turma_sala_horarios('where id_turma = %s',(str(turma.getId(),)))
		self.horarios = []
		for associacao in associacoes:
			sala = BDSala().pegarSala('where id = %s',(str(associacao.getId_sala()))).getCodigo()
			horario = BDHorario().pegarHorario('where id = %s',(str(associacao.getId_horario())))
			self.horarios.append(ModelHorario(horario,sala))
		return self.horarios
						