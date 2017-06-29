angular.
  module('ModalCampusNav').
  component('Campusmodalnav', {
    templateUrl: '/mw/navigation/ModalCampus/modalcampusnav.template.html',
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
