angular.
  module('Sala').
  factory('ApiSalas', ['$resource',
    function($resource) {
      return $resource('/api/Sala/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);
