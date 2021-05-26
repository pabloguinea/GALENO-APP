install:
	sudo ./app.sh

install-ssl:
	sudo ./app-ssl.sh

build:
	docker-compose build

build-ssl:
	docker-compose -f docker-compose-ssl.yml build 

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
	docker exec -ti server /bin/sh

shell-frontend:
	docker exec -ti frontend /bin/sh

shell-backend:
	docker exec -ti backend /bin/sh

shell-db:
	docker exec -ti db /bin/sh

log-server:
	docker-compose logs server  

log-backend:
	docker-compose logs backend  

log-frontend:
	docker-compose logs frontend  

log-db:
	docker-compose logs db

collectstatic:
	docker exec backend /bin/sh -c "python manage.py collectstatic --noinput"

migrate:
	docker exec backend /bin/sh -c "python manage.py makemigrations && python manage.py migrate"

prune:
	docker-compose down && docker system prune -a -f && docker system prune --volumes -f

postgres-ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db

postgres-start:
	docker-compose build db && docker-compose up -d db

list:
	docker-compose ps