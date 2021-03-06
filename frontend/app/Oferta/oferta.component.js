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
}).
  component('ofertaDetalhar', {
    templateUrl: '/app/Oferta/oferta.template3.html',
    controller: ['ApiOfertaDetalhar', 'MatWebGlobals', '$routeParams', function Detalhar(ApiOfertaDetalhar,MatWebGlobals,$routeParams) {
        this.formulario = {'id_disciplina': $routeParams.Id_disciplina , 'pagina': 0 , 'quantidade': 1000};
        var ctrl = this;
        this.detalhar = function()
        {
            ApiOfertaDetalhar.Detalhar(this.formulario,function(resultado) {
                ctrl.oferta = resultado.corpo;
                console.log(ctrl.oferta.turmas);
                for(var i=0, horario = null; i < ctrl.oferta.turmas.length; i++){
                    console.log(ctrl.oferta.turmas[i].horarios);
                    for(var j=0; j < ctrl.oferta.turmas[i].horarios[j]; j++) {
                        console.log(ctrl.oferta.turmas[i].horarios[j].inicio);
                        console.log(ctrl.oferta.turmas[i].horarios[j].fim);
                    }
                }
            }, function(erro) {
                ctrl.error = error.data.mensagem;
                console.log(error.data.mensagem);
            });
        }
        this.detalhar();
    }]
});
