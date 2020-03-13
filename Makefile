init:
	pip install -r REQUIREMENTS.txt

lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src --count --exit-zero --statistics

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

package-test: clean
	python3 setup.dev.py sdist bdist_wheel

upload-test: package-test
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --non-interactive --verbose

upload: package
	python3 -m twine upload dist/* --non-interactive

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

test:
	pytest
