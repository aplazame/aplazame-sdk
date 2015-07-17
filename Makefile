init:
	pip install -r requirements.txt

test:
	py.test test_sdk.py

coverage:
	py.test --verbose --cov-report term --cov=aplazame_sdk test_sdk.py

ci: init
	py.test --junitxml=junit.xml

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
