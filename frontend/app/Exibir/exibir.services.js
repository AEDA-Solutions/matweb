angular.
  module('Exibir').
  factory('ApiExibir', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Listar', {}, {
        Listar: {},
      });
    }
  ]);
