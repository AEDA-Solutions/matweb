angular.
  module('Sala').
  factory('ApiSala', ['$resource',
    function($resource) {
      return $resource('/api/Sala', {}, {});
    }
  ]);