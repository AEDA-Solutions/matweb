angular.
  module('CampusNav').
  factory('ApiCampusNav', ['$resource',
    function($resource) {
      return $resource('/api/Campus/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);