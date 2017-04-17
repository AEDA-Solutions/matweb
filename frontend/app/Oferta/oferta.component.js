angular.
  module('Oferta').
  component('ofertaCursos', {
    templateUrl: '/app/Oferta/oferta.template.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Entrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'usuario':'','senha':''};
      this.entrar = function()
      {
       	ApiUsuario.Entrar(this.formulario,function(resultado) {
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
