angular.
  module('Usuario').
  factory('ApiUsuario', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Entrar', {}, {
        Entrar: { method: 'POST' },
      });
    }
]). 
  factory('ApiUsuarioListar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
]);