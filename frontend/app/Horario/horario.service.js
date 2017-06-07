angular.
  module('Horario').
  factory('ApiHorario', ['$resource',
    function($resource) {
      return $resource('/api/Horario', {}, {});
    }
  ]);