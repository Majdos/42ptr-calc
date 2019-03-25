PYTHON_MAIN_FILE=main.py

DOCS_DIRECTORY_NAME=doc
DOCS_LOCATION=..

TESTS_DIRECTORY_NAME=tests
TESTS_LOCATION=..

.PHONY: all pack clean test doc run install profile

# all (přeloží projekt - včetně programu pro profiling)
all: install doc profile
	pip install -r requirements.txt

pack:
	# todo: zabalí projekt tak, aby mohl být odevzdán

clean:
	# todo: smaže všechny soubory, co nemají být odevzdány

test:
	python -m unittest discover -s $(TESTS_LOCATION)/$(TESTS_DIRECTORY_NAME)/math_tests -v -p '*_test.py'

doc:
	cd $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME) && make html

run: install
	# spusti aplikaciu
	pip install -r requirements.txt
	./$(PYTHON_MAIN_FILE)

install:
	pip install -r requirements.txt

profile:
	# todo: spustí překlad programu pro výpočet směrodatné odchylky na profiling
