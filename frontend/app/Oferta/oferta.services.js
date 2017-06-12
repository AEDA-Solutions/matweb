angular.
  module('Oferta').
  factory('ApiOferta', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]).
  factory('ApiOfertaPDepart', ['$resource',
    function($resource) {
        return $resource('/api/Disciplina/Listar', {}, {
          Listar: { method: 'POST'},
        });
    }                                                                      
  ]).
  factory('ApiOfertaDetalhar',['$resource',
    function($resource) {
        return $resource('/api/Oferta/Detalhar',{}, {
            Detalhar: { method: 'POST'},
        });
    }                                
]);

