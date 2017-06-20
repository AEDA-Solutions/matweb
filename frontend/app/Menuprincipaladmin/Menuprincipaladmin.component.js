angular.
  module('nucleoadmin').
  component('adminUsuario', {
    templateUrl: '/app/Menuprincipaladmin/index.html',
    controller: ['ApiMenuAdmin', 'MatWebGlobals', '$scope', '$location', function Entrar(ApiMenuAdmin,MatWebGlobals,$scope,$location) {
        if (MatWebGlobals.hasOwnProperty('usuarioLogado')) {
            $scope.nomeUsuario = MatWebGlobals.usuarioLogado.nome;
            $scope.cpfUsuario = MatWebGlobals.usuarioLogado.cpf;
        } else {
            $location.path('/Admin/Entrar');
        }
        
  var ctrl = this;
  ctrl.usuarios = [];
        this.pesquisar = function()
      {
        ApiMenuAdmin.Listar({},function(resultado) {
              ctrl.usuarios = resultado.corpo
      console.log(ctrl.usuarios)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
});