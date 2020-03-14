
VENV_PATH='env/bin/activate'
ENVIRONMENT_VARIABLE_FILE='.env'
DOCKER_NAME='python-az'
DOCKER_TAG='1.0'

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)


init: ## sets up environment and installs requirements
init: env
	pip install -r requirements.txt

install: ## Installs development requirments
install:
	python -m pip install --upgrade pip
	# Used for packaging and publishing
	pip install setuptools wheel twine
	# Used for linting
	pip install flake8
	# Used for testing
	pip install pytest

lint: ## Runs flake8 on src, exit if critical rules are broken
lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src --count --exit-zero --statistics

package: ## Create package in dist
package: clean
	python3 setup/setup.py sdist bdist_wheel

upload-test: ## Create package and upload to test.pypi
upload-test: package
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --non-interactive --verbose

upload: ## Create package and upload to pypi
upload: package
	python3 -m twine upload dist/* --non-interactive

clean: ## Remove build and cache files
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

env: ## Source venv and environment files for testing
env:
	python3 -m venv env
	source $(VENV_PATH)
	source $(ENVIRONMENT_VARIABLE_FILE)

leave: ## Cleanup and deactivate venv
leave: clean
	deactivate

test: ## Run pytest
test:
	pytest . -p no:logging -p no:warnings

build: ## Build docker image
build:
	docker build -t $(DOCKER_NAME):$(DOCKER_TAG) -f docker/Dockerfile .

create: ## Create docker image
create: build
	docker create -it --name $(DOCKER_NAME) $(DOCKER_NAME):$(DOCKER_TAG)

start: ## Build and start docker image
start: build
	docker start $(DOCKER_NAME)

run: ## build, start and run docker image
run: start
	docker run -it $(DOCKER_NAME):$(DOCKER_TAG)

exec: ## build, start and exec into docker image
exec: start
	docker exec -it $(DOCKER_NAME) python

