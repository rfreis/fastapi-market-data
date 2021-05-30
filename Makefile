build:
	docker-compose build fastapi

local-bash:
	docker-compose exec fastapi /bin/bash

load-data:
	docker-compose exec fastapi python load_data.py $(qty)

logs:
	docker-compose logs --follow fastapi

migrate:
	docker-compose exec fastapi alembic upgrade head

start-local:
	docker-compose up -d

stop:
	docker-compose down

pytest:
	docker-compose exec fastapi pytest -vv
