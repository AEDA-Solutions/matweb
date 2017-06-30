angular.
  module('CursoNav').
  component('listarCursonav', {
    templateUrl: '/mw/navigation/Cursonav/cursonav.template.html',
    controller: ['ApiCursoNav', 'MatWebGlobals', '$routeParams', function Listar(ApiCursoNav,MatWebGlobals,$routeParams) {
        this.formulario = {id_campus: $routeParams.Id_campusnav , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        console.log($routeParams.Id_campusnav);
        var ctrl = this;
      
            ApiCursoNav.Listar(ctrl.formulario,function(resultado) {
                ctrl.cursos = resultado.corpo;

                for(var i = 0, campi = null; i < MatWebGlobals.campusnav.length; i++) {
                    if (MatWebGlobals.campusnav[i].id == $routeParams.Id_campusnav) {
                        campi = MatWebGlobals.campusnav[i];
                        break;
                    }
                };

                ctrl.campusnav_nome = campi.nome;

            }, function(error){
                ctrl.error = error.data.mensagem;
            });
        
    }]
});
