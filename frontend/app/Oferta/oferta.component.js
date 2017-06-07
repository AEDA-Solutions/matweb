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
});
