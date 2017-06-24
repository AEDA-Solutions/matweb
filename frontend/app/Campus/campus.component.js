angular.
  module('Campus').
  component('listarCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', 'MatWebGlobals',function Entrar(ApiCampus,MatWebGlobals) {
      this.nome_campus = "";
  var ctrl = this;
  ctrl.campus = [];
        ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
            ctrl.campus = resultado.corpo;
            MatWebGlobals.campus = resultado.corpo;
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
    }]
  }).
  component('gerenciarCampus', {
    templateUrl: '/app/Campus/campus.adm.template.html',
    controller: ['ApiCampus', 'ApiCampusCadastrar', 'MatWebGlobals', '$scope', function Gerenciar(ApiCampus,ApiCampusCadastrar,MatWebGlobals,$scope) {
        var ctrl = this;
        ctrl.campus = [];
        this.formulario = { 'nome': '' };
        
        
        $scope.Listar = function() {
            $scope.listando = true;
            $scope.editando = false;
            $scope.gravando = false;
            ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
                ctrl.campus = resultado.corpo;
                MatWebGlobals.campus = resultado.corpo;
            }, function(erro){
                ctrl.erro = erro.data.mensagem
                console.log(ctrl.erro)
            } );
        };
        
        
        $scope.Gravar = function() {
            $scope.listando = false;
            $scope.editando = false;
            $scope.gravando = true;
            $scope.logCadastro = '';
            ctrl.campus.nome = '';
            ctrl.Cadastrar = function() {
                if (ctrl.formulario.nome == '' || typeof ctrl.formulario.nome === 'undefined') {
                    $scope.logCadastro = 'Nome não Preenchido';
                } else {
                    ApiCampusCadastrar.Cadastrar(ctrl.formulario,function(resultado) {
                        ctrl.campus = resultado.corpo;
                        MatWebGlobals.campus = resultado.corpo;
                        $scope.logCadastro = 'Campus Gravado Com Sucesso';
                    }, function(erro){
                        $scope.logCadastro = erro.data.mensagem;
                    });
                    $scope.logCadastro = '';
                }
            }
        };
        
        
        $scope.Editar = function() {
            $scope.listando = false;
            $scope.editando = true;
            $scope.gravando = false;
            $scope.logCadastro = '';
        }
    }]
});
