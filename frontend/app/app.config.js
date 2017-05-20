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
          template: '<listar-curso></listar-curso>'
        })
      $routeProvider.when('/Curso/Registrar', {
          template: '<registrar-curso></registrar-curso>'
        })
      $routeProvider.when('/Departamento', {
          template: '<listar-departamento></listar-departamento>'
        })
        $routeProvider.when('/Cadastrar', {
          template: '<registrar-departamento></registrar-departamento>'
        })
      $routeProvider.when('/CadastroDisciplina', {
          template: '<registrar-disciplina></registrar-disciplina>'
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
