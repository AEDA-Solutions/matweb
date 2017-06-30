angular.
  module('Matricular').
	factory('ApiOfertaPDepartTest', ['$resource',
    function($resource) {
        return $resource('/api/Disciplina/Listar', {}, {
          Listar: { method: 'POST'},
        });
    }                                                                      
  ]).
  factory('ApiOfertaDetalharTest',['$resource',
    function($resource) {
        return $resource('/api/Oferta/Detalhar',{}, {
            Detalhar: { method: 'POST'},
        });
    }                                
]). 
  factory('ApiDisciplinaCadastrarTest',['$resource',
    function($resource) {
        return $resource('/api/Matricula/Cadastrar',{}, {
            Cadastrar: { method: 'POST'},
        });
    }                                
]). 