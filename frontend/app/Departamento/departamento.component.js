angular.
  module('Departamento').
  component('listarDepartamento', {
    templateUrl: '/app/Departamento/departamento.template.html',
    controller: ['ApiDepartamento', 'MatWebGlobals',function Entrar(ApiDepartamento,MatWebGlobals) {
      this.nome_departamento = "";
	var ctrl = this;
	ctrl.departamentos = [];
      this.pesquisar = function()
      {
       	ApiDepartamento.Listar({id_campus: 1 , nome: ctrl.nome_departamento, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.departamentos = resultado.corpo
			console.log(ctrl.departamentos)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  }).
  component('listarDepartpcampus', {
    templateUrl: '/app/Departamento/departPcampus.template.html',
    controller: ['ApiDepartamentoPCampus', 'MatWebGlobals', '$routeParams', function Listar(ApiDepartamentoPCampus,MatWebGlobals,$routeParams) {
        this.formulario = {id_campus: $routeParams.Id_campus , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        console.log($routeParams.Id_campus);
        var ctrl = this;
        this.listar = function()
        {
            ApiDepartamentoPCampus.Listar(this.formulario,function(resultado) {
                ctrl.departamentos = resultado.corpo;
                MatWebGlobals.departamentos = resultado.corpo;
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
    }]
}). 
component('gerenciarDepartamento', {
    templateUrl: '/app/Departamento/departamento.adm.template.html',
    controller: ['ApiDepartamentoGerenciar','ApiCampus','ApiDepartamentoPCampus', 'ApiDepartamentoCadastrar', 'MatWebGlobals', '$routeParams', '$scope', function Gerenciar(ApiDepartamentoGerenciar,ApiCampus,ApiDepartamentoPCampus,ApiDepartamentoCadastrar,MatWebGlobals,$routeParams,$scope) {
        this.formulario = {id_campus: $routeParams.Id_campus , 'nome': '', 'pagina': 0, 'quantidade': 1000 };
        var ctrl = this;
        ctrl.campus = [];
        ctrl.departamento = [];
        
        ctrl.inicializa = function() {
            $scope.opcaolistar = false;
            $scope.listando = false;
            $scope.gravando = false;
            $scope.selecionado = false;
            $scope.editando = false;
        }
        
        ctrl.listarcampus = function() {
            ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
            ctrl.campus = resultado.corpo;      
            }, function(erro) {
                ctrl.error = error.data.mensagem;
            })
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
        
        $scope.Gravar = function() {
            ctrl.inicializa();
            $scope.gravando = true;
            ApiDepartamentoPCampus.Listar({id_campus: id, 'nome': '', 'pagina': 0, 'quantidade': 1000 }, function(resultado) {
                ctrl.departamentos = resultado.corpo;
            }, function(erro) {
                ctrl.error = error.data.mensagem;
            });
        };
        
        $scope.Cadastrar = function() {
            ApiDepartamentoCadastrar.Cadastrar({id_campus: ctrl.departamento.id_campus, nome: ctrl.departamento.nome, codigo: ctrl.departamento.codigo, sigla: ctrl.departamento.sigla}, function(resultado) {
                ctrl.departamento = resultado.corpo;
                $scope.logCadastrar = "Departamento Cadastrado com Sucesso";
            }, function(erro) {
                $scope.logCadastrar = error.data.mensagem;
            });
        };
        
    }]
});

