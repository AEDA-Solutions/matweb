angular.
  module('DepartamentoNav').
  factory('ApiDepartamentoNav', ['$resource',
    function($resource) {
      return $resource('/api/Departamento/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);