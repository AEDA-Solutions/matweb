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
    ctrl.bol = false;

     ctrl.inter = MatWebGlobals.Id ;
     console.log(ctrl.inter)

     if(inter > 0){

      bol = true;
     }

      ctrl.cancel = function () {
      ctrl.dismiss({$value: bol});
      };
      
  }]
});