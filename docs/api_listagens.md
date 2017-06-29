URL: /api/Campus/Listar
Função: Listar os campus, se o parametro nome não é informado, lista todos
PEDIDO:

{
	"nome": "#Nome do Campus#",
	"pagina": "#Numero da Página#",
	"quantidade": "#Quantidade de campus por página#"
}

RESPOSTA EM CASO DE SUCESSO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": 	
		[
			{
				"id" : "#ID do Campus 1#",
				"nome" : "#Nome do Campus 1#"
			},
			{
				"id" : "#ID do Campus 2#",
				"nome" : "#Nome do Campus 2#"
			},
			{
				"id" : "#ID do Campus 3#",
				"nome" : "#Nome do Campus 3#"
			},
			{
				"id" : "#ID do Campus 4#",
				"nome" : "#Nome do Campus 4#"
			}
			...
		]
}

RESPOSTA EM CASO DE NADA ENCONTRADO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": []
}

URL: /api/Departamento/Listar
Função: Listar os departamentos de um campos, se o parametro nome não é informado, lista todos
PEDIDO:

{
	"id_campus" : "#ID do Campus, obtido com o metodo anterior#",
	"nome": "#Nome do Campus#",
	"pagina": "#Numero da Página#",
	"quantidade": "#Quantidade de campus por página#"
}

RESPOSTA EM CASO DE SUCESSO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": 	
		[
			{
				"id" : "#ID do Departamento 1#",
				"nome" : "#Nome do Departamento 1#"
			},
			{
				"id" : "#ID do Departamento 2#",
				"nome" : "#Nome do Departamento 2#"			
			},
			{
				"id" : "#ID do Departamento 3#",
				"nome" : "#Nome do Departamento 3#"			
			},
			{
				"id" : "#ID do Departamento 4#",
				"nome" : "#Nome do Departamento 4#"			
			}
			...
		]
}

RESPOSTA EM CASO DE NADA ENCONTRADO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": []
}

URL: /api/Disciplinas/Listar
Função: Listar as disciplinas, se o parametro nome não é informado, lista todos
PEDIDO:

{
	"id_departamento" : "#ID do Campus, obtido com o metodo anterior#",
	"nome": "#Nome do Campus#",
	"pagina": "#Numero da Página#",
	"quantidade": "#Quantidade de campus por página#"
}

RESPOSTA EM CASO DE SUCESSO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": 	
		[
			{
				"id" : "#ID do Disciplina 1#",
				"nome" : "#Nome do Disciplina 1#"
			},
			{
				"id" : "#ID do Disciplina 2#",
				"nome" : "#Nome do Disciplina 2#"			
			},
			{
				"id" : "#ID do Disciplina 3#",
				"nome" : "#Nome do Disciplina 3#"			
			},
			{
				"id" : "#ID do Disciplina 4#",
				"nome" : "#Nome do Disciplina 4#"			
			}
			...
		]
}

RESPOSTA EM CASO DE NADA ENCONTRADO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": []
}


URL: /api/Horarios/Listar
Função: Listar as disciplinas
PEDIDO:

{
}

RESPOSTA EM CASO DE SUCESSO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": 	
		[
			{
				"id_horario": "#ID Horario#",
				"turno": "# Diurno ou Noturno#",
				"dia_da_semana" : "#Segunda OU Terca OU Quarta OU Quinta OU Sexta OU Sabado OU Domingo#",
				"hora_de_inicio" : "#00:00#",
				"hora_de_termino" : "#00:00#",
			},
			{
				"id_horario": "#ID Horario#",
				"turno": "# Diurno ou Noturno#",
				"dia_da_semana" : "#Segunda OU Terca OU Quarta OU Quinta OU Sexta OU Sabado OU Domingo#",
				"hora_de_inicio" : "#00:00#",
				"hora_de_termino" : "#00:00#",
			},
			{
				"id_horario": "#ID Horario#",
				"turno": "# Diurno ou Noturno#",
				"dia_da_semana" : "#Segunda OU Terca OU Quarta OU Quinta OU Sexta OU Sabado OU Domingo#",
				"hora_de_inicio" : "#00:00#",
				"hora_de_termino" : "#00:00#",
			},
			{
				"id_horario": "#ID Horario#",
				"turno": "# Diurno ou Noturno#",
				"dia_da_semana" : "#Segunda OU Terca OU Quarta OU Quinta OU Sexta OU Sabado OU Domingo#",
				"hora_de_inicio" : "#00:00#",
				"hora_de_termino" : "#00:00#",
			}
		]
}

RESPOSTA EM CASO DE NADA ENCONTRADO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": []
}

URL: /api/Turma/Listar
Função: Listar as turmas
PEDIDO:

{
	"consulta" : "#CONSULTAR NOTA 1#",
	"pagina": "#Numero da Página#",
	"quantidade": "#Quantidade de campus por página#"
}

RESPOSTA EM CASO DE SUCESSO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": 	
		[
			{
				"id" : "#ID da Turma 1#",
				"letra" : "#Letra da Turma#",
				"disciplina" : { 
							"id" : "#ID DA DISCIPLINA#",
							"nome" : "#Nome da Disciplina#",
							"departamento" : { 
										"id" : "#ID DO DEPARTAMENTO#",
										"nome" : "#Nome do Departamento#",
										"campus" : 
											{
												"id" : "#ID DO CAMPUS#",
												"nome" : "#NOME DO CAMPUS#"
										}
								       }
					       },

				"professor" : "#Nome do Professor#",
				"horarios" : [
							{
								"id_horario": "#ID Horario#",
								"turno": "# Diurno ou Noturno#",
								"dia_da_semana" : "#Segunda OU Terca OU Quarta OU Quinta OU Sexta OU Sabado OU Domingo#",
								"hora_de_inicio" : "#00:00#",
								"hora_de_termino" : "#00:00#",
								"sala" :
									{
										"id": "#ID DA SALA#",
										"codigo_sala" : "#Codigo da Sala#",
										"predio" : 
											{
												"id" : "#ID DO PREDIO#",
												"nome" : "#NOME DO PREDIO#",
												"campus" : 
													{
														"id" : "#ID DO CAMPUS#",
														"nome" : "#NOME DO CAMPUS#"
													}
											}
									}
							},
							...
					     ] 
			},
			...
		]
}

RESPOSTA EM CASO DE NADA ENCONTRADO:

{
	"codigo" : 200,
	"mensagem": "Sucesso",
	"corpo": []
}


NOTA 1:

O campo consulta especifica as condições, ele é uma lista de listas
[
	[
		{
			"parametro" : "#nome do parametro#" ,
		 	"valor" : "#valor do parametro#"
		},
		{
			 "parametro" : "#nome do parametro#" ,
			 "valor" : "#valor do parametro#"
		},
			...
	],
	[
		{
			"parametro" : "#nome do parametro#" ,
		 	"valor" : "#valor do parametro#"
		},
		{
			 "parametro" : "#nome do parametro#" ,
			 "valor" : "#valor do parametro#"
		},
			...
	],
	[
		{
			"parametro" : "#nome do parametro#" ,
		 	"valor" : "#valor do parametro#"
		},
		{
			 "parametro" : "#nome do parametro#" ,
			 "valor" : "#valor do parametro#"
		},
			...
	],
		...
]
EXEMPLO:
[
	[
		{
			"parametro" : "id_campus",
			"valor" : "7",
		},
		{
			"parametro" : "id_horario",
			"valor" : "20",
		},
	],

	[
		{
			"parametro" : "id_campus",
			"valor" : "2",
		},
		{
			"parametro" : "id_horario",
			"valor" : "15",
		},
	]
]

A SEGUINTE CONSULTA QUER DIZER: busque turmas que sejam no (campus 7 E no horário 20) OU (no campus 2 E no horário 15) 

Os parâmetros aceitaveis são: id_campus, id_departamento, id_horario, id_disciplina, id_predio, id_sala, id_curso


