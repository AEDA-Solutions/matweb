angular.
  module('Cadastrarusuario').
  component('registrarUsuario', {
    templateUrl: '/app/Cadastraraluno/cadastraraluno.template1.html',
    controller: ['ApiUsuarioCadastrar','$http','$location', 'MatWebGlobals',function(ApiUsuarioCadastrar,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario ={'nome':'','matricula':'','cpf':'','perfil':'','email':'','sexo':'','nome_pai':'','nome_mae':'','ano_conclusao':'','identidade':'','senha':''};
      this.cadastrar = function()
      {
          ApiUsuarioCadastrar.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Usuário cadastrado com sucesso";
          
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
}). 
  component('usuarioEditar', {
    templateUrl: '/app/Cadastraraluno/cadastraraluno.template.html',
    controller: ['ApiUsuarioEditar','ApiUsuarioDeletar','$http','$location', 'MatWebGlobals',function(ApiUsuarioEditar,ApiUsuarioDeletar,$http,$location,MatWebGlobals) {
      var ctrl = this;
      this.formulario = MatWebGlobals.editUser;
      console.log(ctrl.usuario.nome);
    }]
});
  