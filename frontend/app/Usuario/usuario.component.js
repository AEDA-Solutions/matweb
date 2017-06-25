angular.
  module('Usuario').
  component('usuarioGerenciar', {
    templateUrl: '/app/Usuario/usuario.adm.template.html',
    controller: ['ApiUsuario','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiUsuario,$http,$location,MatWebGlobals,$scope) {
    }]
});