angular.
  module('Cadastrarcurso').
  factory('ApiCurso', ['$resource',
    function($resource) {
      return $resource('/api/Curso/Cadastrar', {}, {
        Cadastrar: { method: 'POST'},
      });
    }
  ]);
