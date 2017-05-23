angular.
  module('Cadastrarpredio').
  component('registrarCurso', {
    templateUrl: '/app/Cadastrarpredio/cadastrarpredio.template.html',
    controller: ['ApiRegistroPredio','$http','$location', 'MatWebGlobals',function(ApiRegistroPredio,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','sigla':'','latitude':'','longitude':'','id_campus': 1 };
      this.cadastrar = function()
      {
          ApiRegistroPredio.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Curso cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
