angular.
  module('DadosUsuario').
  factory('ApiDados', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Mostrar', {}, {
        Mostrar: {},
      });
    }
  ]);
