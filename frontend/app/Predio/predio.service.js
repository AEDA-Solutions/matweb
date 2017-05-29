angular.
  module('Predio').
  factory('ApiPredio', ['$resource',
    function($resource) {
      return $resource('/api/Predio', {}, {});
    }
  ]);