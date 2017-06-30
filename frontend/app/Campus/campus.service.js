angular.
  module('Campus').
  factory('ApiCampus', ['$resource',
    function($resource) {
      return $resource('/api/Campus/Listar', {}, {
        Listar: { method: 'POST' }
      });
    }
  ]).
factory('ApiCampusCadastrar', ['$resource',
    function($resource) {
      return $resource('/api/Campus/Cadastrar', {}, {
        Cadastrar: { method: 'POST' }
      });
    }
  ]).
factory('ApiCampusEditar', ['$resource',
    function($resource) {
      return $resource('/api/Campus/Editar', {}, {
        Editar: { method: 'POST' }
      });
    }
  ]).
factory('ApiCampusDeletar', ['$resource',
    function($resource) {
      return $resource('/api/Campus/Deletar', {}, {
        Deletar: { method: 'POST' }
      });
    }
  ]);
