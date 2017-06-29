angular.
  module('Usuario').
  factory('ApiUsuario', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Entrar', {}, {
        Entrar: { method: 'POST' },
        Sair: { method: 'POST' },
        Cadastrar: { method: 'POST' },
        Editar: { method: 'POST' },
        Listar: { method: 'POST' },
        Excluir: { method: 'POST' },
      });
    }
  ]);