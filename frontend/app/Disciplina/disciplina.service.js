angular.
  module('Disciplina').
  factory('ApiDisciplina', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/:operacao', {}, {
        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"}}

      });
    }
  ]).
  factory('ApiDisciplinaListar', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/:operacao', {}, {
        Listar: { method: 'POST', params: {'operacao': "Listar"}}
      });
    }
  ]);
