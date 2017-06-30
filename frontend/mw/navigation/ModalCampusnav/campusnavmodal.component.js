angular.
  module('CampusModalnav').
  component('modalCampusnav', {
    templateUrl: '/mw/navigation/ModalCampusnav/campusnavmodal.template.html',
    bindings: {
    }, 
    controller: [ 'MatWebGlobals',function (MatWebGlobals) {
    var ctrl = this;
    ctrl.inter = "";

     ctrl.inter = MatWebGlobals.Id ;
     console.log(ctrl.inter)
  }]
});