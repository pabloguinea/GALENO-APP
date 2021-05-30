install:
	sudo ./app.sh

install-ssl:
	sudo ./app-ssl.sh

build:
	docker-compose build

build-ssl:
	docker-compose -f docker-compose-ssl.yml build 


build-frontend:
	docker-compose build frontend

build-backend:
	docker-compose build backend

build-backend-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build backend

build-schema-backend-ssl:
	docker-compose -f docker-compose-ssl.yml exec backend /bin/bash -c "python manage.py spectacular --file schema.yml"  

build-frontend-ssl:
	docker-compose -f docker-compose-ssl.yml build frontend 

up:
	docker-compose up -d

up-ssl:
	docker-compose -f docker-compose-ssl.yml  up -d

up-rebuild:
	docker-compose up -d --build

up-rebuild-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --build

up-debug:
	docker-compose up

up-debug-ssl:
	docker-compose -f docker-compose-ssl.yml up

down:
	docker-compose down

down-all:
	docker-compose down -v

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-server:
	docker-compose exec server /bin/bash

list-media:
	docker-compose exec backend ls -la /backend/media/users

shell-frontend:
	docker-compose exec frontend /bin/bash

shell-backend:
	docker-compose exec backend /bin/bash

shell-db:
	docker-compose exec db /bin/sh

log-server:
	docker-compose logs server  

log-backend:
	docker-compose logs backend  

log-frontend:
	docker-compose logs frontend  

log-db:
	docker-compose logs db

log-ml:
	docker-compose logs ml

collectstatic:
	docker-compose exec backend /bin/bash -c "python manage.py collectstatic --noinput"

migrate:
	docker-compose exec backend /bin/bash -c "python manage.py makemigrations && python manage.py migrate core"

prune:
	docker-compose down && docker system prune -a -f && docker system prune --volumes -f

postgres-ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db

postgres-start:
	docker-compose build db && docker-compose up -d db

list:
	docker-compose ps

install-frontend-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate frontend

install-ml-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate ml

install-backend-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate backend 

install-server-ssl:
	docker-compose -f docker-compose-ssl.yml up -d --no-deps --build --force-recreate server

install-frontend:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes frontend

install-ml:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes ml

install-backend:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes backend

install-server:
	docker-compose -f docker-compose.yml up -d --no-deps --build --force-recreate --no-deps --renew-anon-volumes server

deploy-frontend:
	 docker-compose -f docker-compose.yml exec frontend yarn deploy

deploy-frontend-ssl:
	 docker-compose -f docker-compose-ssl.yml exec frontend yarn deploy

dist-frontend-ssl:
	 docker-compose -f docker-compose-ssl.yml exec frontend yarn generate

dist-frontend:
	 docker-compose -f docker-compose.yml exec frontend yarn generate
