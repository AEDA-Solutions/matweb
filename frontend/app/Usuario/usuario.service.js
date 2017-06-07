angular.
  module('Usuario').
  factory('ApiUsuario', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Entrar', {}, {
        Entrar: { method: 'POST' },
      });
    }
]);