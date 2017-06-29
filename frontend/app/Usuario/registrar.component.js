angular.
  module('Usuario').
  component('usuarioRegistrar', {
    templateUrl: '/app/Usuario/registrar.template.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Registrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'usuario':'','senha':'','email':''};
      this.registrar = function()
      {
       	ApiUsuario.Registrar(this.formulario,function(resultado) {
          MatWebGlobals.usuarioLogado = resultado.corpo.usuario;
       		$http.defaults.headers.common.Authorization = resultado.corpo.token;
       		window.localStorage.setItem('token_de_acesso', resultado.corpo.token);
       		$location.path("/")
   		}, function(erro){
   			this.erro = erro.data.mensagem
   		} );
   	  }
    }]
  });
