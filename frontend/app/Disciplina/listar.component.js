angular.
  module('Disciplina').
  component('disciplinaListar', {
    templateUrl: '/app/Disciplina/listar.template.html',
    controller: ['ApiDisciplina', 'MatWebGlobals','$scope', function Listar(ApiDisciplina,MatWebGlobals,$scope) {
      this.formulario = {'id_departamento':'','nome':'','pagina':'','quantidade':''};
      this.listar = function()
      {
       	ApiDisciplina.Listar(this.formulario,function(resultado) {
          MatWebGlobals.disciplinasListadas = resultado.corpo.disciplina;
          cosole.log(MatWebGlobals);
   		}, function(error){
            $scope.erro = error.data.mensagem;
            $scope.$digest();
   		} );
   	  }
    }]
  });
