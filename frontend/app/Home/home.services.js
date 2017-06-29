angular.
  module('Home').
  factory('ApiHome', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Mostrar', {}, {
        Mostrar: {},
      });
    }
  ]);
