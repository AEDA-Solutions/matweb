angular.
  module('Cadastrarmateria').
  component('registrarOferta', {
    templateUrl: '/app/Cadastrarmateria/cadastrarmateria.template.html',
    controller: ['ApiRegistrarOferta','$http','$location', 'MatWebGlobals',function(ApiRegistrarOferta,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'id_departamento':'','nome':'','codigo':''};
      this.cadastrar = function()
      {
          ApiRegistrarOferta.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Disciplina cadastrada com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
