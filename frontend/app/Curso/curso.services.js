angular.
  module('Curso').
  factory('ApiCurso', ['$resource',
    function($resource) {

      return $resource('/api/Curso/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
]).
  factory('ApiCursoPCampus', ['$resource',
    function($resource) {
        return $resource('/api/Curso/Listar', {}, {
          Listar: { method: 'POST'},
        });
    }                                                                      
  ]). 
  factory('ApiCursoGerenciar', ['$resource',
    function($resource) {
        return $resource('/api/Curso/Gerenciar', {}, {
          Gerenciar: { method: 'POST'},
        });
    }                                                                      
  ]). 
  factory('ApiCursoCadastrar', ['$resource',
    function($resource) {
        return $resource('/api/Curso/Cadastrar', {}, {
          Cadastrar: { method: 'POST'},
        });
    }                                                                      
  ]). 
factory('ApiCursoEditar', ['$resource',
    function($resource) {
        return $resource('/api/Curso/Editar', {}, {
          Editar: { method: 'POST'},
        });
    }                                                                      
  ]). 
factory('ApiCursoDeletar', ['$resource',
    function($resource) {
        return $resource('/api/Curso/Deletar', {}, {
          Deletar: { method: 'POST'},
        });
    }                                                                      
  ]). 
factory('ApiFluxoListar', ['$resource',
    function($resource) {
        return $resource('/api/Fluxo/Listar', {}, {
          Listar: { method: 'POST'},
        });
    }                                                                      
  ]);