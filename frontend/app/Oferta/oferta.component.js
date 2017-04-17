angular.
  module('Oferta').
  component('ofertaCursos', {
    templateUrl: '/app/Oferta/oferta.template.html',
    controller: ['ApiOferta', 'MatWebGlobals',function Entrar(ApiOferta,MatWebGlobals) {
      this.nome_disciplina = "";
	var ctrl = this;
	ctrl.disciplinas = [{id: "1",nome:"Biscoioto"}];
      this.pesquisar = function()
      {
       	ApiOferta.Listar({id_departamento: 95 , nome: this.nome_disciplina, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.disciplinas = resultado.corpo
			console.log(ctrl.disciplinas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
