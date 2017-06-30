angular.
  module('Usuario').
  component('usuarioEntrar', {
<<<<<<< HEAD
    templateUrl: '/app/Usuario/entrar.template.html',
=======
    templateUrl: '/app/Usuario/admin.html',
>>>>>>> pedrogabriel96
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiUsuario,$http,$location,MatWebGlobals,$scope) {
      this.formulario = {'usuario':'','senha':''};
      this.entrar = function()
      {
        ApiUsuario.Entrar(this.formulario,function(resultado) {
          MatWebGlobals.usuarioLogado = resultado.corpo.usuario;
<<<<<<< HEAD
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
       		$location.path('/Usuario/Home')
   		}, function(error){
            $scope.erro = error.data.mensagem;
            $scope.$digest();
   		} );
   	  }
=======
          $http.defaults.headers.common.Authorization = resultado.corpo.token;
          window.sessionStorage.setItem('token_de_acesso', resultado.corpo.token);
          window.sessionStorage.setItem('UserName',MatWebGlobals.usuarioLogado.nome);
          window.sessionStorage.setItem('UserCPF',MatWebGlobals.usuarioLogado.cpf);
          window.sessionStorage.setItem('UserProfile',MatWebGlobals.usuarioLogado.perfil);
          window.top.location.href = '/Usuario/Home';
      }, function(error){
            $scope.erro = error.data.mensagem;
            $scope.$digest();
      } );
      }
>>>>>>> pedrogabriel96
    }]
});
