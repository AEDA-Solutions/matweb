angular.
  module('nucleoadmin').
  factory('ApiMenuAdmin', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Mostrar', {}, {
        Mostrar: {},
      });
    }
  ]);