angular.
  module('Departamento').
  component('listarDepartamento', {
    templateUrl: '/app/Departamento/departamento.template.html',
    controller: ['ApiDepartamento', 'MatWebGlobals',function Entrar(ApiDepartamento,MatWebGlobals) {
      this.nome_departamento = "";
	var ctrl = this;
	ctrl.departamentos = [];
      this.pesquisar = function()
      {
       	ApiDepartamento.Listar({id_campus: 1 , nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.departamentos = resultado.corpo
			console.log(ctrl.departamentos)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  }).
  component('listarDepartPCampus', {
    templateUrl: '/app/Departamento/departPcampus.template.html',
    controller: ['ApiDepartamentoPCampus', 'MatWebGlobals', '$routeParams', function Listar(ApiDepartamentoPCampus,MatWebGlobals,$routeParams) {
        this.formulario = {'id_campus': $routeParams.id_campus, 'nome': '', 'pagina':'0', 'quantidade':'1000'};
        this.listar = function()
        {
            ApiDepartamentoPCampus.Listar(this.formulario,function(resultado) {
                ctrl.Departamentos = resultado.corpo;
                console.log(MatWebGlobals);
            }, function(error){
                ctrl.error = error.data.mensagem;
            });
        }
    }]
});

