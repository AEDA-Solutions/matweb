angular.
  module('CampusModal').
  component('modalCampus', {
    templateUrl: '/app/ModalCampus/modalCampus.template.html',
    bindings: {
    dismiss: '&'
    }, 
    controller: [ 'MatWebGlobals',function (MatWebGlobals) {
    this.id = "";
    id = MatWebGlobals.campus.id
    var ctrl = this;

    ctrl.cancel = function () {
      ctrl.dismiss({$value: 'cancel'});
    };
  }]
});

