PYTHON_MAIN_FILE=main.py

DOCS_DIRECTORY_NAME=doc
DOCS_LOCATION=..

TESTS_DIRECTORY_NAME=tests
TESTS_LOCATION=..

# DEPENDENCIES=(sphinx recommonmark nose)

# all (přeloží projekt - včetně programu pro profiling)
all: doc profile

pack:
	# todo: zabalí projekt tak, aby mohl být odevzdán

clean:
	# todo: smaže všechny soubory, co nemají být odevzdány

test:
	# spustí testy matematické knihovny
	cd $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/math_tests && nosetests

doc:
	# vygeneruje dokumentaciu
	cd $(TESTS_LOCATION)/$(TESTS_DIRECTORY_NAME) && make html

run:
	# spusti aplikaciu
	./$(PYTHON_MAIN_FILE)

profile:
	# todo: spustí překlad programu pro výpočet směrodatné odchylky na profiling
