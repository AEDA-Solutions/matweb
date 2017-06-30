angular.
  module('nucleoadmin').
  component('adminUsuario', {
    templateUrl: '/app/Menuprincipaladmin/index.html',
    controller: ['MatWebGlobals', function Menu(MatWebGlobals) {
      if (typeof MatWebGlobals.usuarioLogado !== 'undefined') {
        this.perfil = MatWebGlobals.usuarioLogado.perfil;
      }else{
        this.perfil = ""
      }
    }]
  });