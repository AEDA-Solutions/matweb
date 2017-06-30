angular.
  module('CampusModal').
  component('modalCampus', {
    templateUrl: '/app/ModalCampus/modalCampus.template.html',
    bindings: {
    dismiss: '&'
    }, 
   controller: [ 'MatWebGlobals',function (MatWebGlobals) {
    var ctrl = this;
    ctrl.inter = "";

    ctrl.cancel = function () {
      ctrl.dismiss({$value: 'cancel'});
    };

     ctrl.inter = MatWebGlobals.Id ;
     console.log(ctrl.inter)
  }]
});