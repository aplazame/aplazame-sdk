PYTEST = py.test --host=api.dev.aplazame.com --skip-verify --public-token=e75b929a1e4227230fe36c2af8fde10d6b2c5972 --private-token=2560a62b8c140f32c1b9f754ceefc888865d4f6b
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

