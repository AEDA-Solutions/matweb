(function () {
    'use strict';

    angular
        .module('app')

        .controller: ['ApiUsuario','$http','$location', 'MatWebGlobals',function Registrar(ApiUsuario,$http,$location,MatWebGlobals) {
      this.formulario = {'usuario':'','senha':'','email':'', 'cpf':'', };
      this.registrar = function()

        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['UserService', '$location', '$rootScope', 'FlashService'];
    function RegisterController(UserService, $location, $rootScope, FlashService) {
        var vm = this;

        vm.register = register;

        function register() {
            vm.dataLoading = true;
            UserService.Create(vm.user)
                .then(function (response) {
                    if (response.success) {
                        FlashService.Success('Registration successful', true);
                        $location.path('/login');
                    } else {
                        FlashService.Error(response.message);
                        vm.dataLoading = false;
                    }
                });
        }
    }

})();