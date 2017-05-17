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
          template: '<oferta-cursos></oferta-cursos>'
        })
      $routeProvider.when('/Campus', {
          template: '<listar-campus></listar-campus>'
        })
      $routeProvider.when('/Curso', {
          template: '<curso-listar></curso-listar>'
        })
      $routeProvider.when('/Curso/Registrar', {
          template: '<curso-registrar></curso-registrar>'
        })
      $routeProvider.when('/CadastroDisciplina', {
          template: '<cadastrar-disciplina></cadastrar-disciplina>'
        })
      $routeProvider.when('/Predio', {
          template: '<listar-predio></listar-predio>'
        })
      .otherwise('/');
      $routeProvider.when('/Registrodesala/Cadastrar', {
          template: '<sala-registrar></sala-registrar>'
        })
    }
  ]).value('MatWebGlobals', {});
