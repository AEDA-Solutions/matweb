angular.
  module('Curso').
  component('listarCurso', {
    templateUrl: '/app/Curso/curso.template.html',
    controller: ['ApiCurso', 'MatWebGlobals',function Entrar(ApiCurso,MatWebGlobals) {
      this.nome_curso = "";
	var ctrl = this;
	ctrl.cursos = [];
      this.pesquisar = function()
      {
       	ApiCurso.Listar({nome: ctrl.nome_curso, id_campus: 1 ,id_grau: 1 , pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.cursos = resultado.corpo
			console.log(ctrl.cursos)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
