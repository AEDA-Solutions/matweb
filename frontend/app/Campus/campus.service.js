angular.
  module('Campus').
  factory('ApiCampus', ['$resource',
    function($resource) {
      return $resource('/api/Campus/Listar', {}, {
        Listar: { method: 'POST' }

      });
    }
  ]);
