angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
      if (typeof MatWebGlobals.usuarioLogado !== 'undefined') {
        this.usuario = MatWebGlobals.usuarioLogado.usuario;
      }else{
        this.usuario = ""
      }
    }]
  });