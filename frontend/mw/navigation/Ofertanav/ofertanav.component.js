angular.
  module('OfertaNav').
  component('listarOfertanav', {
    templateUrl: '/mw/navigation/Ofertanav/ofertanav.template.html',
    controller: ['ApiOfertaNav', 'MatWebGlobals', '$routeParams', function Listar(ApiOfertaNav,MatWebGlobals,$routeParams) {
        this.formulario = {id_departamento: $routeParams.Id_departamentonav , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        console.log($routeParams.Id_departamentonav);
        var ctrl = this;

        this.listar = function(){
      
            ApiOfertaNav.Listar(this.formulario,function(resultado) {
                ctrl.disciplinas = resultado.corpo;

                for(var i = 0, dep = null; i < MatWebGlobals.departamentosnavs.length; i++) {
                    if (MatWebGlobals.departamentosnavs[i].id == $routeParams.Id_departamentonav) {
                       dep = MatWebGlobals.departamentosnavs[i];
                        break;
                    }
                };

                ctrl.departamento_nome = dep.nome;
                console.log(departamento_nome)

            }, function(error){
                ctrl.error = error.data.mensagem;
            });

    }

    this.listar();
        
    }]
});

