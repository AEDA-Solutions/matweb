angular.
  module('Matricular').
    factory('ApiDisciplinaCadastrar',['$resource',
    function($resource) {
        return $resource('/api/Matricula/Cadastrar',{}, {
            Cadastrar: { method: 'POST'},
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
    factory('ApiDisciplinaEditar',['$resource',
    function($resource) {
        return $resource('/api/Matricula/Editar',{}, {
            Editar: { method: 'POST'},
        });
    }                                
]). factory('ApiDisciplinaDeletar',['$resource',
    function($resource) {
        return $resource('/api/Matricula/Deletar',{}, {
            Deletar: { method: 'POST'},
        });
    }                                
]);