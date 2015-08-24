PYTEST ?= py.test --host=api.dev.aplazame.com --skip-verify --public-token=d3571070407d151b9b9d20c69deeab27e738b10f --private-token=029f07d69dfdc7aa573318239cdf6fc17d7daa04
export PYTEST

branch ?= dev
tests ?= tests

init-test:
	pip install -r requirements/tests.txt

init: init-test
	pip install -r requirements/local.txt
	pip install -r requirements/build.txt

test:
	$(PYTEST) --verbose $(tests)

coverage:
	$(PYTEST) --verbose --cov-report term --cov=aplazame_sdk tests
	coveralls

ci: init
	$(PYTEST) --junitxml=junit.xml tests

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dev:
	git checkout $(branch)
	git push origin $(branch)

release:
	git checkout release
	git merge master
	git push origin release
	git checkout dev

