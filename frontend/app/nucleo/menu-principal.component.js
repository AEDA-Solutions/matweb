angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', '$scope', function Menu(MatWebGlobals, $scope) {
      if ( window.sessionStorage.hasOwnProperty('UserName')) {
          $scope.NomeUsuario = window.sessionStorage.getItem('UserName');
          $scope.CPFUsuario = window.sessionStorage.getItem('UserCPF');
          $scope.perfilUsuario = window.sessionStorage.getItem('UserProfile');
      } else {
          $scope.pefilUsuario = "";
      }
    }]
  });