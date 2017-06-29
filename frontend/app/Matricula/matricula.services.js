angular.
  module('Matricular').
  factory('ApiTest', ['$resource',
    function($resource) {
      return $resource('/api/Matricula/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
