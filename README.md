# Compilar y ejecutar el proyecto

### Ejecutar la base de datos de Postgres

Primero, necesitamos ejecutar la base de datos de Postgres.
  ```sh
	docker compose up -d flask_db
  ```
Para verificar si se está ejecutando, puede usar el siguiente comando:
```sh
docker compose logs
  ```
y el

```sh
docker ps -a
```
### Construye el proyecto

Para compilar el proyecto, escriba:
  ```sh
	docker compose build
  ```

###  Ejecutar el proyecto

PAhora podemos ejecutar el proyecto.
	```sh
docker compose up flask_app
  ```

### Probar el proyecto

apis crud USERS
- POST request to localhost:4000/users
- GET request to localhost:4000/users
- PUT request to localhost:4000/users/{id}
- GET request to localhost:4000/users/{id} (unjugador) 
- DELETE request to localhost:4000/users/{id}
apis crud ARTICLES
- POST request to localhost:4000/articles
- GET request to localhost:4000/articles
- PUT request to localhost:4000/articles/{id}
- GET request to localhost:4000/articles/{id} (unjugador) 
- DELETE request to localhost:4000/articles/{id}
