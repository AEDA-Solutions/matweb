angular.
  module('Campus').
  component('ofertaCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', '$uibModal', 'MatWebGlobals',function Entrar($uibModal, ApiCampus,MatWebGlobals) {
  var ctrl = this;
  ctrl.campus = [];
  
        ApiCampus.Listar({ nome:"", pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.campus = resultado.corpo
      console.log(ctrl.campus)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );

      this.abrir = function(){

      $uibModal.open({
      animation: 'true',
      component: 'modalCampus',
      size: 'sm',
      });

      }
      
    }]
  });
