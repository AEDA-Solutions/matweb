angular.
  module('DadosUsuario').
  component('usuarioDados', {
    templateUrl: '/app/DadosClient/dados.template.html',
    controller: ['ApiDados', 'MatWebGlobals', '$scope', '$location', function Entrar(ApiDados,MatWebGlobals,$scope,$location) {
        if ( window.sessionStorage.hasOwnProperty('token_de_acesso') && window.sessionStorage.getItem('token_de_acesso') != '') {
            $scope.nomeUsuario = MatWebGlobals.usuarioLogado.nome;
            $scope.cpfUsuario = MatWebGlobals.usuarioLogado.cpf;
            $scope.perfilUsuario = MatWebGlobals.usuarioLogado.perfil;
            $scope.matriculaUsuario = MatWebGlobals.usuarioLogado.matricula;
            console.log($scope.perfilUsuario);
        } else {
            $location.path('/');
        }
  var ctrl = this;
  ctrl.usuarios = [];
        this.pesquisar = function()
      {
        ApiDados.Listar({},function(resultado) {
              ctrl.usuarios = resultado.corpo
      console.log(ctrl.usuarios)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
});