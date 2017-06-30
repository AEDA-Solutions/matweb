angular.
  module('Matricular').
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
        return $resource('/api/Matricula/Cadastrar',{}, {
            Cadastrar: { method: 'POST'},
        });
    }                                
]). 