init:
	pip install -r requirements/tests.txt
	pip install -r requirements/build.txt
test:
	# py.test tests
	py.test --host=api.dev.aplazame.com --token=029f07d69dfdc7aa573318239cdf6fc17d7daa04 --skip-verify
coverage:
	py.test --verbose --cov-report term --cov=aplazame_sdk tests

ci: init
	py.test --junitxml=junit.xml
publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
