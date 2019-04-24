LANGUAGE ?= sk_SK

DOCS_DIRECTORY_NAME = docs
DOCS_LOCATION = ..
DOCS_API_LOCATION = $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source/modules
SRC = ./ptr42

TESTS_DIRECTORY_NAME = tests

I18N_DIRECTORY = ./resources/translations
I18N_DOMAIN = messages

PROJECT_ROOT = ..
IVS_ZIP_NAME = xlorin01_xjavor20_xondri08_xvinar00.zip
IVS_DOC_DIR = $(PROJECT_ROOT)/temp/doc
IVS_INSTALL_DIR = $(PROJECT_ROOT)/temp/install
IVS_REPO_DIR = $(PROJECT_ROOT)/temp/repo
IVS_REQUIRED_DIRS = $(IVS_DOC_DIR) $(IVS_INSTALL_DIR) $(IVS_REPO_DIR)

.PHONY: all pack clean test all-tests doc run install profile i18n_extract i18n_init i18n_update i18n_compile \
	prepare_dev_environment win_installer

all: install i18n_compile profile

pack:
	$(RM) -r $(PROJECT_ROOT)/temp
	mkdir -p $(IVS_REQUIRED_DIRS)
	cp -r $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/build/html/* $(IVS_DOC_DIR)
	cp build/nsis/42ptr_calc_1.0.exe $(IVS_INSTALL_DIR)
	cd $(PROJECT_ROOT) && git archive --format zip -9 -o $(IVS_ZIP_NAME) master

	mv $(PROJECT_ROOT)/$(IVS_ZIP_NAME) $(IVS_REPO_DIR)/
	cd $(IVS_REPO_DIR) && unzip $(IVS_ZIP_NAME) && $(RM) $(IVS_ZIP_NAME)
	cp -r $(PROJECT_ROOT)/.git $(IVS_REPO_DIR)/
	cd $(PROJECT_ROOT)/temp && zip -r ../$(IVS_ZIP_NAME) *
	$(RM) -r $(PROJECT_ROOT)/temp

clean:
	$(RM) -r src/build src/*.egg-info
	$(RM) -r $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/build

doc:
	$(RM) -r $(DOCS_API_LOCATION)
	pipenv run sphinx-apidoc -o $(DOCS_API_LOCATION) -M --implicit-namespaces \
		--ext-autodoc --ext-githubpages $(SRC)

	pipenv run bash -c 'cd $(DOCS_LOCATION)/$(DOCS_DIRECTORY_NAME)/source && sphinx-build -b html -D language=$(LANGUAGE) \
		. ../build/html/$(LANGUAGE)'

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

win_installer:
	pipenv run pynsist installer.cfg

prepare_dev_environment: install i18n_compile
