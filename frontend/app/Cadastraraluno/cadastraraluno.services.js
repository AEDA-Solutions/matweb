angular.
  module('Cadastrarusuario').
  factory('ApiUsuarioCadastrar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]). 
  factory('ApiUsuarioEditar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Editar', {}, {
        Editar: { method: 'POST' },
      });
    }
  ]). 
  factory('ApiUsuarioDeletar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Deletar', {}, {
        Deletar: { method: 'POST' },
      });
    }
  ]);
