angular.
  module('Disciplina').
  component('ofertaDisciplina', {
    templateUrl: '/app/Disciplina/oferta.template.html',
    controller: ['ApiDisciplina', 'MatWebGlobals',function Entrar(ApiDisciplina,MatWebGlobals) {
      this.nome_disciplina = "";
	var ctrl = this;
	ctrl.disciplinas = [];
      this.pesquisar = function()
      {
       	ApiDisciplina.Listar({id_departamento: 95 , nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.disciplinas = resultado.corpo
			console.log(ctrl.disciplinas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
