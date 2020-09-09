dist: clean
	python3 setup.py sdist

install: dist
	pip install dist/*

upload: dist
	twine upload dist/*

doc:
	mkdir docs
	mkdir docs/html
	doxygen

clean:
	rm -rf build
	rm -rf dist
	rm -rf r2cloud.egg-info
	rm -rf docs