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
]). 
    factory('ApiDisciplinaCadastrar',['$resource',
    function($resource) {
        return $resource('/api/Disciplina/Cadastrar',{}, {
            Cadastrar: { method: 'POST'},
        });
    }                                
]). 
    factory('ApiDisciplinaEditar',['$resource',
    function($resource) {
        return $resource('/api/Disciplina/Editar',{}, {
            Editar: { method: 'POST'},
        });
    }                                
]). factory('ApiDisciplinaDeletar',['$resource',
    function($resource) {
        return $resource('/api/Disciplina/Deletar',{}, {
            Deletar: { method: 'POST'},
        });
    }                                
]);