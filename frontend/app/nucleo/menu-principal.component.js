angular.
  module('nucleo').
  component('menuPrincipal', {
    templateUrl: '/app/nucleo/menu-principal.template.html',
    controller: ['MatWebGlobals', '$scope', '$window', function Menu(MatWebGlobals, $scope, $window) {
      if ( window.sessionStorage.hasOwnProperty('UserName')) {
          $scope.NomeUsuario = window.sessionStorage.getItem('UserName');
          $scope.CPFUsuario = window.sessionStorage.getItem('UserCPF');
          $scope.perfilUsuario = window.sessionStorage.getItem('UserProfile');
          if ($scope.perfilUsuario == 'Admin') {
              $scope.admin = true;
          } else if ($scope.perfilUsuario == 'Aluno') {
              $scope.aluno = true;
          }
          console.log($scope);
      } else {
          $scope.pefilUsuario = "";
      };
        $scope.logout = function (){
          $window.sessionstorage.empty();
          $scope.perfilUsuario = "";
          window.location.href = "/";
          console.log('cheguei aqui');
        }
      }]
  });