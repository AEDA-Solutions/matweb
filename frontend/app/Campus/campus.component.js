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
            ctrl.Cadastrar = function() {
                if (ctrl.formulario.nome == '' || typeof ctrl.formulario.nome === 'undefined') {
                    $scope.erro = 'Nome não Preenchido';
                } else {
                    ApiCampusCadastrar.Cadastrar(ctrl.formulario,function(resultado) {
                        ctrl.campus = resultado.corpo;
                        MatWebGlobals.campus = resultado.corpo;
                    }, function(erro){
                        $scope.erro = erro.data.mensagem;
                        console.log($scope.erro);
                    });
                    $scope.erro = '';
                    console.log('cheguei aqui');
                    console.log(ctrl.formulario);
                }
            }
            console.log()
        }
    }]
});
