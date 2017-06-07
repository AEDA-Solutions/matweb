angular.
  module('Prereq').
  component('prereqListar', {
    templateUrl: '/app/Prereq/listar.template.html',
    controller: ['ApiPrereq', 'MatWebGlobals','$scope', function Listar(ApiPrereq,MatWebGlobals,$scope) {
      this.formulario = {'disciplina':'','pagina':'','quantidade':''};
      this.listar = function()
      {
       	ApiPrereq.Listar(this.formulario,function(resultado) {
          MatWebGlobals.disciplinasListadas = resultado.corpo.disciplina;
          cosole.log(MatWebGlobals);
   		}, function(error){
            $scope.erro = error.data.mensagem;
            $scope.$digest();
   		} );
   	  }
    }]
  });
