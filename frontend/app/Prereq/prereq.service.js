angular.
  module('Prereq').
  factory('ApiPrereq', ['$resource',
    function($resource) {
      return $resource('/api/Prereq/Listar', {}, {
          Listar: { method: 'POST'},
      });
    }
  ]);