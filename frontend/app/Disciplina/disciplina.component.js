angular.
  module('Disciplina').
  component('cadastrarDisciplina', {
    templateUrl: '/app/Disciplina/cadastrar.template.html',
    controller: ['ApiDisciplina', 'MatWebGlobals',function Cadastro(ApiDisciplina,MatWebGlobals){

    var ctrl = this;
    this.formulario = {'nome':'', 'codigo': '', 'id_departamento':''}

    this.cadastrardisciplina = function(){

      console.log("Se funfo")

      ApiDisciplina.Cadastrar(ctrl.formulario, function(data){
        ctrl.mensagem = "Cadastro de disciplina realizado com sucesso !";
        console.log("Se foi cadastrado")
      }, function(data){
        crtl.mensagem = "Erro ao cadastrar disciplina!";
        console.log("Se n foi cadastrado")
      });

      }
  }]
}).
  component ('ofertaDisciplina', {
    templateUrl: '/app/Disciplina/oferta.template.html',
    controller: ['ApiDisciplinaListar', '$uibModal', 'MatWebGlobals',function Pesquisar(ApiDisciplinaListar,$uibModal,MatWebGlobals) {
      this.nome_disciplina = "";
      this.i_departamento = "";
  var ctrl = this;
  ctrl.disciplinas = [];
      this.pesquisar = function()
      {
        ApiDisciplinaListar.Listar({id_departamento: ctrl.i_departamento , nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
              ctrl.disciplinas = resultado.corpo
      console.log(ctrl.disciplinas)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }

      this.abrir = function(){

      $uibModal.open({
      animation: 'true',
      component: 'modalDisciplina',
      size: 'lg',
      });

      }

    }]
  });