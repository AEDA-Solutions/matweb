angular.
  module('Matricular').
  component('usuarioMatricular', {
    templateUrl: '/app/Matricula/matricula.template.html',
    controller: ['ApiOfertaDetalhar','ApiCampus','ApiDepartamentoPCampus','ApiOfertaPDepart','ApiDisciplinaCadastrar','ApiDisciplinaEditar','ApiDisciplinaDeletar', 'MatWebGlobals', '$routeParams', '$scope', function Detalhar(ApiOfertaDetalhar,ApiCampus,ApiDepartamentoPCampus,ApiOfertaPDepart,ApiDisciplinaCadastrar,ApiDisciplinaEditar,ApiDisciplinaDeletar,MatWebGlobals,$routeParams,$scope) {
        this.formulario = {'id_disciplina': $routeParams.Id_disciplina , 'pagina': 0 , 'quantidade': 1000};
        var ctrl = this;
        ctrl.disciplina = [];
        ctrl.campus = [];
        ctrl.departamento = [];
        
        ctrl.inicializa = function() {
            $scope.opcaolistar = false;
            $scope.listando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
            $scope.editando = false;
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
            $scope.opcaolistar = false;
            $scope.listando = true;
            ApiDepartamentoPCampus.Listar({id_campus: id, 'nome': '', 'pagina': 0, 'quantidade': 1000 }, function(resultado) {
                ctrl.departamentos = resultado.corpo;
            }, function(erro) {
                ctrl.error = error.data.mensagem;
            });
        };
        
        $scope.SelectDpto = function(departamento) {
            ctrl.departamento = departamento;
            if ($scope.gravando == true) {
                $scope.listando = false;
                $scope.selecionado = true;
            } else if ($scope.editando == true ){
                $scope.selecteddisciplinas = true;
                $scope.listando = false;
            } else {
                ctrl.inicializa();
                $scope.selecteddisciplinas = true;
            };
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
        
        $scope.Cadastrar = function() {
            ApiDisciplinaCadastrar.Cadastrar({ 'id': 1, 'id_disciplina': ctrl.disciplina.id, 'id_usuario': ctrl.usuario.id, 'status': 'Pedido Enviado' }, function(resultado) {
                ctrl.disciplina = [];
                $scope.logCadastrar = "Disciplina Cadastrada com Sucesso";
            }, function(erro) {
                $scope.logCadastrar = error.data.mensagem;
            });
        };
        
        $scope.Escolher = function() {
            ctrl.inicializa();
            $scope.opcaolistar = true;
            $scope.editando = true;
            ctrl.listarcampus();
        }
        
        $scope.SelectDisciplina = function(disciplina) {
            ctrl.disciplina = disciplina;
            $scope.selecteddisciplinas = false;
            $scope.selecionado = true;
        }
        
        $scope.AlterDisciplina = function() {
            ApiDisciplinaEditar.Editar({'id':ctrl.disciplina.id, 'id_departamento':ctrl.departamento.id, 'nome':ctrl.disciplina.nome, 'codigo':ctrl.disciplina.codigo, 'creditos':ctrl.disciplina.creditos}, function(resultado) {
                $scope.logEditar = "Disciplina Alterada com Sucesso";
                ctrl.disciplina = [];
            }, function(erro) {
                $scope.logEditar = error.data.mensagem;
            });
        };
        
        $scope.DelDisciplina = function() {
            ApiDisciplinaDeletar.Deletar({'id':ctrl.disciplina.id}, function(resultado) {
                $scope.logEditar = "Disciplina Apagada com Sucesso";
                ctrl.disciplina = [];
            }, function(erro) {
                $scope.logEditar = error.data.mensagem;
            });
        };
    }]
});
