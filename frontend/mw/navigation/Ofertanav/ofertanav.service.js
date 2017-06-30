angular.
  module('OfertaNav').
  factory('ApiOfertaNav', ['$resource',
    function($resource) {
        return $resource('/api/Disciplina/Listar', {}, {
          Listar: { method: 'POST'},
        });
    }                                                                      
  ]);

  