init:
	pip install -r requirements.txt

lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src --count --exit-zero --statistics

package: clean
	python3 setup.py sdist bdist_wheel

upload-test: package
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --non-interactive --verbose

upload: package
	python3 -m twine upload dist/* --non-interactive

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

env:
	source env/bin/activate 
	source .env

leave: clean 
	deactivate

test: env
	pytest
