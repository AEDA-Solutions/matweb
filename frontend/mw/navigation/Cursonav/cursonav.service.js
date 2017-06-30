angular.
  module('CursoNav').
  factory('ApiCursoNav', ['$resource',
    function($resource) {
      return $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);