clean: destroy build up

destroy:
	docker-compose -f local.yml down -v

build:
	docker-compose -f local.yml build

build_nocache:
	docker-compose -f local.yml build --no-cache

up:
	docker-compose -f local.yml up

testing:
	docker-compose -f local.yml run --rm django sh -c "pytest"
