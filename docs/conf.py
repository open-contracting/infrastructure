#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 20 21:53:17 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
from collections import OrderedDict
from glob import glob
from pathlib import Path

import standard_theme
from ocds_babel.translate import translate
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinxcontrib.opendataservices import AutoStructifyLowPriority

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.jsonschema',
    'sphinxcontrib.opendataservices',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.md'
source_parsers = {
    '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Open Contracting for Infrastructure Data Standards Toolkit'
copyright = 'Open Contracting Partnership'
author = 'Open Contracting Partnership'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = 'alpha'  # '1.0.0-rc.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'standard_theme'
html_theme_path = [standard_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'examples']


# -- Local configuration --------------------------------------------------

profile_identifier = 'infrastructure'
repository_url = 'https://github.com/open-contracting/infrastructure'

html_theme_options = {
    'display_version': True,
    'root_url': '/{}'.format(profile_identifier),
    'short_project': project.replace('Open Contracting Data Standard', 'OCDS'),
    'copyright': copyright,
    'license_name': 'Apache License 2.0',
    'license_url': '{}/blob/HEAD/LICENSE'.format(repository_url),
    'repository_url': repository_url,
}

# The version of OCDS to patch.
standard_tag = '1__1__3'
standard_version = '1.1'

# Where the patched schemas will be deployed.
schema_base_url = 'http://standard.open-contracting.org{}/schema/{}/'.format(
    html_theme_options['root_url'], release.replace('-', '__').replace('.', '__'))

# The `LOCALE_DIR` from `config.mk`, plus the theme's locale.
locale_dirs = ['../locale/', os.path.join(standard_theme.get_html_theme_path(), 'locale')]

gettext_compact = False

# The `DOMAIN_PREFIX` from `config.mk`.
gettext_domain_prefix = '{}-'.format(profile_identifier)

# List the extension identifiers and versions that should be part of this profile. The extensions must be available in
# the extension registry: https://github.com/open-contracting/extension_registry/blob/master/extension_versions.csv
extension_versions = OrderedDict([
    # ('extension_id_in_registry', 'version'),
])


def setup(app):
    app.add_config_value('extension_versions', extension_versions, True)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True
    }, True)

    app.add_transform(AutoStructify)
    app.add_transform(AutoStructifyLowPriority)

    # The root of the repository.
    basedir = Path(os.path.realpath(__file__)).parents[1]
    # The `LOCALE_DIR` from `config.mk`.
    localedir = basedir / 'locale'

    language = app.config.overrides.get('language', 'en')

    # The gettext domain for schema translations. Should match the domain in the `pybabel compile` command.
    schema_domain = '{}schema'.format(gettext_domain_prefix)
    # The gettext domain for codelist translations. Should match the domain in the `pybabel compile` command.
    codelists_domain = '{}codelists'.format(gettext_domain_prefix)

    project_dir = basedir / 'schema' / 'project-level'
    project_build_dir = basedir / 'docs' / '_static' / 'project-level'
    language_dir = basedir / 'build' / language

    translate([
        # The glob patterns in `babel_ocds_schema.cfg` should match these filenames.
        (glob(str(project_dir / '*-schema.json')), project_build_dir, schema_domain),
        (glob(str(project_dir / '*-schema.json')), language_dir, schema_domain),
        # The glob patterns in `babel_ocds_codelist.cfg` should match these.
        (glob(str(project_dir / 'codelists' / '*.csv')), project_build_dir / 'codelists', codelists_domain),
        (glob(str(project_dir / 'codelists' / '*.csv')), language_dir / 'codelists', codelists_domain),
    ], localedir, language, version=standard_version)

    # Copy our mapping files as well. This currently does not perform translation, which would need to be added.
    for filename in glob(str(basedir / 'mapping' / '*.csv')):
        with open(filename) as f:
            mapping_file = f.read()
        with open(language_dir / os.path.basename(filename), 'w') as f:
            f.write(mapping_file)
