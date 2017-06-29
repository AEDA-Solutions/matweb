angular.
  module('Matricular').
  component('usuarioMatricular', {
    templateUrl: '/app/Matricula/matricula.template.html',
    controller: ['ApiTest','$http','$location', 'MatWebGlobals',function(ApiTest,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','id_campus':'','sigla':'','codigo':'0'};
      this.cadastrar = function()
      {
          ApiTest.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Matricula feita com Sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
