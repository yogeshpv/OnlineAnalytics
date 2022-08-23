setup:
	python -m venv ./venv

install:
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=lib tests/

lint:
	pylint --disable=R,C lib  

lint2:
	pylint --disable=R,C tests

all: install lint lint2 test
