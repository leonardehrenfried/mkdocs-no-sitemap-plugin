clean:
	rm -rf dist
build:
	python3 -m build

publish: clean build
	python3 -m twine upload dist/*

