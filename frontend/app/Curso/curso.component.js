angular.
  module('Curso').
  component('listarCurso', {
    templateUrl: '/app/Campus/campus.template.html',
    controller: ['ApiCurso','ApiCampus','MatWebGlobals','$scope',function (ApiCurso,ApiCampus,MatWebGlobals,$scope) {
        $scope.listcurso = true;
        this.nome_curso = "";
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
   component('cursoPcampus', {
    templateUrl: '/app/Curso/curso.template.html',
    controller: ['ApiCursoPCampus', 'MatWebGlobals', '$routeParams','$scope', function            Listar(ApiCursoPCampus,MatWebGlobals,$routeParams,$scope) {
        this.formulario = {id_campus: $routeParams.Id_campus , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        var ctrl = this;
        this.listar = function()
        {
            $scope.listacursos = true;
            $scope.detalhescurso = false;
            ApiCursoPCampus.Listar(this.formulario,function(resultado) {
                ctrl.cursos = resultado.corpo;
                MatWebGlobals.cursos = resultado.corpo;
                for(var i = 0, campi = null; i < MatWebGlobals.campus.length; i++) {
                    if (MatWebGlobals.campus[i].id == $routeParams.Id_campus) {
                        campi = MatWebGlobals.campus[i];
                        break;
                    }
                };
                ctrl.campus_nome = campi.nome;
                console.log(ctrl.campus_nome);
            }, function(error){
                ctrl.error = error.data.mensagem;
            });
        }
        this.listar();
        
        $scope.detalhar = function(curso) {
            $scope.listacursos = false;
            $scope.detalhescurso = true;
            $scope.tabelaCurriculo = false;
            $scope.tabelaFluxo = false;
            console.log(curso);
            ctrl.curso = curso;
        };
        
        this.botaoFluxo =  function() {
            if ($scope.tabelaCurriculo == true ) {
                $scope.tabelaCurriculo = false;
            };
            $scope.tabelaFluxo = !$scope.tabelaFluxo;
        };
        
        this.botaoCurriculo =  function() {
            if ($scope.tabelaFluxo == true ) {
                $scope.tabelaFluxo = false;
            };
            $scope.tabelaCurriculo = !$scope.tabelaCurriculo;
        }; 
        
        $scope.Fluxo = function() {
            this.botaoFluxo();
        };
        
        $scope.Curriculo = function() {
            this.botaoCurriculo();
        };
    }]
}).
    component('gerenciarCurso', {
    templateUrl: '/app/Campus/curso.adm.template.html',
    controller: ['ApiCurso', 'ApiCursoCadastrar', 'ApiCursoEditar', 'ApiCursoDeletar', 'MatWebGlobals', '$scope', '$location', function Gerenciar(ApiCurso,ApiCursoCadastrar,ApiCursoEditar,ApiCursoDeletar,MatWebGlobals,$scope,$location) {
        if (window.sessionStorage.getItem('UserProfile') != 'Admin') {
            $location.path('/');
        }
        var ctrl = this;
        ctrl.curso = [];
        this.formulario = { 'nome': '' };
        
        
        $scope.Listar = function() {
            $scope.listando = true;
            $scope.editando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
            ApiCurso.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
                ctrl.curso = resultado.corpo;
                MatWebGlobals.curso = resultado.corpo;
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
            ctrl.curso.nome = '';
            ctrl.formulario.nome = '';
            ctrl.Cadastrar = function() {
                if (ctrl.formulario.nome == '' || typeof ctrl.formulario.nome === 'undefined') {
                    $scope.logCadastro = 'Nome não Preenchido';
                } else {
                    ApiCursoCadastrar.Cadastrar(ctrl.formulario,function(resultado) {
                        ctrl.cursos = [];
                        MatWebGlobals.cursos = resultado.corpo;
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
                ctrl.cursos = resultado.corpo;
                MatWebGlobals.cursos = resultado.corpo;
            }, function(erro){
                $scope.logEdicao = erro.data.mensagem;
            } );
        };
    
        
        $scope.Selecionar = function(curso) {
            ctrl.cursos = cursos;
            console.log(curso);
            $scope.editando = false;
            $scope.selecionado = true;
        };
        
        $scope.Update = function() {
            ApiCursoEditar.Editar({ nome: ctrl.curso.nome, id: ctrl.curso.id},function(resultado) {
                $scope.logEdicao = 'Alteração Realizada com Sucesso';
                ctrl.cursos = [];
            }, function(erro) {
                $scope.logEdicao = erro.data.mensagem;
            });
        }
        
        $scope.Deletar = function() {
            ApiCursoDeletar.Deletar({ id: ctrl.curso.id },function(resultado) {
                $scope.logEdicao = 'Exclusão Realizada com Sucesso';
                ctrl.cursos = [];
            }, function(erro) {
                $scope.logEdicao = erro.data.mensagem; 
            });
        }
        
        console.log($scope);
    }]
});
