angular.
  module('Campus').
  component('listarCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', 'MatWebGlobals',function Entrar(ApiCampus,MatWebGlobals) {
      this.nome_campus = "";
  var ctrl = this;
  ctrl.campus = [];
        ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.campus = resultado.corpo
      console.log(ctrl.campus)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
    }]
  });
