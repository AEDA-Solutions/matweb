angular.
  module('Home').
  component('casaUsuario', {
    templateUrl: '/app/Home/index.html',
    controller: ['ApiHome', 'MatWebGlobals', '$scope', '$location', function Entrar(ApiHome,MatWebGlobals,$scope,$location) {
        if (window.sessionStorage.hasOwnProperty('usuarioLogado')) {
            $scope.nomeUsuario = window.sessionStorage.usuarioLogado.nome;
            $scope.cpfUsuario = window.sessionStorage.usuarioLogado.cpf;
            console.log(window.sessionStorage.getItem('usuarioLogado.nome'));
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