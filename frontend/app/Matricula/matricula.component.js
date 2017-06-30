angular.
  module('Matricular').
  component('usuarioMatricular', {
    templateUrl: '/app/Matricular/matricula.template.html',
    controller: ['ApiMatricular','ApiCampus','ApiDepartamentoPCampus','ApiOfertaPDepart', '$http','$location','MatWebGlobals','$scope',function(ApiMatricular,ApiCampus,ApiDepartamentoPCampus,ApiOfertaPDepart,$http,$location,MatWebGlobals,$scope) {
      var ctrl = this;
      
      ctrl.inicializa = function() {
          $scope.escolhacampus = false;
          $scope.escolhadepartamento = false;
          $scope.escolhadisciplina = false;
          $scope.escolhaturma= false;
      };
      
      ApiCampus.Listar({ nome: "", pagina: 0, quantidade: 1000 },function(resultado) {
            ctrl.inicializa();
            $scope.escolhacampus = true;
            ctrl.campus = resultado.corpo;
            MatWebGlobals.campus = resultado.corpo;
    }, function(erro){
        ctrl.erro = erro.data.mensagem
      console.log(ctrl.erro)
      } );
    
      $scope.VerificarDepartamentos = function(idcampus) {
          ctrl.inicializa();
          $scope.escolhadepartamento=true;
          ApiDepartamentoPCampus.Listar({id_campus: idcampus , 'nome': '', 'pagina': 0, 'quantidade': 1000} ,function(resultado) {
                ctrl.departamentos = resultado.corpo;
            }, function(error){
                ctrl.error = error.data.mensagem;
            });
      };
        
      $scope.VericiarDisciplinas = function(iddepartamento) {
          ctrl.inicializa();
          $scope.escolhadisciplina=true;
          ApiOfertaPDepart.Listar({id_departamento: iddepartamento , 'nome': '', 'pagina': 0, 'quantidade': 1000} ,function(resultado) {
                ctrl.disciplinas = resultado.corpo;
            }, function(error){
                ctrl.error = error.data.mensagem;
            });
      };
        
      $scope.VerificarTurmas = function(iddisciplina) {
          ctr.inicializa();
          $scope.escolhaturma = true;
          ApiOfertaDetalhar.Detalhar({'id_disciplina': iddisciplina, 'pagina': 0 , 'quantidade': 1000 } ,function(resultado) {
                ctrl.oferta = resultado.corpo;
                for(var i=0, horario = null; i < ctrl.oferta.turmas.length; i++){
                    console.log(ctrl.oferta.turmas[i].horarios);
                    for(var j=0; j < ctrl.oferta.turmas[i].horarios[j]; j++) {
                        console.log(ctrl.oferta.turmas[i].horarios[j].inicio);
                        console.log(ctrl.oferta.turmas[i].horarios[j].fim);
                    }
                }
            }, function(erro) {
                ctrl.error = error.data.mensagem;
            });
      };
      
      this.cadastrar = function()
      {
          ApiMatricular.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Matricula feita com Sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
    };
    }]
});
