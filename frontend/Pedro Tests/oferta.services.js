angular.
  module('Sala').
  factory('ApiSala', ['$resource',
    function($resource) {
      return $resource('/api/Sala/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
        Editar: { method: 'POST' },
        Listar: { method: 'POST' },
        Excluir: { method: 'POST' },
      });
    }
  ]);