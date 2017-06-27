angular.
  module('Curso').
  component('listarCurso', {
    templateUrl: '/app/Curso/curso.template.html',
    controller: ['ApiCurso', 'MatWebGlobals',function (ApiCurso,MatWebGlobals) {
      console.log(ApiCurso.Listar);
	    this.nome_curso = "";
	var ctrl = this;
	ctrl.cursos = [];
      this.pesquisar = function()
      {
       	ApiCurso.Listar({id_campus: 1, id_grau: 1, nome: ctrl.nome_curso, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.cursos = resultado.corpo
      console.log(ctrl.cursos)
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
      }
    }]
  })
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
