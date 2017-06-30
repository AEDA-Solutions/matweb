angular.
  module('CursoNav').
  factory('ApiCampusNav', ['$resource',
    function($resource) {
      return $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);