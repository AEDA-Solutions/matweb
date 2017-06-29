angular.
  module('Departamento').
  component('listarDepartamento', {
    templateUrl: '/app/Departamento/pesquisar.template.html',
    controller: ['ApiDepartamento', 'MatWebGlobals',function Dep(ApiDepartamento,MatWebGlobals) {
      this.nome_departamento = "";
      this.campi = "";
  var ctrl = this;
  ctrl.departamento = [];
      this.pesquisar = function()
      {
        ApiDepartamento.Listar({id_campus: ctrl.campi , nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.departamento = resultado.corpo
      console.log(ctrl.departamento)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  }).
  component('listarDepartamentoc', {
    templateUrl: '/app/Departamento/listarc.template.html',
    controller: ['ApiDepartamentoc','$routeParams','MatWebGlobals',function Dep(ApiDepartamentoc,$routeParams,MatWebGlobals) {
      this.formulario = {id_campus: $routeParams.Id_campus, 'nome': '', 'pagina': 0, 'quantidade': 1000}
      console.log($routeParams)
  var ctrl = this;
      this.listar = function()
      {
        ApiDepartamentoc.Listar(this.formulario,function(resultado) {
              ctrl.departamento = resultado.corpo
      console.log(ctrl.departamento)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      });
      }
      this.listar();

    }]
  });
