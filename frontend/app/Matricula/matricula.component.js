angular.
  module('Matricular').
  component('usuarioMatricular', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiMatricular','ApiCampus', '$http','$location','MatWebGlobals','$scope',function(ApiMatricular,ApiCampus,$http,$location,MatWebGlobals,$scope) {
      var ctrl = this;
      $scope.pedindomatricula = true;
      ctrl.campus = [];
      this.formulario = {'id_usuario':'','id_disciplina':'','id_turma':'','status':''};
      ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
            $scope.listcurso = false;
            ctrl.campus = resultado.corpo;
            MatWebGlobals.campus = resultado.corpo;
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
        
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
