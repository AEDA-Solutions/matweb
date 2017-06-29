angular.
  module('CampusModalnav').
  component('modalCampusnav', {
    templateUrl: '/mw/navigation/ModalCampus/campusnavmodal.template.html',
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