angular.
  module('Cadastrarcurso').
  factory('ApiRegistroCurso', ['$resource',
    function($resource) {
      return $resource('/api/Curso/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
