init:
	pip install -r REQUIREMENTS.txt

build:
	docker build -t python-az:1.0 .

create:
	docker create -it --name python-az python-az:1.0

start:
	docker start python-az

exec: start
	docker exec -it python-az python

test:
	@echo "lol wut"
