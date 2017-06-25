angular.
  module('Cadastrarusuario').
  component('registrarUsuario', {
    templateUrl: '/app/Cadastraraluno/cadastraraluno.template1.html',
    controller: ['ApiUsuarioCadastrar','$http','$location', 'MatWebGlobals',function(ApiUsuarioCadastrar,$http,$location,MatWebGlobals) {
      if (window.sessionStorage.getItem('UserProfile') != 'Admin') {
            $location.path('/');
      }
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
    controller: ['ApiUsuarioEditar','ApiUsuarioDeletar','$http','$location','$scope', 'MatWebGlobals',function(ApiUsuarioEditar,ApiUsuarioDeletar,$http,$location,$scope,MatWebGlobals) {
        if (window.sessionStorage.getItem('UserProfile') != 'Admin') {
            $location.path('/');
        }
      var ctrl = this;
      ctrl.usuario = MatWebGlobals.editUser;
      
      ctrl.setformulario = function(usuario) {
          ctrl.formulario = {'nome': usuario.nome, 'matricula': usuario.matricula, 'cpf': usuario.cpf, 'perfil': usuario.perfil, 'email': usuario.email, 'sexo': usuario.sexo, 'nome_pai': usuario.nome_pai, 'nome_mae': usuario.nome_mae, 'ano_conclusao': usuario.ano_conclusao, 'identidade':usuario.identidade, 'senha': usuario.senha, 'id': usuario.id};
      };
        
      $scope.Alterar = function() {
          ctrl.setformulario(ctrl.usuario);
          ApiUsuarioEditar.Editar(ctrl.formulario, function(resultado) {
              $scope.logEditar = 'Usuário Alterado Com Sucesso';
          }, function(erro) {
              $scope.logEditar = erro.data.mensagem;
          })
        
      };
        
      $scope.Apagar = function() {
          ApiUsuarioDeletar.Deletar({ 'id': ctrl.usuario.id }, function(resultado) {
              $scope.logEditar = resultado.corpo;
          }, function(erro) {
              $scope.logEditar = erro.data.mensagem;
          })
        
      };
    }]
});
  