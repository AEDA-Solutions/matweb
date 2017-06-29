angular.
  module('Exibir').
  component('materiaInfo', {
    templateUrl: '/app/Exibir/exibir.template.html',
    controller: ['ApiExibir', 'MatWebGlobals',function Entrar(ApiExibir,MatWebGlobals) {
      this.nome_disciplina = "";
  var ctrl = this;
  ctrl.disciplina = [];
      this.pesquisar = function()
      {
        ApiExibir.Listar({id_departamento: 95, nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.disciplina = resultado.corpo
      console.log(ctrl.disciplina)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  });
