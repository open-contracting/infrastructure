# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
from glob import glob
from pathlib import Path

import standard_theme
from docutils.nodes import make_id
from ocds_babel.translate import translate
from sphinx.locale import get_translation

# -- Project information -----------------------------------------------------

project = 'Open Contracting for Infrastructure Data Standards Toolkit'
copyright = 'Open Contracting Partnership'
author = 'Open Contracting Partnership'

version = '0.9'
release = '0.9.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinxcontrib.jsonschema',
    'sphinxcontrib.opencontracting',
    'sphinxcontrib.opendataservices',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_static/docson/**.html', '_static/docson/**.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'standard_theme'  # 'pydata_sphinx_theme'
html_theme_path = [standard_theme.get_html_theme_path()]
html_favicon = '_static/favicon-16x16.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'examples']


# -- Local configuration -----------------------------------------------------

_ = get_translation('theme')

profile_identifier = 'infrastructure'
repository_url = 'https://github.com/open-contracting/infrastructure'

# Internationalization.
gettext_compact = False
# `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = f'{profile_identifier}-' if profile_identifier else ''
locale_dirs = ['locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]
# We use single quotes for codes, which docutils will change to double quotes.
# https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/utils/smartquotes.py
smartquotes = False

# MyST configuration.
myst_enable_extensions = ['linkify']
myst_heading_anchors = 6
myst_heading_slug_func = make_id

# Theme customization.
navigation_with_keys = False  # restore the Sphinx default
html_context = {
    'analytics_id': 'YEWDOOEQ',
}
html_theme_options = {
    'analytics_id': 'YEWDOOEQ',
    'display_version': True,
    'root_url': f'/{profile_identifier}' if profile_identifier else '',
    'short_project': project.replace('Open Contracting Data Standard', 'OCDS'),
    'copyright': copyright,
    'license_name': 'Apache License 2.0',
    'license_url': f'{repository_url}/blob/HEAD/LICENSE',
    'repository_url': repository_url,
}


def setup(app):
    # The root of the repository.
    basedir = Path(__file__).resolve().parents[1]
    # `LOCALE_DIR` from `config.mk`.
    localedir = basedir / 'docs' / 'locale'

    language = app.config.overrides.get('language', 'en')

    # Headers for columns to translate in codelist CSVs. The headers in babel_ocds_mapping.cfg should match these.
    codelist_headers = ['Title', 'Description', 'Extension']
    # Headers for columns to translate in mapping CSVs. The headers in babel_ocds_mapping.cfg should match these.
    mapping_headers = ['Mapping to OC4IDS', 'Mapping from OCDS']

    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = f'{gettext_domain_prefix}schema'
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = f'{gettext_domain_prefix}codelists'
    # The gettext domain for mapping translations. Should match the domain in the `pybabel compile` command.
    mapping_domain = f'{gettext_domain_prefix}mappings'

    schema_dir = basedir / 'schema' / 'project-level'
    static_dir = basedir / 'docs' / '_static' / 'project-level'
    build_dir = basedir / 'build' / language

    branch = os.getenv('GITHUB_REF_NAME', 'latest')

    translate([
        # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
        (glob(str(schema_dir / '*-schema.json')), static_dir, schema_domain),
        (glob(str(schema_dir / '*-schema.json')), build_dir, schema_domain),
        # The glob patterns in `babel_ocds_codelist.cfg` should match these.
        (glob(str(schema_dir / 'codelists' / '*.csv')), static_dir / 'codelists', codelists_domain),
        (glob(str(schema_dir / 'codelists' / '*.csv')), build_dir / 'codelists', codelists_domain),
    ], localedir, language, codelist_headers, version=branch)

    translate([
        # The glob patterns in `babel_ocds_mapping.cfg` should match these filenames.
        (glob(str(basedir / 'mapping' / '*.csv')), static_dir, mapping_domain),
        (glob(str(basedir / 'mapping' / '*.csv')), build_dir, mapping_domain),
    ], localedir, language, mapping_headers, version=branch)
