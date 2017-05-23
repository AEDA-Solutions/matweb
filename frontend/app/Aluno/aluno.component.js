angular.
  module('Aluno').
  component('alunoRegistrar', {
    templateUrl: '/app/Aluno/aluno.template.html',
    controller: ['ApiAluno','$http','$location', 'MatWebGlobals',function Registrar(ApiAluno,$http,$location,MatWebGlobals) {
      var ctrl = this;

      this.formulario = {'nome':'','matricula':'','cpf':'','identidade':'','email':'','sexo':'','uf':'','nivel':'','conclusao':'','nome_pai':'','nome_mae':'','senha':'','cep':'','complemento':'','numero_telefone':'','numero_lote':'','id_raca_cor':'','
      ,'ano_conclusao':'','tipo_escola':''};
      this.cadastrar = function()
      {
          ApiAluno.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
      } );
      }
    }]
  });
