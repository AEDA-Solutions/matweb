angular.
  module('Oferta').
  component('ofertaDisciplina', {
    templateUrl: '/app/Oferta/oferta.template.html',
    controller: ['ApiOferta', 'MatWebGlobals',function Entrar(ApiOferta,MatWebGlobals) {
      this.nome_disciplina = "";
	var ctrl = this;
	ctrl.disciplinas = [];
      this.pesquisar = function()
      {
       	ApiOferta.Listar({id_departamento: 95, nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.disciplinas = resultado.corpo
			console.log(ctrl.disciplinas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  }).
 component('testDiscpdepart',{
    templateUrl: '/app/Oferta/test.template.html',
    controller: ['ApiOfertaPDepart', 'MatWebGlobals', '$routeParams', function Listar(ApiOfertaPDepart,MatWebGlobals,$routeParams) {
        this.formulario = {'id_departamento': $routeParams.Id_departamento , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        var ctrl = this;
        this.listar = function()
        {
            ApiOfertaPDepart.Listar(this.formulario,function(resultado) {
                ctrl.disciplinas = resultado.corpo;
                for(var i = 0, depart = null; i < MatWebGlobals.departamentos.length; i++) {
                    if (MatWebGlobals.departamentos[i].id == $routeParams.Id_departamento) {
                        depart = MatWebGlobals.departamentos[i];
                        break;
                    }
                };
                ctrl.departamento_nome = depart.nome;
                console.log(ctrl.departamento_nome);
            }, function(error){
                ctrl.error = error.data.mensagem;
            });
        }
        this.listar();
    }]
}).
  component('ofertaDiscpdepart',{
    templateUrl: '/app/Oferta/oferta.template2.html',
    controller: ['ApiOfertaPDepart', 'MatWebGlobals', '$routeParams', function Listar(ApiOfertaPDepart,MatWebGlobals,$routeParams) {
        this.formulario = {'id_departamento': $routeParams.Id_departamento , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        var ctrl = this;
        this.listar = function()
        {
            ApiOfertaPDepart.Listar(this.formulario,function(resultado) {
                ctrl.disciplinas = resultado.corpo;
                for(var i = 0, depart = null; i < MatWebGlobals.departamentos.length; i++) {
                    if (MatWebGlobals.departamentos[i].id == $routeParams.Id_departamento) {
                        depart = MatWebGlobals.departamentos[i];
                        break;
                    }
                };
                ctrl.departamento_nome = depart.nome;
                console.log(ctrl.departamento_nome);
            }, function(error){
                ctrl.error = error.data.mensagem;
            });
        }
        this.listar();
    }]
}).
  component('ofertaDetalhar', {
    templateUrl: '/app/Oferta/oferta.template3.html',
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
component('gerenciarDisciplina', {
    templateUrl: '/app/Oferta/disciplina.adm.template.html',
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
            ApiDisciplinaCadastrar.Cadastrar({ 'id_departamento': ctrl.departamento.id, 'nome': ctrl.disciplina.nome, 'codigo': ctrl.disciplina.codigo, 'creditos': ctrl.disciplina.creditos }, function(resultado) {
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
