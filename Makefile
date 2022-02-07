install:
	pip3 install --upgrade pip &&\
		pip3 install -r Requirements.txt &&\


test:
	#python -m pytest -vv test_hello.py

lint:
	pylint -- disable=R,C mimic_example.py 

all: install lint test