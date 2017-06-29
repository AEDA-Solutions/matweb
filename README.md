MATWEB
===================

Este é um software opensource em MVC de administração acadêmica que roda na web.

Dependências
-------------
 - Aplicação Web
 	- AngularJS (1.6)
	- Bootstrap CSS ()
 - Servidor da API 
	 - Python (2.7)
	 - uWSGI (2.0.15)
	 - bcrypt (3.1.3)
	 - psycopg2 (2.7.1)
 - Banco de Dados
	 - PostgreSQL

Estrutura de Diretórios
-------------

 - frontend (Aplicação Web)
 - backend (Servidor da API)
 	- Framework (Utilitários do Servidor)
  	- Models (Representa as requisições da API e as resposta da mesma)
  	- Controllers (Processa as requisições da API)
  	- Database (Classes para interação com o banco de dados)
    	- Models (Representa a estrutura do banco de dados)
	   	- Controllers (Realiza operações no banco de dados)
		
Executar Servidor da API
-------------

> Dentro da pasta backend, execute:
> uwsgi --http-socket :8080 --module __init__:application
>

