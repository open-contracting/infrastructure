# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import csv
import os
from glob import glob
from pathlib import Path

import standard_theme
from docutils.nodes import make_id
from ocds_babel.translate import translate
from sphinx.locale import get_translation

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Open Contracting for Infrastructure Data Standards Toolkit"
copyright = "Open Contracting Partnership"
author = "Open Contracting Partnership"

version = "0.9"
release = "0.9.5"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.jsonschema",
    "sphinxcontrib.opencontracting",
    "sphinxcontrib.opendataservices",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/docson/[!p]**", "**/docson/package*.json"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "standard_theme"  # 'pydata_sphinx_theme'
html_theme_path = [standard_theme.get_html_theme_path()]
html_favicon = "_static/favicon-16x16.ico"
html_static_path = ["_static", "examples", "../mapping/sustainability.yaml"]
html_css_files = ["renderjson.css", "https://fonts.googleapis.com/css?family=Montserrat", "custom.css"]
html_js_files = ["renderjson.js", "json-example-format.js"]


# -- Local configuration -----------------------------------------------------

_ = get_translation("theme")

profile_identifier = "infrastructure"
repository_url = "https://github.com/open-contracting/infrastructure"

# Internationalization.
gettext_compact = False
# `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = f"{profile_identifier}-" if profile_identifier else ""
locale_dirs = ["locale/", os.path.join(standard_theme.get_html_theme_path(), "locale")]
# We use single quotes for codes, which docutils will change to double quotes.
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/utils/smartquotes.py
smartquotes = False

# MyST configuration.
myst_enable_extensions = ["linkify"]
myst_heading_anchors = 6
myst_heading_slug_func = make_id

# Theme customization.
navigation_with_keys = False  # restore the Sphinx default
html_context = {
    "analytics_id": "YEWDOOEQ",
}
html_theme_options = {
    "analytics_id": "YEWDOOEQ",
    "display_version": True,
    "root_url": f"/{profile_identifier}" if profile_identifier else "",
    "short_project": "OC4IDS",
    "copyright": copyright,
    "license_name": "Apache License 2.0",
    "license_url": f"{repository_url}/blob/HEAD/LICENSE",
    "repository_url": repository_url,
}
html_short_title = f"{html_theme_options['short_project']} v{release}"


def setup(app):
    # The root of the repository.
    basedir = Path(__file__).resolve().parents[1]
    # `LOCALE_DIR` from `config.mk`.
    localedir = basedir / "docs" / "locale"

    language = app.config.overrides.get("language", "en")

    # Headers for columns to translate in codelist CSVs. The headers in babel_ocds_mapping.cfg should match these.
    codelist_headers = ["Title", "Description", "Extension", "Business Logic"]
    # Headers for columns to translate in mapping CSVs. The headers in babel_ocds_mapping.cfg should match these.
    mapping_headers = ["CoST IDS element", "CoST IDS draft definition", "Mapping to OC4IDS", "Mapping from OCDS"]

    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = f"{gettext_domain_prefix}schema"
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = f"{gettext_domain_prefix}codelists"
    # The gettext domain for mapping translations. Should match the domain in the `pybabel compile` command.
    mapping_domain = f"{gettext_domain_prefix}mappings"

    schema_dir = basedir / "schema" / "project-level"
    static_dir = basedir / "docs" / "_static" / "project-level"
    build_dir = basedir / "build" / language

    branch = os.getenv("GITHUB_REF_NAME", "latest")

    translate(
        [
            # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
            (glob(str(schema_dir / "*-schema.json")), static_dir, schema_domain),
            (glob(str(schema_dir / "*-schema.json")), build_dir, schema_domain),
            # The glob patterns in `babel_ocds_codelist.cfg` should match these.
            (glob(str(schema_dir / "codelists" / "*.csv")), static_dir / "codelists", codelists_domain),
            (glob(str(schema_dir / "codelists" / "*.csv")), build_dir / "codelists", codelists_domain),
        ],
        localedir,
        language,
        codelist_headers,
        version=branch,
    )

    translate(
        [
            # The glob patterns in `babel_ocds_mapping.cfg` should match these filenames.
            (glob(str(basedir / "mapping" / "*.csv")), static_dir, mapping_domain),
            (glob(str(basedir / "mapping" / "*.csv")), build_dir, mapping_domain),
        ],
        localedir,
        language,
        mapping_headers,
        version=branch,
    )

    # Split the mapping CSV into two.
    for path in build_dir.iterdir():
        name = path.name
        if name.endswith(".csv") and not name.startswith(("ids-", "ocds-")):
            for prefix, column_index in (("ids", 3), ("ocds", 2)):
                with path.open() as i, (build_dir / f"{prefix}-{name}").open("w") as o:
                    reader = csv.reader(i)
                    writer = csv.writer(o, lineterminator="\n")
                    for row in reader:
                        del row[column_index]  # Drop mapping column
                        writer.writerow(row[0:3])  # Drop OC4IDS Fields and OC4IDS Codes columns
            path.unlink()
