angular.
  module('Cadastrar').
  component('registrarDepartamento', {
    templateUrl: '/app/Cadastrar/cadastrar.template.html',
    controller: ['ApiSexo','$http','$location', 'MatWebGlobals',function(ApiSexo,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','id_campus':'','sigla':'','codigo':'0'};
      this.cadastrar = function()
      {
          ApiSexo.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Departamento cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
