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
  });