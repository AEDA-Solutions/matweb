angular.
   module('Departamento').
   factory('ApiDepartamento', ['$resource',
      function($resource) {
	  var methodListar = function($resource){
		departamentos = $resource('/api/Departamento/Listar', {},
		{Listar: {method: 'POST'},
		});
	  };
	  return {
		Listar: methodListar	
	  };
}]);
