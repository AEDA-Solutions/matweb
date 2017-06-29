angular.
  module('Cadastrar').
  factory('ApiSexo', ['$resource',
    function($resource) {
      return $resource('/api/Departamento/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
