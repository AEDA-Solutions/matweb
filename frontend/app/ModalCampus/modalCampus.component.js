angular.
  module('CampusModal').
  component('modalCampus', {
    templateUrl: '/app/ModalCampus/modalCampus.template.html',
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