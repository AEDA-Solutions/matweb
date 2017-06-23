angular.
  module('Home').
  component('casaUsuario', {
    templateUrl: '/app/Home/index.html',
    controller: ['ApiHome', 'MatWebGlobals', '$scope', '$location', function Entrar(ApiHome,MatWebGlobals,$scope,$location) {
        if (window.sessionStorage.hasOwnProperty('token_de_acesso')) {
            $scope.nomeUsuario = window.sessionStorage.getItem('UserName');
            $scope.cpfUsuario = window.sessionStorage.getItem('UserCPF');
            $scope.perfilUsuario = window.sessionStorage.getItem('UserProfile');
            console.log($scope.perfilUsuario);
        } else {
            $location.path('/Usuario/Entrar');
        }
        
  var ctrl = this;
  ctrl.usuarios = [];
        this.pesquisar = function()
      {
        ApiHome.Listar({},function(resultado) {
              ctrl.usuarios = resultado.corpo
      console.log(ctrl.usuarios)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
});