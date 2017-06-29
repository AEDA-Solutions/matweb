angular.
  module('Grade').
  factory('ApiGrade', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Mostrar', {}, {
        Mostrar: {},
      });
    }
  ]);
