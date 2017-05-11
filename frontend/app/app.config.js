angular.
  module('MatWeb').
  config(['$locationProvider', '$routeProvider', '$httpProvider',
    function config($locationProvider, $routeProvider, $httpProvider) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      
      $httpProvider.defaults.headers.common.Authorization = window.localStorage.getItem('token_de_acesso');
      $httpProvider.defaults.headers.post = { 'Content-Type' : 'application/json; charset=UTF-8' }

      $routeProvider.when('/Usuario/Entrar', {
          template: '<usuario-entrar></usuario-entrar>'
        })
      $routeProvider.when('/', {
          template: '<tela-principal></tela-principal>'
        })
      $routeProvider.when('/Oferta', {
          template: '<listar-cursos></listar-cursos>'
        })
      $routeProvider.when('/Campus/Listar', {
          template: '<oferta-campus></oferta-campus>'
        })
      $routeProvider.when('/Curso', {
          template: '<curso-listar></curso-listar>'
        })
      $routeProvider.when('/Curso/Registrar', {
          template: '<curso-registrar></curso-registrar>'
        })
      .otherwise('/');
    }
  ]).value('MatWebGlobals', {});
