init:
	pip install -r REQUIREMENTS.txt

build:
	docker build -t python-az:1.0 .

create: build
	docker create -it --name python-az python-az:1.0

start: build
	docker start python-az

run: start
	docker run -it python-az:1.0

exec: start
	docker exec -it python-az python

test:
	@echo "lol wut"
