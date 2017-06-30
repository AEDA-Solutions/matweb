angular.
  module('Usuario').
  component('usuarioEntrar', {
    templateUrl: '/app/Usuario/admin.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiUsuario,$http,$location,MatWebGlobals,$scope) {
      this.formulario = {'usuario':'','senha':''};
      this.entrar = function()
      {
        ApiUsuario.Entrar(this.formulario,function(resultado) {
          MatWebGlobals.usuarioLogado = resultado.corpo.usuario;
          $http.defaults.headers.common.Authorization = resultado.corpo.token;
          window.sessionStorage.setItem('token_de_acesso', resultado.corpo.token);
          window.sessionStorage.setItem('UserName',MatWebGlobals.usuarioLogado.nome);
          window.sessionStorage.setItem('UserCPF',MatWebGlobals.usuarioLogado.cpf);
          window.sessionStorage.setItem('UserProfile',MatWebGlobals.usuarioLogado.perfil);
          window.sessionStorage.setItem('UserId',MatWebGlobals.usuarioLogado.id);
          window.top.location.href = '/Usuario/Home';
      }, function(error){
            $scope.erro = error.data.mensagem;
            $scope.$digest();
      } );
      }
    }]
});