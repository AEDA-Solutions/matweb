angular.
  module('Campus').
  component('ofertaCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', 'MatWebGlobals',function Entrar(ApiCampus,MatWebGlobals) {
  var ctrl = this;
  ctrl.campus = [];
      this.pesquisar = function(){
        console.log("q q ta acontecendo")
        ApiCampus.Listar({ nome:"", pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.campus = resultado.corpo
      console.log(ctrl.campus)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });
