angular.
  module('Admin').
  factory('ApiAdmin', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Entrar', {}, {
        Entrar: { method: 'POST' },
      });
    }
  ]);