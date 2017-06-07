angular.
  module('Predio').
  component('listarPredio', {
    templateUrl: '/app/Predio/predio.template.html',
    controller: ['ApiPredio', 'MatWebGlobals',function Entrar(ApiPredio,MatWebGlobals) {
      this.nome_predio = "";
	var ctrl = this;
	ctrl.predios = [];
      this.pesquisar = function()
      {
       	ApiPredio.Listar({id_campus: 1, nome: ctrl.nome_predio, pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.predios = resultado.corpo
			console.log(ctrl.predios)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
