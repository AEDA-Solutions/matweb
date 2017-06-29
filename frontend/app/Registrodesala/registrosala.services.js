angular.
  module('Registrodesala').
  factory('ApiSala', ['$resource',
    function($resource) {
      return $resource('/api/Sala/Cadastrar', {}, {
        Cadastrar: { method: 'POST' },
      });
    }
  ]);
