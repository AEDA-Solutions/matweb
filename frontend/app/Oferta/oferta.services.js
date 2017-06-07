angular.
  module('Oferta').
  factory('ApiOferta', ['$resource',
    function($resource) {
      return $resource('/api/Disciplina/Listar', {}, {
        Listar: { method: 'POST' },
      });
    }
  ]);
