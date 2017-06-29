angular.
  module('Curriculo').
  factory('ApiCurriculo', ['$resource',
    function($resource) {
      return $resource('/api/Curriculo', {}, {});
    }
  ]);