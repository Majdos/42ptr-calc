LANGUAGE ?= sk_SK
PYTHON_MAIN_FILE=main.py

DOCS_DIRECTORY_NAME=doc
DOCS_LOCATION=.
DOC_API_LOCATION=$(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source/modules

TESTS_DIRECTORY_NAME=tests
TESTS_LOCATION=.

I18N_DIRECTORY=./src/translations
I18N_DOMAIN=messages

DEBIAN_MAINTAINER=Marian Lorinc
DEBIAN_MAINTAINER_EMAIL=xlorin01@vutbr.cz
DEBIAN_PACKAGER_DIR=dist

DH_MAKE_FLAGS=-c gpl3 -e $(DEBIAN_MAINTAINER_EMAIL) -n -y -s

PROGRAM_VERSION=1.0.0
PROGRAM_NAME=calc42


SRC=./src

.PHONY: all pack clean test all-tests doc run install profile i18n_extract i18n_init i18n_update i18n_compile

all: install i18n_compile doc profile

pack:
	# todo: zabalí projekt tak, aby mohl být odevzdán

clean:
	# todo: smaže všechny soubory, co nemají být odevzdány

test:
	python -m unittest discover -s $(TESTS_DIRECTORY_NAME).math_tests -v -p '*_test.py'

all_tests:
	python -m unittest discover -s $(TESTS_DIRECTORY_NAME) -v -p '*_test.py'

i18n_extract:
	pybabel extract -w 80 --copyright-holder 42ptr -o $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot src

i18n_init:
	pybabel init --domain $(I18N_DOMAIN) -i $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot -d $(I18N_DIRECTORY)/ -l $(LANGUAGE)

i18n_update:
	pybabel update --domain $(I18N_DOMAIN) -i $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot -d $(I18N_DIRECTORY)/ -l $(LANGUAGE)

i18n_compile:
	pybabel compile -f -d $(I18N_DIRECTORY)

doc:
	rm -r $(DOC_API_LOCATION)
	sphinx-apidoc -o $(DOC_API_LOCATION) -M --implicit-namespaces \
		--ext-autodoc --ext-githubpages $(SRC)

	cd $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source && sphinx-build -b html -D language=$(LANGUAGE) . ../build/html/$(LANGUAGE)

init_debpkg:
	cd $(DEBIAN_PACKAGER_DIR) && tar xzvf $(PROGRAM_NAME)-$(PROGRAM_VERSION).tar.gz
	cd $(DEBIAN_PACKAGER_DIR)/$(PROGRAM_NAME)-$(PROGRAM_VERSION) && USER=majo dh_make $(DH_MAKE_FLAGS) && cp packager/install debian

run: install
	./$(PYTHON_MAIN_FILE)

install:
	pip install -r requirements.txt

profile:
	# todo: spustí překlad programu pro výpočet směrodatné odchylky na profiling
