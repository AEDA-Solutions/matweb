angular.
  module('Disciplina').
  component('ofertaDisciplina', {
    templateUrl: '/app/Disciplina/oferta.template.html',
    controller: ['ApiDisciplina',function List(ApiDisciplina) {
      this.nome_disciplina = "";
      this.i_departamento = "";
	var ctrl = this;
	ctrl.disciplinas = [];
      this.pesquisar = function()
      {
       	ApiDisciplina.Listar({id_departamento: ctrl.i_departamento , nome: ctrl.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.disciplinas = resultado.corpo
			console.log(ctrl.disciplinas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });