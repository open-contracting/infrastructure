import json
import os
import warnings
from glob import glob
from pathlib import Path

import pytest
from jsonschema import FormatChecker
from jsonschema.validators import Draft4Validator
from jscc.testing.checks import validate_schema

from manage import set_additional_properties

cwd = os.getcwd()
basedir = Path(__file__).resolve().parents[1]


def formatwarning(message, category, filename, lineno, line=None):
    return str(message).replace(cwd + os.sep, '')


warnings.formatwarning = formatwarning
pytestmark = pytest.mark.filterwarnings('always')


# See test_example_valid in standard-maintenance-scripts/tests/test_readme.py
def test_examples_valid():
    with (basedir / 'schema' / 'project-level' / 'project-package-schema.json').open() as f:
        schema = json.load(f)

    set_additional_properties(schema, False)

    validator = Draft4Validator(schema, format_checker=FormatChecker())

    errors = 0
    for path in (basedir / 'docs' / 'examples').glob('**/*.json'):
        if path.name == 'blank.json':
            continue

        with open(path) as f:
            data = json.load(f)

        errors += validate_schema(path, data, validator)

    assert not errors, 'One or more JSON files are invalid. See warnings below.'
