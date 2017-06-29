angular.
  module('Campus').
  component('listarCampus', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCampus', 'MatWebGlobals','$scope',function Entrar(ApiCampus,MatWebGlobals,$scope) {
        this.nome_campus = "";
        var ctrl = this;
        ctrl.campus = [];
        $scope.listcurso = false;
        ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
            ctrl.campus = resultado.corpo;
            MatWebGlobals.campus = resultado.corpo;
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
    }]
  }).
  angular.
  module('CampusNav').
  component('sexoCampus', {
    templateUrl: '/app/Campus/campus-nav.template.html',
    controller: ['ApiCampusSex', 'MatWebGlobals','$scope',function Entrar(ApiCampusSex,MatWebGlobals,$scope) {
        this.nome_campus = "";
        var ctrl = this;
        ctrl.campus = [];
        $scope.listcurso = false;
        ApiCampusSex.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
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
    controller: ['ApiCampus', 'ApiCampusCadastrar', 'ApiCampusEditar', 'ApiCampusDeletar', 'MatWebGlobals', '$scope', '$location', function Gerenciar(ApiCampus,ApiCampusCadastrar,ApiCampusEditar,ApiCampusDeletar,MatWebGlobals,$scope,$location) {
        if (window.sessionStorage.getItem('UserProfile') != 'Admin') {
            $location.path('/');
        }
        var ctrl = this;
        ctrl.campus = [];
        this.formulario = { 'nome': '' };
        
        
        $scope.Listar = function() {
            $scope.listando = true;
            $scope.editando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
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
            $scope.selecionado = false;
            $scope.logCadastro = '';
            ctrl.campus.nome = '';
            ctrl.formulario.nome = '';
            ctrl.Cadastrar = function() {
                if (ctrl.formulario.nome == '' || typeof ctrl.formulario.nome === 'undefined') {
                    $scope.logCadastro = 'Nome não Preenchido';
                } else {
                    ApiCampusCadastrar.Cadastrar(ctrl.formulario,function(resultado) {
                        ctrl.campus = [];
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
            $scope.selecionado = false;
            $scope.logEdicao = '';
            ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
                ctrl.campus = resultado.corpo;
                MatWebGlobals.campus = resultado.corpo;
            }, function(erro){
                $scope.logEdicao = erro.data.mensagem;
            } );
        };
    
        
        $scope.Selecionar = function(campus) {
            ctrl.campus = campus;
            console.log(campus);
            $scope.editando = false;
            $scope.selecionado = true;
        };
        
        $scope.Update = function() {
            ApiCampusEditar.Editar({ nome: ctrl.campus.nome, id: ctrl.campus.id},function(resultado) {
                $scope.logEdicao = 'Alteração Realizada com Sucesso';
                ctrl.campus = [];
            }, function(erro) {
                $scope.logEdicao = erro.data.mensagem;
            });
        }
        
        $scope.Deletar = function() {
            ApiCampusDeletar.Deletar({ id: ctrl.campus.id },function(resultado) {
                $scope.logEdicao = 'Exclusão Realizada com Sucesso';
                ctrl.campus = [];
            }, function(erro) {
                $scope.logEdicao = erro.data.mensagem; 
            });
        }
        
        console.log($scope);
    }]
});
