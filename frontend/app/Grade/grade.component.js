angular.
  module('Grade').
  component('usuarioGrade', {
    templateUrl: '/app/Grade/grade.template.html',
    controller: ['ApiGrade', 'MatWebGlobals', '$scope', '$location', function Entrar(ApiGrade,MatWebGlobals,$scope,$location) {
        if (MatWebGlobals.hasOwnProperty('usuarioLogado')) {
            $scope.disciplinaUsuario = MatWebGlobals.usuarioLogado.disciplina;
            $scope.horarioUsuario = MatWebGlobals.usuarioLogado.horario;
        } else {
            $location.path('/Usuario/Entrar');
        }
        
  var ctrl = this;
  ctrl.usuarios = [];
        this.pesquisar = function()
      {
        ApiGrade.Listar({},function(resultado) {
              ctrl.usuarios = resultado.corpo
      console.log(ctrl.usuarios)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
});