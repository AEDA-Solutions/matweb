angular.
   module('Departamento').
   factory('ApiDepartamento', ['$resource',
      function($resource) {
	  var methodListar = function(){
		$resource('/api/Departamento/Listar', {},
		{Listar: {method: 'POST'},
		});
	  };
	  return {
		Listar: methodListar	
	  };
}]);
