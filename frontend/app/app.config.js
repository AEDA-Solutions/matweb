angular.
  module('MatWeb').
  config(['$locationProvider', '$routeProvider', '$httpProvider',
    function config($locationProvider, $routeProvider, $httpProvider) {
      $locationProvider.html5Mode(true).hashPrefix('!');
      
      $httpProvider.defaults.headers.common.Authorization = window.localStorage.getItem('token_de_acesso');
      $httpProvider.defaults.headers.post = { 'Content-Type' : 'application/json; charset=UTF-8' }

      $routeProvider.when('/Admin/Entrar', {
          template: '<admin-entrar></admin-entrar>'
        })
      $routeProvider.when('/Admin', {
          template: '<admin-usuario></admin-usuario>'
        })
      $routeProvider.when('/Usuario/Entrar', {
          template: '<usuario-entrar></usuario-entrar>'
        })
      $routeProvider.when('/Usuario/Dados', {
          template: '<usuario-dados></usuario-dados>'
        })
      $routeProvider.when('/Usuario/Cadastrar', {
          template: '<registrar-usuario></registrar-usuario>'
        })
      $routeProvider.when('/Disciplina/Info', {
          template: '<materia-info></materia-info>'
        })
      $routeProvider.when('/Usuario/Home', {
          template: '<casa-usuario></casa-usuario>'
        })
      $routeProvider.when('/', {
          template: '<tela-principal></tela-principal>'
        })
      $routeProvider.when('/Oferta/Cadastrar', {
          template: '<registrar-oferta></registrar-oferta>'
        })
      $routeProvider.when('/Oferta', {
          template: '<oferta-disciplina></oferta-disciplina>'
        })
      $routeProvider.when('/Oferta/:Id_departamento', {
          template: '<oferta-discpdepart></oferta-discpdepart>'
        })
      $routeProvider.when('/Oferta/Listar/:Id_departamentonav', {
          template: '<listar-ofertanav></listar-ofertanav>'
        })
      $routeProvider.when('/Oferta/Detalhar/:Id_disciplina', {
          template: '<oferta-detalhar></oferta-detalhar>'
        })
      $routeProvider.when('/Campus', {
          template: '<listar-campus></listar-campus>'
        })
      $routeProvider.when('/Campus/Listar', {
          template: '<listar-campusnav></listar-campusnav>'
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
      $routeProvider.when('/Departamento/:Id_campus', {
          template: '<listar-departpcampus></listar-departpcampus>'
        })
      $routeProvider.when('/Departamento/Listar/:Id_campusnav', {
          template: '<listar-departamentonav></listar-departamentonav>'
        })
      $routeProvider.when('/Curso/Listar/:Id_campusnav', {
          template: '<listar-cursonav></listar-cursonav>'
        })
        $routeProvider.when('/Cadastrar', {
          template: '<registrar-departamento></registrar-departamento>'
        })
        $routeProvider.when('/Usuario/Grade', {
          template: '<usuario-grade></usuario-grade>'
        })
      $routeProvider.when('/Cadastro/Disciplina', {
          template: '<registrar-disciplina></registrar-disciplina>'
        })
      $routeProvider.when('/Predio', {
          template: '<listar-predio></listar-predio>'
        })
      $routeProvider.when('/Predio/Cadastrar', {
          template: '<cadastrar-predio></cadastrar-predio>'
        })
      .otherwise('/');
      $routeProvider.when('/Registrodesala/Cadastrar', {
          template: '<sala-registrar></sala-registrar>'
        })
      $routeProvider.when('/Salas', {
          template: '<listar-salas></listar-salas>'
        })
    }
  ]).value('MatWebGlobals', {});
