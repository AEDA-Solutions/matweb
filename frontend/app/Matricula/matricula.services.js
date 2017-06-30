angular.
  module('Matricular').
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