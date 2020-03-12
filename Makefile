init:
	pip install -r requirements.txt

build:
	docker build -t python-az:1.0 .

run: build
	docker


test:
	@echo "lol wut"
