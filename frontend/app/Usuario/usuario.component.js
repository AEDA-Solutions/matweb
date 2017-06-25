angular.
  module('Usuario').
  component('gerenciarUsuario', {
    templateUrl: '/app/Usuario/usuario.adm.template.html',
    controller: ['ApiUsuarioListar','$http','$location', 'MatWebGlobals', '$scope',function Entrar(ApiUsuarioListar,$http,$location,MatWebGlobals,$scope) {
        var ctrl = this;
        ctrl.usuarios = [];
        
        ctrl.inicializa = function() {
            $scope.opcaolistar = false;
            $scope.listando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
            $scope.editando = false;
        }
        
        $scope.OpcaoListar = function(){
            ctrl.inicializa();
            ctrl.ListaParams ();
        };
        
        ctrl.ListaParams = function(){
            ctrl.formulario = { 'usuario': ''};
            $scope.opcaolistar = true;
            $scope.logListar = '';
        };
        
        $scope.Listar = function(){
            $scope.listando = true;
            $scope.opcaolistar = false;
            ctrl.logListar = '';
            if ( ctrl.formulario.usuario == '' || typeof ctrl.formulario.usuario === 'undefined' ) {
                $scope.logListar = 'Critério de Pesquisa não Preenchido';
                console.log('cheguei aqui');
                $scope.opcaolistar = true;
                $scope.listando = false;
            } else {
            ApiUsuarioListar.Listar({ usuario: ctrl.formulario.usuario},function(resultado) {
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
            ctrl.inicializa();
            console.log('cheguei aqui');
            $scope.gravando = true;
        }; 
        
        $scope.Escolher = function() {
            $scope.editando = true;
            $scope.selecionando = true;
            ctrl.ListaParams();
        }
        
    }]
});



 