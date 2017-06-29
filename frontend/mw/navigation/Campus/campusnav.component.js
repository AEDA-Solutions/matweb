angular.
	module('CampusNav').
	component('listarCampusnav',{
    templateUrl: '/mw/navigation/Campus/campusnav.template.html',
    controller: ['ApiCampusNav', '$uibModal' ,'MatWebGlobals', function Listar(ApiCampusNav,$uibModal,MatWebGlobals) {
        var ctrl = this;
        ctrl.campus = [];

            ApiCampusNav.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
                ctrl.campus = resultado.corpo;
                console.log(ctrl.campus)
            }, function(error){
                ctrl.error = error.data.mensagem;
                console.log(ctrl.error)
            });

            this.abrir = function(){

      	 		$uibModal.open({
      			animation: 'true',
      			component: '',
      			size: 'sm',
      			});
			}
        
    }]
});