angular.
  module('Campus').
  component('ofertaCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', '$uibModal', 'MatWebGlobals',function Entrar(ApiCampus,$uibModal,MatWebGlobals) {
  var ctrl = this;
        ctrl.campus = [];

            ApiCampusNav.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
                ctrl.campus = resultado.corpo;
                console.log(ctrl.campus)
            }, function(error){
                ctrl.error = error.data.mensagem;
                console.log(ctrl.error)
            });

            this.abrir = function(id){

                $uibModal.open({
                animation: 'true',
                component: 'modalCampus',
                size: 'sm',
                });

            MatWebGlobals.Id = id;

            console.log(id)
            console.log(MatWebGlobals.Id)
            }
        
    }]
});
  