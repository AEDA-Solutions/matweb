angular.
  module('Usuario').
  component('gerenciarUsuario', {
    templateUrl: '/app/Usuario/usuario.adm.template.html',
    controller: ['ApiUsuarioListar','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiUsuarioListar,$http,$location,MatWebGlobals,$scope) {
        var ctrl = this;
        ctrl.usuarios = [];
        
        $scope.OpcaoListar = function(){
            ctrl.formulario = { 'usuario': ''};
            $scope.opcaolistar = true;
            $scope.listando = false;
            $scope.logListar = '';
        };
        
        $scope.Listar = function(){
            $scope.listando = true;
            $scope.opcaolistar = false;
            $scope.editando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
            ctrl.logListar = '';
            if ( ctrl.formulario.usuario == '' || typeof ctrl.formulario.usuario === 'undefined' ) {
                $scope.logListar = 'Critério de Pesquisa não Preenchido';
                console.log('cheguei aqui');
                $scope.opcaolistar = true;
                $scope.listando = false;
            } else {
            ApiUsuarioListar.Listar({ usuario: ctrl.formulario.usuario},function(resultado) {
                console.log('vou pesquisar por ',ctrl.formulario.usuario);
                ctrl.usuarios = resultado.corpo;
                if (ctrl.usuarios.length == 0){
                    $scope.logListar = 'Nenhum Usuário Encontrado';
                }
            }, function(erro) {
                $scope.logListar = erro.data.mensagem;
            });
            };
        };
        
       $scope.Gravar = function() {
            $scope.listando = false;
            $scope.opcaolistar = false;
            $scope.editando = false;
            $scope.gravando = true;
            $scope.selecionado = false;
        }; 
        
    }]
});



 