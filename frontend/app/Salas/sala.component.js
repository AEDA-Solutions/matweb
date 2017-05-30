angular.
  module('Sala').
  component('listarSalas', {
    templateUrl: '/app/Salas/sala.template.html',
    controller: ['ApiSalas', 'MatWebGlobals',function Entrar(ApiSalas,MatWebGlobals) {
      this.nome_sala = "";
	var ctrl = this;
	ctrl.salas = [];
      this.pesquisar = function()
      {
       	ApiSalas.Listar({'id_predio':'','codigo':'', pagina: 0, quantidade: 1000 },function(resultado) {
		          ctrl.salas = resultado.corpo
			console.log(ctrl.salas)
		}, function(erro){
   			ctrl.erro = erro.data.mensagem
			console.log(ctrl.erro)
   		} );
   	  }
    }]
  });
