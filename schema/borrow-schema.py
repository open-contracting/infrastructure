"""borrow-schema.py.

This script takes the full PPP extension schema as a basis (as this includes
most of the elements we need in OC for Infrastructure, and copies definitions
across into the Infrastructure Project Transparency Schema, making
modifications to titles or descriptions where required.

The goal of this is to make it easier to see where changes might be needed in
future to keep Project Level Data Specification aligned with OCDS
object definitions.

When major updates to OCDS take place, and OCDS for PPPs is updated, this script
should be run, and the diffs compared to see if changes to the project level data
specification should be made.
"""

import json
import os
from collections import OrderedDict

import requests

base_url = 'http://standard.open-contracting.org/profiles/ppp/latest/en/_static/patched/'
schema_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'project-level')


def copy_def(definition):
    schema['definitions'][definition] = pppSchema['definitions'][definition]


def copy_codelist(codelist):
    with open(os.path.join(schema_folder, 'codelists', codelist + '.csv'), 'w') as f:
        f.write(requests.get(base_url + 'codelists/' + codelist + '.csv').text)


pppSchema = requests.get(base_url + 'release-schema.json').json(object_pairs_hook=OrderedDict)

with open(os.path.join(schema_folder, 'project-schema.json')) as f:
    schema = json.load(f, object_pairs_hook=OrderedDict)


copy_codelist('releaseTag')
copy_codelist('currency')
copy_codelist('method')
copy_codelist('partyRole')
copy_codelist('documentType')
copy_codelist('geometryType')
copy_codelist('locationGazetteers')

copy_def('Identifier')
copy_def('Value')

copy_def('Period')
schema['definitions']['Period']['description'] = "Key events during a project or contracting process may have a known start date, end date, duration, or maximum extent (the latest date the period can extend to). In some cases, not all of these fields will have known or relevant values."  # noqa

copy_def('BudgetBreakdown')

# We need organisations, but not shareholder or beneficial ownership information.
copy_def('Organization')
copy_def('OrganizationReference')
del(schema['definitions']['Organization']['properties']['shareholders'])
del(schema['definitions']['Organization']['properties']['beneficialOwnership'])
del(schema['definitions']['Organization']['properties']['details'])
schema['definitions']['Organization']['properties']['roles']['description'] = str(schema['definitions']['Organization']['properties']['roles']['description']).replace('contracting process', 'project')  # noqa

copy_def('Address')

copy_def('ContactPoint')
schema['definitions']['ContactPoint']['properties']['name']['description'] = str(schema['definitions']['ContactPoint']['properties']['name']['description']).replace('contracting process', 'project')  # noqa

copy_def('Document')
schema['definitions']['Document']['properties']['description']['description'] = "Where a link to a full document is provided, the description should provide a 1 - 3 paragraph summary of the information the document contains, and the `pageStart` field should be used to make sure readers can find the correct section of the document containing more information. Where there is no linked document available, the description field may contain all the information required by the current `documentType`. \n\nLine breaks in text (represented in JSON using `\\n\\n`) must be respected by systems displaying this information, and systems may also support basic HTML tags (H1-H6, B, I, U, strong, A and optionally IMG) or [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for formatting. "  # noqa
schema['definitions']['Document']['properties']['url']['description'] = "This should be a direct link to the document or web page where the information described by the current documentType exists."  # noqa

# Recognising that the buyer address may not be appropriate for geolocation, but that projects may have a physical
# address, we add 'address' to location.
copy_def('Location')
schema['definitions']['Location']['description'] = "The location where activity related to this project will be delivered, or will take place. A location may be described using a geometry (point location, line or polygon), a gazetteer entry, an address, or a combination of these."  # noqa
schema['definitions']['Location']['properties']['address'] = {
    'title': 'Address',
    'description': 'A physical address where works will take place.',
    '$ref': '#/definitions/Address',
}

copy_def('Classification')
schema['definitions']['Classification']['properties']['scheme']['description'] = "An classification should be drawn from an existing scheme or list of codes. This field is used to indicate the scheme/codelist from which the classification is drawn."  # noqa
del(schema['definitions']['Classification']['properties']['scheme']['codelist'])
del(schema['definitions']['Classification']['properties']['scheme']['openCodelist'])
# The URI property has been poorly used within OCDS, so is removed from project level data specification.
del(schema['definitions']['Classification']['properties']['uri'])

with open(os.path.join(schema_folder, 'project-schema.json'), 'w') as f:
    json.dump(schema, f, ensure_ascii=False, indent=2, separators=(',', ': '))
    f.write('\n')
