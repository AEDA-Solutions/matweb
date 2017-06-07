angular.
  module('DisciplinaModal').
  component('modalDisciplina', {
    templateUrl: '/app/ModalDisciplina/modal.template.html',
    bindings: {
    dismiss: '&'
    }, 
    controller: function () {
    var ctrl = this;

    ctrl.cancel = function () {
      ctrl.dismiss({$value: 'cancel'});
    };
  }
});