all: test clean build deploy

test:
	pytest

clean:
	rm -Rf *.egg-info
	rm -Rf dist

build: clean
	python3 setup.py sdist

deploy: build
	pip3 install twine
	twine upload --skip-existing dist/*