angular.
  module('Usuario').
  component('gerenciarUsuario', {
    templateUrl: '/app/Usuario/usuario.adm.template.html',
    controller: ['ApiUsuarioListar','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiUsuarioListar,$http,$location,MatWebGlobals,$scope) {
        var ctrl = this;
        ctrl.usuarios = [];
        this.formulario = { 'usuario': '' };
        
        $scope.OpcaoListar = function(){
            $scope.opcaolistar = true;
            ctrl.logListar = '';
        };
        
        $scope.Listar = function(){
            $scope.listando = true;
            $scope.opcaolistar = false;
            $scope.editando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
            ctrl.logListar = '';
            if ( ctrl.formulario.usuario = '' || typeof ctrl.formulario.usuario === 'undefined' ) {
                $scope.logListar = 'Critério de Pesquisa não Preenchido';
            } else {
            ApiUsuarioListar.Listar({ usuario: ctrl.formulario.usuario},function(resultado) {
                ctrl.usuarios = resultado.corpo;
            }, function(erro) {
                ctrl.logListar = erro.data.mensagem;
            });
            };
        };
    }]
});



 