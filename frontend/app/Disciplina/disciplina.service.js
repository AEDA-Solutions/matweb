angular.
  module('Disciplina').
  factory('ApiDisciplina', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/:operacao', {}, {
        Cadastrar: { method: 'POST', params: {'operacao': "Cadastrar"} }
      });
    }
  ]);