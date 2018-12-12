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
import sys
from collections import OrderedDict
from copy import deepcopy

import requests

base_url = 'http://standard.open-contracting.org/profiles/ppp/latest/en/_static/patched/'
schema_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'project-level')
codelists_dir = os.path.join(schema_dir, 'codelists')
ppp_schema = requests.get(base_url + 'release-schema.json').json(object_pairs_hook=OrderedDict)


def copy_def(definition, replacements=None):
    value = deepcopy(ppp_schema['definitions'][definition])
    schema['definitions'][definition] = value
    if replacements:
        for keys, replacement in replacements.items():
            leaf = keys[-1]
            for key in keys[:-1]:
                value = value[key]
            value[leaf] = replacement(value[leaf])


def compare(actual, infra_list, ocds_list, prefix, suffix):
    actual = set(actual)

    # An editor might have added an infrastructure codelist, or copied an OCDS codelist, without updating this script.
    added = actual - infra_list - ocds_list
    if added:
        sys.exit('{prefix} has unexpected {items}: add to infra_{suffix} or ocds_{suffix} in borrow-schema.py?'.format(
            items=', '.join(added),
            prefix=prefix,
            suffix=suffix,
        ))

    # An editor might have removed an infrastructure codelist, without updating this script.
    removed = infra_list - actual
    if removed:
        sys.exit('{prefix} is missing {items}: remove from infra_{suffix} in borrow-schema.py?'.format(
            items=', '.join(removed),
            prefix=prefix,
            suffix=suffix,
        ))


with open(os.path.join(schema_dir, 'project-schema.json')) as f:
    schema = json.load(f, object_pairs_hook=OrderedDict)

infra_codelists = {
    '+documentType.csv',
    'contractingProcessStatus.csv',
    'contractNature.csv',
    'projectStatus.csv',
    'projectType.csv',
}
ocds_codelists = {
    'currency.csv',
    'documentType.csv',
    'geometryType.csv',
    'locationGazetteers.csv',
    'method.csv',
    'partyRole.csv',
    'releaseTag.csv',
}
compare(os.listdir(codelists_dir), infra_codelists, ocds_codelists,
        'schema/project-level/codelists', 'codelists')

infra_definitions = {
    'ContractingProcess',
    # Similar to OCDS release, and includes direction on how to populate from OCDS data.
    'ContractingProcessSummary',
    # Similar to linked release in OCDS record package.
    'LinkedRelease',
    'Variation',
}
ocds_definitions = {
    'Period',
    'Classification',
    'Location',
    'Value',
    'Organization',
    'OrganizationReference',
    'Address',
    'ContactPoint',
    'BudgetBreakdown',
    'Document',
    'Identifier',
}
compare(schema['definitions'], infra_definitions, ocds_definitions,
        'schema/project-level/project-schema.json#/definitions', 'definitions')

# Copy the OCDS codelists.
for basename in ocds_codelists:
    with open(os.path.join(schema_dir, 'codelists', basename), 'w') as f:
        f.write(requests.get(base_url + 'codelists/' + basename).text)

# The following definitions follow the same order as in project-schema.json.

copy_def('Period', {
    # Refer to project.
    ('description',): lambda s: s.replace('contracting process', 'project or contracting process'),
})

copy_def('Classification', {
    # Remove line item classifications from the definition.
    ('properties', 'scheme', 'description'): lambda s: s[:s.index(' For line item classifications,')],
})
# Remove the `itemClassificationScheme.csv` codelist.
del(schema['definitions']['Classification']['properties']['scheme']['codelist'])
del(schema['definitions']['Classification']['properties']['scheme']['openCodelist'])
# Remove the "uri" field, which is poorly used in OCDS implementations.
del(schema['definitions']['Classification']['properties']['uri'])

copy_def('Location')
# noqa: Original from ocds_location_extension:     "The location where activity related to this tender, contract or license will be delivered, or will take place. A location can be described by either a geometry (point location, line or polygon), or a gazetteer entry, or both."
schema['definitions']['Location']['description'] = "The location where activity related to this project will be delivered, or will take place. A location may be described using a geometry (point location, line or polygon), a gazetteer entry, an address, or a combination of these."  # noqa
# Add address to Location.
schema['definitions']['Location']['properties']['address'] = {
    'title': 'Address',
    'description': 'A physical address where works will take place.',
    '$ref': '#/definitions/Address',
}

copy_def('Value')

copy_def('Organization', {
    # Refer to project instead of contracting process.
    ('properties', 'roles', 'description'): lambda s: s.replace('contracting process', 'project'),
})
# Remove unneeded extensions and details from Organization.
del(schema['definitions']['Organization']['properties']['shareholders'])
del(schema['definitions']['Organization']['properties']['beneficialOwnership'])
del(schema['definitions']['Organization']['properties']['details'])

copy_def('OrganizationReference')

copy_def('Address')

copy_def('ContactPoint', {
    # Refer to project instead of contracting process.
    ('properties', 'name', 'description'): lambda s: s.replace('contracting process', 'project'),
})

copy_def('BudgetBreakdown')

copy_def('Document')
# noqa: Original from standard:                                                 "A short description of the document. We recommend descriptions do not exceed 250 words. In the event the document is not accessible online, the description field can be used to describe arrangements for obtaining a copy of the document.",
schema['definitions']['Document']['properties']['description']['description'] = "Where a link to a full document is provided, the description should provide a 1 - 3 paragraph summary of the information the document contains, and the `pageStart` field should be used to make sure readers can find the correct section of the document containing more information. Where there is no linked document available, the description field may contain all the information required by the current `documentType`. \n\nLine breaks in text (represented in JSON using `\\n\\n`) must be respected by systems displaying this information, and systems may also support basic HTML tags (H1-H6, B, I, U, strong, A and optionally IMG) or [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for formatting. "  # noqa
# noqa: Original from standard:                                         " direct link to the document or attachment. The server providing access to this document should be configured to correctly report the document mime type."
schema['definitions']['Document']['properties']['url']['description'] = "This should be a direct link to the document or web page where the information described by the current documentType exists."  # noqa

copy_def('Identifier')


with open(os.path.join(schema_dir, 'project-schema.json'), 'w') as f:
    json.dump(schema, f, ensure_ascii=False, indent=2, separators=(',', ': '))
    f.write('\n')
