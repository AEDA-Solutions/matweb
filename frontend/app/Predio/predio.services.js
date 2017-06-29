angular.
  module('Predio').
  factory('ApiPredio', ['$resource',
    function($resource) {
      return $resource('/api/Predio/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);
