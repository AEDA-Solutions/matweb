angular.
  module('Departamento').
  factory('ApiDepartamento', ['$resource',
    function($resource) {
      return $resource('/api/Departamento/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]).
  factory('ApiDepartamentoPCampus', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/Listar', {}, {
          Listar: { method: 'POST'},
        });
    }                                                                      
  ]);