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
  ]). 
  factory('ApiDepartamentoGerenciar', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/Gerenciar', {}, {
          Gerenciar: { method: 'POST'},
        });
    }                                                                      
  ]). 
  factory('ApiDepartamentoCadastrar', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/Cadastrar', {}, {
          Cadastrar: { method: 'POST'},
        });
    }                                                                      
  ]). 
factory('ApiDepartamentoEditar', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/Editar', {}, {
          Editar: { method: 'POST'},
        });
    }                                                                      
  ]). 
factory('ApiDepartamentoDeletar', ['$resource',
    function($resource) {
        return $resource('/api/Departamento/Deletar', {}, {
          Deletar: { method: 'POST'},
        });
    }                                                                      
  ]);