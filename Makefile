PYTEST ?= py.test --host=api.aplazame.com --version=1
export PYTEST

init:
	pip install -r requirements/tests.txt
	pip install -r requirements/build.txt

test:
	$(PYTEST)

coverage:
	$(PYTEST) --verbose --cov-report term --cov=aplazame_sdk tests
	coveralls --verbose

ci: init
	$(PYTEST) --junitxml=junit.xml

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
