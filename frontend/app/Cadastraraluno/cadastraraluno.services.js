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
        Cadastrar: { method: 'POST' },
      });
    }
  ]). 
  factory('ApiUsuarioDeletar', ['$resource',
    function($resource) {
      return $resource('/api/Usuario/Deletar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
