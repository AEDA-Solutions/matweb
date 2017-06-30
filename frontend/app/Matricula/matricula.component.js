angular.
  module('Matricular').
  component('usuarioMatricular', {
    templateUrl: '/app/Matricula/matricula.template.html',
    controller: ['ApiMatricular','$http','$location', 'MatWebGlobals',function(ApiMatricular,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','sigla':'','latitude':'','longitude':'','id_campus': 1 };
      this.cadastrar = function()
      {
          ApiMatricular.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Prédio cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
}).
  
