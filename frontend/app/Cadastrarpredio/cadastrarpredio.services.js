angular.
  module('Cadastrarpredio').
  factory('ApiRegistroPredio', ['$resource',
    function($resource) {
      return $resource('/api/Predio/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
