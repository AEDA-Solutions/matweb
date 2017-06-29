angular.
  module('Horario').
  component('ofertaHorario', {
    templateUrl: '/app/Horario/horario.template.html',
    controller: ['ApiHorario', 'MatWebGlobals',function Entrar(ApiHorario,MatWebGlobals) {
      this.nome_horario = "";
  var ctrl = this;
  ctrl.horario = [];
      this.pesquisar = function()
      {
        ApiHorario.Listar({},function(resultado) {
              ctrl.horario = resultado.corpo
      console.log(ctrl.horario)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });