angular.
  module('Disciplina').
  factory('ApiDisciplina', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Listar', {}, {
          Listar: { method: 'POST'},
      });
    }
  ]);