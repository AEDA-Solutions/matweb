angular.
  module('Cadastrarusuario').
  component('registrarUsuario', {
    templateUrl: '/app/Cadastraraluno/cadastraraluno.template.html',
    controller: ['ApiUsuarioCadastrar','$http','$location', 'MatWebGlobals',function(ApiUsuarioCadastrar,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','matricula':'','cpf':'','perfil':'','senha':'','identidade':'','email':'','ano_conclusao':'','nome_pai':'','nome_mae':''};
      this.cadastrar = function()
      {
          ApiUsuarioCadastrar.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Aluno cadastrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});