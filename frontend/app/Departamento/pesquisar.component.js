angular.
  module('Departamento').
  component('listarDepartamento', {
    templateUrl: '/app/Departamento/pesquisar.template.html',
    controller: ['ApiDepartamento', 'MatWebGlobals',function Dep(ApiDepartamento,MatWebGlobals) {
      this.nome_departamento = "";
  var ctrl = this;
  ctrl.departamento = [];
      this.pesquisar = function()
      {
        ApiDepartamento.Listar({id_campus: 1 , nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.departamento = resultado.corpo
      console.log(ctrl.departamento)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });