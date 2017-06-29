angular.
  module('Turma').
  factory('ApiTurma', ['$resource',
    function($resource) {
      return $resource('/api/Turma', {}, {});
    }
  ]);