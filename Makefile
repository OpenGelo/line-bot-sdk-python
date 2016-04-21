all: clean-pyc setup test

setup:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

test:
	python runtests.py


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
