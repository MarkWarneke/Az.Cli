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

package: clean
	python3 setup.py sdist bdist_wheel

upload: package
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

test:
	@echo "lol wut"
