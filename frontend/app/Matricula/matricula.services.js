angular.
  module('Matricular').
  factory('ApiMatricular', ['$resource',
    function($resource) {
      return $resource('/api/Matricula/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
