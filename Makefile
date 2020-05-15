.PHONY: deps build uploadtest release

deps:
	python3 -m pip install --user --upgrade setuptools wheel
	python3 -m pip install --user --upgrade twine

build:
	python3 setup.py sdist bdist_wheel

local: build
	cd dist; pip3 install aws-autoscaler-*.tar.gz

uploadtest:
	python3 -m twine upload --repository testpypi dist/*
