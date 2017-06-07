angular.
  module('Cadastrarusuario').
  factory('ApiUsuarioCadastrar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
