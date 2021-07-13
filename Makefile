# Instala la aplicación en un entorno local (los servicios serán accedidos a traves de HTTP)
install:
	sudo sh app.sh

# Instala la aplicación en un entorno productivo (los servicios serán accedidos a traves de HTTPS)
install-ssl:
	sudo sh app-ssl.sh

# Compila todas las imágenes de cada servicio para la versión local
build:
	docker-compose build

# Compila todas las imágenes de cada servicio para la versión de producción
build-ssl:
	docker-compose -f docker-compose-ssl.yml build 


# Compila la imágen del frontend en local
build-frontend:
	docker-compose build frontend

# Compila la imágen del backend en local
build-backend:
	docker-compose build backend

# Compila la imágen del backend para producción
build-backend-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build backend

# Genera la documentación OpenAPI de los servicios Rest del backend en producción
build-schema-backend-ssl:
	docker-compose -f docker-compose-ssl.yml exec backend /bin/bash -c "python manage.py spectacular --file schema.yml"  

# Compila la imágen del frontend en producción
build-frontend-ssl:
	docker-compose -f docker-compose-ssl.yml build frontend 

# Desplega todos los servicios de la aplicación en entorno local
up:
	docker-compose up -d

# Desplega todos los servicios de la aplicación en producción
up-ssl:
	docker-compose -f docker-compose-ssl.yml  up -d

# Re-compila y desplega todos los servicios de la aplicación en entorno local
up-rebuild:
	docker-compose up -d --build

# Re-compila y desplega todos los servicios de la aplicación en producción
up-rebuild-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --build

# Desplega en modo debug todos los servicios de la aplicación en entorno local
up-debug:
	docker-compose up

# Desplega en modo debug todos los servicios de la aplicación en producción
up-debug-ssl:
	docker-compose -f docker-compose-ssl.yml up

# Destruye todos los servicios de la aplicación en entorno local
down:
	docker-compose down

# Destruye todos los servicios incluyendo la eliminación volumenes (bases de datos y archivos) de la aplicación en entorno local
down-all:
	docker-compose down -v

# Inicia todos los servicios de la aplicación en entorno local
start:
	docker-compose start

# Detiene todos los servicios de la aplicación en entorno local
stop:
	docker-compose stop

# Reinicia todos los servicios de la aplicación en entorno local
restart:
	docker-compose stop && docker-compose start

# Ejecuta la shell del contenedor del servidor web nginx para realizar trabajos de mantenimiento directamente sobre el contenedor.
shell-server:
	docker-compose exec server /bin/bash

# Lista todas las imágenes cargadas por los usuarios al sistema.
list-media:
	docker-compose exec backend ls -la /backend/media/users

# Ejecuta la shell del contenedor del frontend para realizar trabajos de mantenimiento directamente sobre el contenedor.
shell-frontend:
	docker-compose exec frontend /bin/bash

# Ejecuta la shell del contenedor del backend para realizar trabajos de mantenimiento directamente sobre el contenedor.
shell-backend:
	docker-compose exec backend /bin/bash

# Ejecuta la shell del contenedor de base de datos para realizar trabajos de mantenimiento directamente sobre el contenedor.
shell-db:
	docker-compose exec db /bin/sh

# Recupera los logs del contenedor del servidor web.
log-server:
	docker-compose logs server  

# Recupera los logs del contenedor del backend
log-backend:
	docker-compose logs backend  

# Recupera los logs del contenedor de frontend
log-frontend:
	docker-compose logs frontend  

# Recupera los logs del contenedor de la base de datos
log-db:
	docker-compose logs db

# Recupera los logs del contenedor de la api de predicción 
log-ml:
	docker-compose logs ml

# Genera los assets (imágenes, css, js) del administrador del backend 
collectstatic:
	docker-compose exec backend /bin/bash -c "python manage.py collectstatic --noinput"

# Actualiza el esquema de base de datos con cambios realizados en los modelos desde el código (modificación/eliminación/creación de tablas en DB) 
migrate:
	docker-compose exec backend /bin/bash -c "python manage.py makemigrations && python manage.py migrate core"

# destruye todos los servicios, aplicaciones, volumenes, imágenes  y redes creadas por el sistema.
prune:
	docker-compose down && docker system prune -a -f && docker system prune --volumes -f

# recupera la ip del servidor de base de datos.
postgres-ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db

# Construye e Inicia el servicio de base de datos
postgres-start:
	docker-compose build db && docker-compose up -d db

# lista todos los servicios actualmente creados
list:
	docker-compose ps

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el frontend en producción
install-frontend-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate frontend

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el API en producción
install-ml-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate ml

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el backend en producción
install-backend-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate backend 

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el servidor web en producción
install-server-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate server

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el frontend en local
install-frontend:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes frontend

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) la API en local
install-ml:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes ml

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el backend en local
install-backend:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes backend

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el servidor web en local
install-server:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes server

# Instala o Reinstala exclusivamente (sin incluir servicios dependientes) el frontend en local
deploy-frontend:
	 docker-compose -f docker-compose.yml exec frontend yarn deploy

# Compila e instala el proyecto nodejs del frontend en producción
deploy-frontend-ssl:
	 docker-compose -f docker-compose-ssl.yml exec frontend yarn deploy

# Empaqueta los modulos del frontend para el entorno de producción
dist-frontend-ssl:
	 docker-compose -f docker-compose-ssl.yml exec frontend yarn generate

# Empaqueta los modulos del frontend para el entorno local
dist-frontend:
	 docker-compose -f docker-compose.yml exec frontend yarn generate
