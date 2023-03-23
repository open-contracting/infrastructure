#!/usr/bin/env python
import csv
import json
import re
import sys
import warnings
from collections import OrderedDict
from copy import deepcopy
from io import StringIO
from pathlib import Path

import click
import requests
from ocdsextensionregistry import ProfileBuilder
from ocdskit.mapping_sheet import mapping_sheet
from ocdskit.schema import add_validation_properties

basedir = Path(__file__).resolve().parent
referencedir = basedir / 'docs' / 'reference'


def get(url):
    """
    GETs a URL and returns the response. Raises an exception if the status code is not successful.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response


def csv_reader(url):
    """
    Reads a CSV from a URL and returns a ``csv.DictReader`` object.
    """
    return csv.DictReader(StringIO(get(url).text))


def coerce_to_list(data, key):
    """
    Returns the value of the ``key`` key in the ``data`` mapping. If the value is a string, wraps it in an array.
    """
    item = data.get(key, [])
    if isinstance(item, str):
        return [item]
    return item


def edit_code(row, oc4ids_codes, source):
    """
    If the row's "Code" is in the ``oc4ids_codes`` list, adds " or project" after "contracting process" in the row's
    "Description" and sets the row's "Source" to ``"OC4IDS"``. Otherwise, sets the row's "Source" to ``source``.
    """
    if row['Code'] in oc4ids_codes:
        row['Description'] = re.sub(r'(?<=contracting process\b)', ' or project', row['Description'])
        row['Description'] = re.sub(r'(?<=contracting processes\b)', ' or projects', row['Description'])
        row['Source'] = 'OC4IDS'
    else:
        row['Source'] = source
    return row


def traverse(schema_action=None, object_action=None):
    """
    Implements common logic for walking through the schema.
    """
    if object_action is None:
        def object_action(value):
            pass

    def method(schema, pointer=''):
        schema_action(schema, pointer)

        if 'properties' in schema:
            for key, value in schema['properties'].items():
                new_pointer = f'{pointer}/{key}'

                prop_type = coerce_to_list(value, 'type')
                object_action(value)

                if 'object' in prop_type:
                    method(value, pointer=new_pointer)
                elif 'array' in prop_type:
                    items_type = coerce_to_list(value['items'], 'type')
                    object_action(value['items'])

                    # Recursing into arrays of arrays or arrays of objects hasn't been implemented.
                    if ('object' in items_type or 'array' in items_type
                            and new_pointer != '/Location/geometry/coordinates'):
                        raise NotImplementedError(f'{new_pointer}/items has unexpected type {items_type}')
        elif pointer != '/Observation/dimensions':
            warnings.warn(f'Missing "properties" key at {pointer}')

        for key, value in schema.get('definitions', {}).items():
            method(value, pointer=f'{pointer}/{key}')

    return method


# Similar in structure to `add_versioned` in the standard's `make_versioned_release_schema.py`.
def remove_null_and_pattern_properties(*args):
    """
    Removes the "patternProperties" key, ``"null"`` from the "type" key, and ``None`` from the "enum" key.
    """

    def schema_action(schema, pointer):
        schema.pop('patternProperties', None)

    def object_action(value):
        if 'type' in value and isinstance(value['type'], list) and 'null' in value['type']:
            value['type'].remove('null')
        if 'enum' in value and None in value['enum']:
            value['enum'].remove(None)

    traverse(schema_action, object_action)(*args)


def remove_deprecated_properties(*args):
    """
    Removes "deprecated" properties.
    """

    def schema_action(schema, pointer):
        if 'properties' in schema:
            for key in list(schema['properties']):
                if 'deprecated' in schema['properties'][key]:
                    del schema['properties'][key]
        elif pointer != '/Observation/dimensions':
            warnings.warn(f'Missing "properties" key at {pointer}')

    traverse(schema_action)(*args)


def remove_integer_identifier_types(*args):
    """
    Sets all ``id`` fields to allow only strings, not integers.
    """

    def schema_action(schema, pointer):
        if 'properties' in schema:
            if 'id' in schema['properties']:
                schema['properties']['id']['type'] = 'string'
        elif pointer != '/Observation/dimensions':
            warnings.warn(f'Missing "properties" key at {pointer}')

    traverse(schema_action)(*args)


def compare(actual, infra_list, ocds_list, prefix, suffix):
    """
    Aborts if ``infra_list`` contains values not in ``actual``, or if ``actual`` contains values not in ``infra_list``
    or ``ocds_list``. This ensures an editor updates this script when codelists or definitions are added to OC4IDS.
    """

    actual = set(actual)

    # An editor might have added an infrastructure codelist, or copied an OCDS codelist, without updating this script.
    added = actual - infra_list - ocds_list
    if added:
        sys.exit(f'{prefix} has unexpected {", ".join(added)}: add to infra_{suffix} or ocds_{suffix}?')

    # An editor might have removed an infrastructure codelist, without updating this script.
    removed = infra_list - actual
    if removed:
        sys.exit(f'{prefix} is missing {", ".join(removed)}: remove from infra_{suffix}?')


def get_definition_references(schema, defn, parents=None, project_schema=None, include_nested=True):
    """
    Recursively generate a list of JSON pointers that reference a definition in JSON schema.

    :param schema: The JSON schema
    :defn: The name of the definition
    :parents: A list of the parents of schema
    :project_schema: The full project schema
    "include_nested: Whether to include nested references
    """

    references = []

    if parents is None:
        parents = []

    if project_schema is None:
        project_schema = schema

    if 'properties' in schema:
        for key, value in schema['properties'].items():
            if value.get('type') == 'array' and '$ref' in value['items']:
                if value['items']['$ref'] == f"#/definitions/{defn}":
                    references.append(parents + [key, '0'])
                elif include_nested:
                    references.extend(get_definition_references(
                        project_schema['definitions'][value['items']['$ref'].split('/')[-1]],
                        defn,
                        parents + [key, '0'],
                        project_schema, include_nested))
            elif '$ref' in value:
                if value['$ref'] == f"#/definitions/{defn}":
                    references.append(parents + [key])
                elif include_nested:
                    references.extend(get_definition_references(
                        project_schema['definitions'][value['$ref'].split('/')[-1]],
                        defn,
                        parents + [key],
                        project_schema, include_nested))
            elif 'properties' in value:
                references.extend(get_definition_references(value,
                                                            defn,
                                                            parents + [key],
                                                            project_schema,
                                                            include_nested))

    if 'definitions' in schema:
        for key, value in schema['definitions'].items():
            references.extend(get_definition_references(value, defn, [key], project_schema, include_nested))

    return references


def update_sub_schema_reference(schema):
    """Update docs/reference/schema.md"""

    # Load schema reference
    with (referencedir / 'schema.md').open() as f:
        schema_reference = f.readlines()

    # Preserve content that appears before the generated reference content for each sub-schema
    sub_schema_index = schema_reference.index("## Sub-schemas\n") + 3

    for i in range(sub_schema_index, len(schema_reference)):
        if schema_reference[i][:4] == "### ":
            defn = schema_reference[i][4:-1]

            # Drop definitions that don't appear in the schema
            if defn in schema["definitions"]:
                schema["definitions"][defn]["content"] = []
                j = i+1

                while j < len(schema_reference) and not schema_reference[j].startswith(f"`{defn}` is defined as:"):
                    schema["definitions"][defn]["content"].append(schema_reference[j])
                    j = j+1

    # Preserve introductory content up to and including the sentence below the ## Sub-schema heading
    schema_reference = schema_reference[:sub_schema_index]
    schema_reference.append("\n")

    # Generate standard reference content for each definition
    for defn, definition in schema["definitions"].items():
        definition["content"] = definition.get("content", [])

        # Add heading
        definition["content"].insert(0, f"### {defn}\n")

        # Add description
        definition["content"].extend([
            f"`{defn}` is defined as:\n\n",
            "```{jsoninclude-quote} ../../schema/project-level/project-schema.json\n",
            f":jsonpointer: /definitions/{defn}/description\n",
            "```\n\n"
        ])

        # Add a list of properties that reference this definition
        definition["references"] = get_definition_references(schema, defn, include_nested=False)
        definition["content"].append("This sub-schema is referenced by the following properties:\n")

        for ref in definition["references"]:
            # noqa: Remove array indices because they do not appear in the HTML anchors generated by the json schema directive
            ref = [part for part in ref if part != '0']

            url = 'project-schema.json,'

            # Omit nested references
            if ref[0] in schema['definitions']:
                url += f"/definitions/{ref[0]},{'/'.join(ref[1:])}"
            else:
                url += f",{'/'.join(ref)}"

            definition["content"].append(f"* [`{'/'.join(ref)}`]({url})\n")

        # Add schema table
        properties_to_collapse = []
        for key, value in definition['properties'].items():
            if value.get('type') != 'object':
                properties_to_collapse.append(key)

        definition["content"].extend([
            f"\nEach `{defn}` has the following fields:\n\n",
            "`````{tab-set}\n\n",
            "````{tab-item} Schema\n\n",
            "```{jsonschema} ../../schema/project-level/project-schema.json\n",
            f":pointer: /definitions/{defn}\n",
            f":collapse: {','.join(properties_to_collapse)}\n"
            ":addtargets:\n"
            "```\n\n",
            "````\n\n",
            "````{tab-item} Examples\n\n"
        ])

        # Paths that don't appear in the example data at all
        paths_to_skip = ['forecasts/0/observations/0/value', 'metrics/0/observations/0/value']

        # Add examples
        definition["references"] = get_definition_references(schema, defn)
        for ref in definition["references"]:
            if ref[0] not in schema['definitions'] and '/'.join(ref) not in paths_to_skip:
                if ref[-1] == '0':
                    ref.pop(-1)

                definition["content"].extend([
                  "```{jsoninclude} ../../docs/examples/example.json\n",
                  f":jsonpointer: /projects/0/{'/'.join(ref)}\n",
                  f":title: {'/'.join(ref)}\n",
                  "```\n\n"
                ])

        definition["content"].extend([
            "````\n\n",
            "`````\n\n"
        ])

        schema_reference.extend(definition["content"])

    # Paths that don't appear in the example data, but for which there is an alternative
    paths_to_replace = {
      '/projects/0/contractingProcesses/0/summary/modifications/0/oldContractValue': (
        '/projects/0/contractingProcesses/0/summary/modifications/2/oldContractValue'),
      '/projects/0/contractingProcesses/0/summary/modifications/0/newContractValue': (
        '/projects/0/contractingProcesses/0/summary/modifications/2/newContractValue')
    }

    for key, value in paths_to_replace.items():
        index = schema_reference.index(f":jsonpointer: {key}\n")
        del schema_reference[index]
        schema_reference.insert(index, f":jsonpointer: {value}\n")

    with (referencedir / 'schema.md').open('w') as f:
        f.writelines(schema_reference)


@click.group()
def cli():
    pass


@cli.command()
def pre_commit():
    """
    Update docs/reference/schema.md and _static/i8n.csv
    """
    with (basedir / 'schema' / 'project-level' / 'project-schema.json').open() as f:
        schema = json.load(f)

    # Update schema reference documentation
    update_sub_schema_reference(schema)

    # Generate a CSV file of fields that can contain non-English text.
    _, rows = mapping_sheet(schema, include_codelist=True, include_deprecated=False)

    with (basedir / 'docs' / '_static' / 'i18n.csv').open('w') as f:
        fieldnames = ['path', 'title', 'translatable', 'notes']

        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n', extrasaction='ignore')
        writer.writeheader()

        for row in rows:
            row['translatable'] = row['type'] == 'string' and not row['values'] and not row['codelist']

            if row['path'] in ('id', 'contractingProcesses/id', 'contractingProcesses/summary/ocid'):
                row['notes'] = 'Only the part of the identifier following the prefix can be internationalized.'
            elif row['path'] in ('forecasts/observations/measure', 'metrics/observation/measure'):
                row['notes'] = 'Only string measures can be internationalized.'

            writer.writerow(row)


@cli.command()
@click.option('--ppp-base-url',
              default='https://standard.open-contracting.org/profiles/ppp/latest/en/_static/patched/')
def update(ppp_base_url):
    """
    Align OC4IDS with OCDS.

    It uses OCDS for PPPs as a basis, because it includes most definitions and codelists needed in OC4IDS. It copies
    definitions, properties and codelists across, making modifications as required.

    Run this command for every release of OCDS for PPPs, review any changes to schemas or codelists, and update the
    command as needed.

    Some OC4IDS-specific definitions have fields with the same names as in OCDS-specific definitions, notably:

    - procurementMethod
    - procurementMethodDetails
    - tenderers

    The descriptions of most other such fields have diverged. As such, the command makes no effort to copy the
    descriptions of such fields, and instead leaves this up to the editor.
    """

    def copy_element(name, replacements=None, root='definitions'):
        """
        Copies definitions or properties from the OCDS for PPPs schema to the OC4IDS schema.

        :param name: The name of the definition or property to copy
        :param replacements: A dict whose keys are tuples containing the path of the field in which the replacement is
                             to be performed and whose values are a function to perform the replacements
        :param str root: "definitions" or "properties"
        """
        value = deepcopy(ppp_schema[root][name])
        schema[root][name] = value
        if replacements:
            for keys, replacement in replacements.items():
                leaf = keys[-1]
                for key in keys[:-1]:
                    value = value[key]
                value[leaf] = replacement(value[leaf])

    ocds_base_url = 'https://standard.open-contracting.org/1.1/en/'

    builder = ProfileBuilder('1__1__5', {'budget': 'master'})
    ppp_schema = get(f'{ppp_base_url}release-schema.json').json(object_pairs_hook=OrderedDict)
    ppp_schema = builder.patched_release_schema(schema=ppp_schema)

    schema_dir = basedir / 'schema' / 'project-level'
    codelists_dir = schema_dir / 'codelists'

    with (schema_dir / 'project-schema.json').open() as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)

    infra_codelists = {
        'contractingProcessStatus.csv',
        'contractNature.csv',
        'metricID.csv',
        'modificationType.csv',
        'projectSector.csv',
        'projectStatus.csv',
        'projectType.csv',
        'relatedProjectScheme.csv',
        'relatedProject.csv',
    }
    ocds_codelists = {
        'currency.csv',
        'documentType.csv',
        'geometryType.csv',
        # Uncomment once OCDS for PPPs is updated for OCDS 1.2.
        # 'language.csv',
        'locationGazetteers.csv',
        'method.csv',
        'partyRole.csv',
        'releaseTag.csv',
        'unitClassificationScheme.csv',
    }
    compare([path.name for path in codelists_dir.iterdir()], infra_codelists, ocds_codelists,
            'schema/project-level/codelists', 'codelists')

    infra_definitions = {
        'ContractingProcess',
        'ContractingProcessSummary',  # Similar to individual release in OCDS
        'LinkedRelease',  # Similar to linked release in OCDS
        'Modification',
        'RelatedProject',  # Similar to relatedProcess in OCDS
        'Person',
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
        'Metric',
        'Observation',
        'Transaction',
    }
    compare(schema['definitions'], infra_definitions, ocds_definitions,
            'schema/project-level/project-schema.json#/definitions', 'definitions')

    # Originally from https://docs.google.com/spreadsheets/d/1ttXgMmmLvqBlPRi_4jAJhIobjnCiwMv13YwGfFOnoJk/edit#gid=0
    ignore = {
        # https://github.com/open-contracting/infrastructure/issues/269
        'finalAudit',
        # https://github.com/open-contracting/standard/issues/870
        'contractSchedule',
        # PPP-specific code or description
        'needsAssessment',
        'projectAdditionality',
        'financeAdditionality',
        'pppModeRationale',
        'riskComparison',
        'discountRate',
        'equityTransferCaps',
        'financeArrangements',
        'guaranteeReports',
        'grants',
        'servicePayments',
        'landTransfer',
        'assetTransfer',
        'revenueShare',
        'otherGovernmentSupport',
        'tariffMethod',
        'tariffReview',
        'tariffs',
        'tariffIllustration',
        'handover',
        'financialStatement',
    }

    # Copy the OCDS codelists.
    for basename in ocds_codelists:
        path = schema_dir / 'codelists' / basename

        if basename in ('documentType.csv', 'partyRole.csv'):
            with open(path) as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames

                oc4ids_rows = []
                oc4ids_codes = []
                for row in reader:
                    if row['Source'] == 'OC4IDS':
                        oc4ids_rows.append(row)
                        oc4ids_codes.append(row['Code'])

        with open(path, 'w') as f:
            if basename == 'documentType.csv':
                io = StringIO()
                writer = csv.DictWriter(io, fieldnames, lineterminator='\n', extrasaction='ignore')
                writer.writeheader()
                seen = []

                # Add codes from OCDS for PPPs.
                reader = csv_reader(f'{ppp_base_url}codelists/{basename}')
                for row in reader:
                    if row['Code'] not in ignore:
                        seen.append(row['Code'])
                        # These codes' descriptions are entirely new.
                        if row['Code'] in ('environmentalImpact',):
                            row = next(oc4ids_row for oc4ids_row in oc4ids_rows if oc4ids_row['Code'] == row['Code'])
                        else:
                            edit_code(row, oc4ids_codes, 'OCDS for PPPs')
                        writer.writerow(row)

                # Add codes from OCDS.
                reader = csv_reader(f'{ocds_base_url}codelists/documentType.csv')
                for row in reader:
                    if row['Code'] not in seen and row['Code'] not in ignore:
                        seen.append(row['Code'])
                        edit_code(row, oc4ids_codes, 'OCDS')
                        writer.writerow(row)

                # Add pre-existing codes from OC4IDS.
                writer.writerows(row for row in oc4ids_rows if row['Code'] not in seen)

                text = io.getvalue()
            elif basename == 'partyRole.csv':
                io = StringIO()
                writer = csv.DictWriter(io, fieldnames, lineterminator='\n', extrasaction='ignore')
                writer.writeheader()
                seen = []

                # Add codes from OCDS.
                reader = csv_reader(f'{ocds_base_url}codelists/partyRole.csv')
                for row in reader:
                    if row['Code'] not in seen:
                        seen.append(row['Code'])
                        edit_code(row, oc4ids_codes, 'OCDS')
                        writer.writerow(row)

                # Add pre-existing codes from OC4IDS.
                writer.writerows(row for row in oc4ids_rows if row['Code'] not in seen)

                text = io.getvalue()
            else:
                text = get(f'{ppp_base_url}codelists/{basename}').text

            f.write(text)

    # Copy properties

    copy_element('language', {
        ('title',): lambda s: s.replace('Release language', 'Language'),
    }, root='properties')

    # Copy definitions. The following definitions follow the same order as in project-schema.json.

    copy_element('Period', {
        # Refer to project.
        ('description',): lambda s: s.replace('contracting process', 'project or contracting process'),
    })

    copy_element('Classification', {
        # Remove line item classifications from the definition.
        ('properties', 'scheme', 'description'): lambda s: s[:s.index(' For line item classifications,')],
    })
    # Remove the `itemClassificationScheme.csv` codelist.
    del schema['definitions']['Classification']['properties']['scheme']['codelist']
    del schema['definitions']['Classification']['properties']['scheme']['openCodelist']

    copy_element('Location')
    # Original from ocds_location_extension:     "The location where activity related to this tender, contract or license will be delivered, or will take place. A location can be described by either a geometry (point location, line or polygon), or a gazetteer entry, or both." # noqa: E501
    schema['definitions']['Location']['description'] = "The location where activity related to this project will be delivered, or will take place. A location may be described using a geometry (point location, line or polygon), a gazetteer entry, an address, or a combination of these."  # noqa: E501
    # Add id to Location.
    schema['definitions']['Location']['properties']['id'] = {
        'title': 'Identifier',
        'description': 'A local identifier for this location, unique within the array this location appears in.',
        'type': 'string',
        'minLength': 1,
    }
    # Add address to Location.
    schema['definitions']['Location']['properties']['address'] = {
        'title': 'Address',
        'description': 'A physical address where works will take place.',
        '$ref': '#/definitions/Address',
    }
    schema['definitions']['Location']['properties'].move_to_end('id', last=False)
    schema['definitions']['Location']['required'] = ['id']

    # Set stricter validation on gazetteer identifiers
    schema['definitions']['Location']['properties']['gazetteer']['properties']['identifiers']['uniqueItems'] = True

    copy_element('Value')

    copy_element('Organization', {
        # Refer to project instead of contracting process, link to infrastructure codelist instead of PPP codelist.
        ('properties', 'roles', 'description'): lambda s: s.replace('contracting process', 'project').replace('profiles/ppp/latest/en/', 'infrastructure/{{version}}/{{lang}}/')  # noqa: E501
    })
    # Remove unneeded extensions and details from Organization.
    del schema['definitions']['Organization']['properties']['shareholders']
    del schema['definitions']['Organization']['properties']['beneficialOwnership']
    del schema['definitions']['Organization']['properties']['details']

    # Set stricter validation on party roles
    schema['definitions']['Organization']['properties']['roles']['uniqueItems'] = True

    # Add `people` property to OrganizationReference
    schema['definitions']['Organization']['properties']['people'] = {
        "title": "People",
        "description": "People associated with, representing, or working on behalf of this organization in respect of this project.",  # noqa: E501
        "type": "array",
        "items": {
            "$ref": "#/definitions/Person"
        },
        "uniqueItems": True
    }

    copy_element('OrganizationReference')

    copy_element('Address')

    copy_element('ContactPoint', {
        # Refer to project instead of contracting process.
        ('properties', 'name', 'description'): lambda s: s.replace('contracting process', 'project'),
    })

    copy_element('BudgetBreakdown')

    copy_element('Document', {
        # Link to infrastructure codelist instead of PPP codelist
        ('properties', 'documentType', 'description'): lambda s: s.replace('profiles/ppp/latest/en/', 'infrastructure/{{version}}/{{lang}}/'),  # noqa: E501
    })
    # Original from standard:                                                 "A short description of the document. We recommend descriptions do not exceed 250 words. In the event the document is not accessible online, the description field can be used to describe arrangements for obtaining a copy of the document.", # noqa: E501
    schema['definitions']['Document']['properties']['description']['description'] = "Where a link to a full document is provided, the description should provide a 1 - 3 paragraph summary of the information the document contains, and the `pageStart` field should be used to make sure readers can find the correct section of the document containing more information. Where there is no linked document available, the description field may contain all the information required by the current `documentType`. \n\nLine breaks in text (represented in JSON using `\\n\\n`) must be respected by systems displaying this information, and systems may also support basic HTML tags (H1-H6, B, I, U, strong, A and optionally IMG) or [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for formatting. "  # noqa: E501
    # Original from standard:                                         " direct link to the document or attachment. The server providing access to this document should be configured to correctly report the document mime type." # noqa: E501
    schema['definitions']['Document']['properties']['url']['description'] = "This should be a direct link to the document or web page where the information described by the current documentType exists."  # noqa: E501

    copy_element('Identifier')

    copy_element('Metric', {
        ('properties', 'id', 'description'): lambda s: s.replace('contracting process', 'contracting process or project')}),  # noqa: E501

    schema['definitions']['Metric']['description'] = "Metrics are used to set out forecast and actual metrics targets for a project: for example, planned and actual physical and financial progress over time."  # noqa: E501
    # Original from standard: "Metrics are used to set out targets and results from a contracting process. During the planning and tender sections, a metric indicates the anticipated results. In award and contract sections it indicates the awarded/contracted results. In the implementation section it is used to provide updates on actually delivered results, also known as outputs." # noqa: E501

    copy_element('Observation')
    # Remove the `relatedImplementationMilestone` property
    del schema['definitions']['Observation']['properties']['relatedImplementationMilestone']

    copy_element('Transaction')

    remove_null_and_pattern_properties(schema)
    remove_integer_identifier_types(schema)
    remove_deprecated_properties(schema)
    add_validation_properties(schema)

    with (schema_dir / 'project-schema.json').open('w') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
        f.write('\n')


if __name__ == '__main__':
    cli()
