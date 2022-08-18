# Edit these variables as appropriate.

# The space-separated, period-prefixed translations to build (for easier substitutions).
TRANSLATIONS=.es
# The source language and translations to build.
LANGUAGES=.en $(TRANSLATIONS)

# Directory of documentation files to build with Sphinx.
DOCS_DIR=docs
# Directory of catalog files.
LOCALE_DIR=docs/locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Extra build files or directories. (These should match paths in .gitignore.)
EXTRA_BUILD_FILES=chromedriver* docs/_static/process-level docs/_static/project-level
# Files that are built and distributed (you may use Bash extended globbing).
DIST_FILES=
# Directory in which to build .pot files.
POT_DIR=$(BUILD_DIR)/locale
# The prefix, if any, to the schema and codelists domains.
DOMAIN_PREFIX=infrastructure-
# The Transifex project name.
TRANSIFEX_PROJECT=oc4ids-09
# Any additional extract targets.
EXTRACT_TARGETS=extract_mappings
# Extra arguments for sphinx-autobuild.
SPHINX_AUTOBUILD_EXTRA_ARGS=--re-ignore $(DOCS_DIR)/_static.*

# The path to the branch of the documentation to print to PDF.
PDF_ROOT=/infrastructure/latest
# The pattern of pages to print to PDF. Update if the documentation adds, removes or renames pages.
PDF_PAGES={,about/,projects/,reference/{,browser/,schema/,codelists/,package/,changelog/},guidance/{,identifiers/,publishing/,using/,evaluating/,data_user_guide/,example/},cost/,support/}
# 15000 may warn: "Warning: Received createRequest signal on a disposed ResourceObject's NetworkAccessManager. This might
# be an indication of an iframe taking too long to load."
PDF_DELAY=20000

# Compile PO files for codelists, schema and mappings to MO files, so that `translate` succeeds.
.PHONY: compile
compile:
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)schema
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)codelists
	pybabel compile --use-fuzzy -d $(LOCALE_DIR) -D $(DOMAIN_PREFIX)mappings

# Put local targets below.

.PHONY: extract_mappings
extract_mappings: $(POT_DIR)
	pybabel extract -F babel_ocds_mapping.cfg . -o $(POT_DIR)/$(DOMAIN_PREFIX)mappings.pot
