PYTEST ?= py.test --host=api.dev.aplazame.com --skip-verify --token=029f07d69dfdc7aa573318239cdf6fc17d7daa04
export PYTEST

init:
	pip install -r requirements/tests.txt
	pip install -r requirements/build.txt
test:
	$(PYTEST)
coverage:
	$(PYTEST) --verbose --cov-report term --cov=aplazame_sdk tests

ci: init
	$(PYTEST) --junitxml=junit.xml
publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
