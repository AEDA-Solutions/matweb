angular.
  module('Departamento').
  factory('ApiDepartamento', ['$resource',
    function($resource) {
      return $resource('/api/Departamento', {}, {});
    }
  ]);