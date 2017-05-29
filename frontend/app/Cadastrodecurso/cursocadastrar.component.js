angular.
  module('Cadastrarcurso').
  component('cadastrarCurso', {
    templateUrl: '/app/Cadastrodecurso/cadastrar.template.html',
    controller: ['ApiCurso', 'MatWebGlobals',function Registrar(ApiCurso,MatWebGlobals) {
      var ctrl = this;
      this.formulario = {'nome':'','id_campus':'','id_grau':'','codigo':'','campus':'','grau':'','permanencia_minima':'','permanencia_maxima':'','creditos_formatura':'','creditos_optativos_concentracao':'','creditos_optativos_conexa':'','creditos_livres_maximo':''};
      this.cadastrar = function()
      {
          ApiCurso.Cadastrar(ctrl.formulario,function(data){
            ctrl.mensagem = "Curso registrado com sucesso";
          },function(data){
            ctrl.mensagem = "ERRO";
          });
       };
       }]
  }); 

/*              self.id = curso.getId()
                self.nome = curso.getNome()
                self.id_campus = curso.getId_campus()
                self.id_grau = curso.getId_grau()
                self.codigo = curso.getCodigo()
                self.permanencia_minima = curso.getPermanencia_minima()
                self.permanencia_maxima = curso.getPermanencia_maxima()
                self.creditos_formatura = curso.getCreditos_formatura()
                self.creditos_optativos_concentracao = curso.getCreditos_optativos_concentracao()
                self.creditos_optativos_conexa = curso.getCreditos_optativos_conexa()
                self.creditos_livres_maximo = curso.getCreditos_livres_maximo() */