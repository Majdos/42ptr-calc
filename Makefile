LANGUAGE ?= sk_SK

DOCS_DIRECTORY_NAME=docs
DOCS_LOCATION=.
DOCS_API_LOCATION=$(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source/modules

TESTS_DIRECTORY_NAME=tests
TESTS_LOCATION=.

I18N_DIRECTORY=./resources/translations
I18N_DOMAIN=messages

SRC=./ptr42

.PHONY: all pack clean test all-tests doc run install profile i18n_extract i18n_init i18n_update i18n_compile

all: install i18n_compile profile

pack: clean
	mkdir -p install doc repo
	cp -r $(DOCS_DIRECTORY_NAME)/build/html/* doc/
	cp build/nsis/42ptr_calc_1.0.exe install/
	cp -r * repo/
	zip repo --out xlorin01_xjavor20_xondri08_xvinar00.zip
	$(RM) -r repo

clean:
	$(RM) -r build *.egg-info
	$(RM) -r $(DOCS_DIRECTORY_NAME)/build

doc:
	$(RM) -r $(DOCS_API_LOCATION)
	pipenv run sphinx-apidoc -o $(DOCS_API_LOCATION) -M --implicit-namespaces \
		--ext-autodoc --ext-githubpages $(SRC)

	cd $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source && pipenv run sphinx-build -b html -D language=$(LANGUAGE) \
		. ../build/html/$(LANGUAGE)

run:
	pipenv run bash -c "python setup.py develop && calc42"

install:
	pipenv install --dev

test:
	python -m unittest discover -s $(TESTS_DIRECTORY_NAME).math_tests -v -p '*_test.py'

all_tests:
	python -m unittest discover -s $(TESTS_DIRECTORY_NAME) -v -p '*_test.py'

i18n_extract:
	pipenv run pybabel extract -w 80 --copyright-holder 42ptr -o $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot src

i18n_init:
	pipenv run pybabel init --domain $(I18N_DOMAIN) -i $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot -d $(I18N_DIRECTORY)/ -l $(LANGUAGE)

i18n_update:
	pipenv run pybabel update --domain $(I18N_DOMAIN) -i $(I18N_DIRECTORY)/$(I18N_DOMAIN).pot -d $(I18N_DIRECTORY)/ -l $(LANGUAGE)

i18n_compile:
	pipenv run pybabel compile -f -d $(I18N_DIRECTORY)

profile:
	pipenv run bash -c "python setup.py develop > /dev/null && profile"
