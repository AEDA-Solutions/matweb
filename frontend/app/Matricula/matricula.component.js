angular.
  module('Matricular').
    component('detalheMatricula', {
    templateUrl: '/app/Matricula/matriculadetalhar.html',
    controller: ['ApiOfertaDetalhar', 'MatWebGlobals', '$routeParams','$scope', function Detalhar(ApiOfertaDetalhar,MatWebGlobals,$routeParams,$scope) {
        this.formulario = {'id_disciplina': $routeParams.Id_disciplina , 'pagina': 0 , 'quantidade': 1000};
        var ctrl = this;
        this.detalhar = function()
        {   
            $scope.ementa = false;
            ApiOfertaDetalhar.Detalhar(this.formulario,function(resultado) {
                ctrl.oferta = resultado.corpo;
                console.log(ctrl.oferta.turmas);
                for(var i=0, horario = null; i < ctrl.oferta.turmas.length; i++){
                    console.log(ctrl.oferta.turmas[i].horarios);
                    for(var j=0; j < ctrl.oferta.turmas[i].horarios[j]; j++) {
                        console.log(ctrl.oferta.turmas[i].horarios[j].inicio);
                        console.log(ctrl.oferta.turmas[i].horarios[j].fim);
                    }
                }
            }, function(erro) {
                ctrl.error = error.data.mensagem;
                console.log(error.data.mensagem);
            });
        }
        this.detalhar();
        
        $scope.MostraEmenta = function() {
            $scope.ementa = !$scope.ementa;
        }
    }]
}). 
  component('usuarioMatricular', {
    templateUrl: '/app/Matricula/matricula.template.html',
    controller: ['ApiOfertaDetalhar','ApiCampus','ApiDepartamentoPCampus','ApiOfertaPDepart','ApiDisciplinaCadastrar','ApiDisciplinaEditar','ApiDisciplinaDeletar','ApiOfertaDetalhar','MatWebGlobals', '$routeParams', '$scope', function Detalhar(ApiOfertaDetalhar,ApiCampus,ApiDepartamentoPCampus,ApiOfertaPDepart,ApiDisciplinaCadastrar,ApiDisciplinaEditar,ApiDisciplinaDeletar,ApiOfertaDetalhar,MatWebGlobals,$routeParams,$scope) {
        this.formulario = {'id_disciplina': $routeParams.Id_disciplina , 'pagina': 0 , 'quantidade': 1000};
        var ctrl = this;
        ctrl.disciplina = [];
        ctrl.campus = [];
        ctrl.departamento = [];
        
        ctrl.inicializa = function() {
            $scope.opcaolistar = false;
            $scope.detalhando = false;
            $scope.ementa = false;
            $scope.selecionado = false;
            $scope.listando = false;
            $scope.selecteddisciplinas = false;
        };
        
        ctrl.listarcampus = function() {
            ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
            ctrl.campus = resultado.corpo;      
            }, function(erro) {
                ctrl.error = error.data.mensagem;
            });
        };
        
        $scope.OpcaoListar = function(){
            ctrl.inicializa();
            $scope.opcaolistar = true;
            ctrl.listarcampus();
        };
        
        $scope.listdptos = function(id) {
            ctrl.inicializa();
            $scope.listando = true;
            ApiDepartamentoPCampus.Listar({id_campus: id, 'nome': '', 'pagina': 0, 'quantidade': 1000 }, function(resultado) {
                ctrl.departamentos = resultado.corpo;
            }, function(erro) {
                ctrl.error = error.data.mensagem;
            });
        };
        
        $scope.SelectDpto = function(departamento) {
            ctrl.inicializa();
            $scope.selecteddisciplinas = true;
            ApiOfertaPDepart.Listar({id_departamento: departamento.id, 'nome': '', 'pagina': 0, 'quantidade': 1000 },function(resultado) {
                ctrl.disciplinas = resultado.corpo;
            }, function(error){
                ctrl.logListar = error.data.mensagem;
            });
        };

        $scope.Gravar = function() {
            ctrl.inicializa();
            $scope.gravando = true;
            $scope.opcaolistar = true;
            ctrl.listarcampus();
        };
        
        $scope.Escolher = function() {
            ctrl.inicializa();
            $scope.opcaolistar = true;
            ctrl.listarcampus();
        };
        
        $scope.SelectDisciplina = function(disciplina) {
            ctrl.inicializa();
            $scope.selecionado = true;
            ctrl.disciplina = disciplina;
        };
        
        $scope.DetalharMatricula = function(iddisciplina) {
            $scope.detalhando = !$scope.detalhando;
            ApiOfertaDetalhar.Detalhar({'id_disciplina': iddisciplina , 'pagina': 0 , 'quantidade': 1000}   ,function(resultado) {
                ctrl.oferta = resultado.corpo;
            }, function(erro) {
                ctrl.error = error.data.mensagem;
                console.log(error.data.mensagem);
            });
        };
        
        $scope.MostraEmenta = function() {
            $scope.ementa = !$scope.ementa;
        };
        
        $scope.DefineTurma = function(turma) {
            ctrl.turmaescolhida = turma;
        };
        
        $scope.PedirMatricula = function(){
            console.log(ctrl.disciplina);
            console.log(ctrl.turmaescolhida);
            ctrl.formulario = { id_disciplina: ctrl.disciplina.id, id_usuario: window.sessionStorage.getItem('UserId'), id_turma: ctrl.turmaescolhida.id, status: "P"  };
            console.log(ctrl.formulario);
        };
    }]
});

