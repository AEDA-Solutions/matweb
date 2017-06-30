angular.
  module('Matricular').
  component('usuarioMatricular', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiMatricular','$http','$location','MatWebGlobals','$scope',function(ApiMatricular,$http,$location,MatWebGlobals,$scope) {
      var ctrl = this;
      $scope.pedindomatricula = true;
      this.formulario = {'id_usuario':'','id_disciplina':'','id_turma':'','status':''};
      this.cadastrar = function()
      {
          ApiMatricular.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Matricula feita com Sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
