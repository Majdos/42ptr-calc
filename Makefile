PYTHON_MAIN_FILE=main.py

DOCS_DIRECTORY_NAME=doc
DOCS_LOCATION=.
DOC_API_LOCATION=$(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source/modules

TESTS_DIRECTORY_NAME=tests
TESTS_LOCATION=.

I18N_DIRECTORY=./src/translations
I18N_DOMAIN=messages

SRC=./src/ptr42

.PHONY: all pack clean test all-tests doc run install profile i18n_extract i18n_init i18n_update i18n_compile

# all (přeloží projekt - včetně programu pro profiling)
all: install i18n_compile doc profile

pack:
	# todo: zabalí projekt tak, aby mohl být odevzdán

clean:
	# todo: smaže všechny soubory, co nemají být odevzdány

test:
	python -m unittest discover -s $(TESTS_DIRECTORY_NAME).math_tests -v -p '*_test.py'

all-tests:
	python -m unittest discover -s $(TESTS_DIRECTORY_NAME) -v -p '*_test.py'

i18n_extract:
	pybabel extract -w 80 --copyright-holder 42ptr -o $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot src

i18n_init:
	pybabel init --domain $(I18N_DOMAIN) -i $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot -d $(I18N_DIRECTORY)/ -l $(LANG)

i18n_update:
	pybabel update --domain $(I18N_DOMAIN) -i $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot -d $(I18N_DIRECTORY)/ -l $(LANG)

i18n_compile:
	pybabel compile -f -d $(I18N_DIRECTORY)

doc:
	rm -r $(DOC_API_LOCATION)
	sphinx-apidoc -o $(DOC_API_LOCATION) -M --implicit-namespaces \
		--ext-autodoc --ext-githubpages $(SRC)

	cd $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME) && make html

run: install
	./$(PYTHON_MAIN_FILE)

install:
	pip install -r requirements.txt

profile:
	# todo: spustí překlad programu pro výpočet směrodatné odchylky na profiling
