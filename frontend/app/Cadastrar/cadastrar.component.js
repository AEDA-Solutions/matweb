angular.
  module('Cadastrar').
  component('resgistrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiDepartamentoRegistrar','$http','$location', 'MatWebGlobals',function(ApiDepartamentoRegistrar,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'depName':''};
      this.cadastrar = function()
      {
          ApiDepartamentoRegistrar.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Departamento cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
