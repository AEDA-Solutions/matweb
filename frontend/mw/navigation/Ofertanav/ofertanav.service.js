angular.
  module('OfertaNav').
  factory('ApiOfertaNav', ['$resource',
    function($resource) {
      return $resource('/api/Oferta/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);