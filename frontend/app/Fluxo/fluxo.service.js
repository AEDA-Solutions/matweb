angular.
  module('Fluxo').
  factory('ApiFluxo', ['$resource',
    function($resource) {
      return $resource('/api/Fluxo', {}, {});
    }
  ]);