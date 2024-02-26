import json
import os
import warnings
from glob import glob

import pytest
from jsonschema import FormatChecker
from jsonschema.validators import Draft4Validator

cwd = os.getcwd()


def formatwarning(message, category, filename, lineno, line=None):
    return str(message).replace(cwd + os.sep, '')


warnings.formatwarning = formatwarning
pytestmark = pytest.mark.filterwarnings('always')


def disallow_additional(schema):
    """
    Disallows additional properties.
    """

    if schema.get('type') not in ['object', 'array']:
        return schema

    if schema.get('type') == 'array':
        schema['items'] = disallow_additional(schema['items'])
        return schema

    for k, v in schema.get('properties', {}).items():
        schema['properties'][k] = disallow_additional(v)

    for k, v in schema.get('definitions', {}).items():
        schema['definitions'][k] = disallow_additional(v)

    schema['additionalProperties'] = False

    return schema


def test_examples_valid():
    with open('schema/project-level/project-package-schema.json') as f:
        schema = json.load(f)

    schema = disallow_additional(schema)

    validator = Draft4Validator(schema, format_checker=FormatChecker())

    paths = glob('docs/examples/*.json')

    for path in paths:
        if 'blank.json' not in path:
            with open(path) as f:
                data = json.load(f)

            errors = 0
            for error in validator.iter_errors(data):
                errors += 1
                warnings.warn(
                    f"{json.dumps(error.instance, indent=2)}\n"
                    f"{error.message} ({'/'.join(error.absolute_schema_path)})\n"
                )

            assert not errors, f'{path} is invalid. See warnings below.'
