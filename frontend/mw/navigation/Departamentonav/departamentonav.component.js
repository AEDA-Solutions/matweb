angular.
  module('DepartamentoNav').
  component('listarDepartamentonav', {
    templateUrl: '/mw/navigation/Departamentonav/departamentonav.template.html',
    controller: ['ApiDepartamentoNav', 'MatWebGlobals', '$routeParams', function Listar(ApiDepartamentoNav,MatWebGlobals,$routeParams) {
        
        this.nome_departamento = "";
        var ctrl = this;
        this.formulario = {id_campus: $routeParams.Id_campusnav , 'nome': crtl.nome_departamento, 'pagina': 0, 'quantidade': 1000 };
        console.log($routeParams.Id_campusnav);
        

      
            ApiDepartamentoNav.Listar(this.formulario,function(resultado) {
                ctrl.departamentos = resultado.corpo;
                MatWebGlobals.departamentosnavs = resultado.corpo;

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
