angular.
  module('Cadastrarmateria').
  factory('ApiRegistrarOferta', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
