#!/usr/bin/env python
import csv
import json
import re
import sys
import warnings
from collections import OrderedDict, defaultdict
from copy import deepcopy
from io import StringIO
from pathlib import Path

import click
import json_merge_patch
import mdformat
import requests
import yaml
from docutils import nodes
from jsonschema import FormatChecker
from jsonschema.validators import Draft4Validator
from ocdsextensionregistry import ProfileBuilder
from ocdskit.mapping_sheet import mapping_sheet
from ocdskit.schema import add_validation_properties

basedir = Path(__file__).resolve().parent
referencedir = basedir / 'docs' / 'reference'


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def str_representer(dumper, data):
    # Use the literal style on multiline strings to reduce quoting, instead of the single-quoted style (default).
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|" if "\n" in data else None)


Dumper.add_representer(str, str_representer)


def get(url):
    """
    GET a URL and returns the response. Raises an exception if the status code is not successful.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response


def csv_reader(url):
    """
    Read a CSV from a URL and returns a ``csv.DictReader`` object.
    """
    return csv.DictReader(StringIO(get(url).text))


def write_yaml_file(filename, data):
    with open(filename, "w") as f:
        # Make it easier to see indentation. Avoid line wrapping. sort_keys is True by default.
        yaml.dump(data, f, Dumper=Dumper, indent=4, width=1000, sort_keys=False)


def traverse(schema_action=None, object_action=None):
    """
    Common logic for walking through the schema.
    """
    if object_action is None:
        def object_action(value):
            pass

    def _coerce_to_list(data, key):
        """
        Return the value of the ``key`` key in the ``data`` mapping. If the value is a string, wraps it in an array.
        """
        item = data.get(key, [])
        if isinstance(item, str):
            return [item]
        return item

    def _method(schema, pointer=''):
        schema_action(schema, pointer)

        if 'properties' in schema:
            for key, value in schema['properties'].items():
                new_pointer = f'{pointer}/{key}'

                prop_type = _coerce_to_list(value, 'type')
                object_action(value)

                if 'object' in prop_type:
                    _method(value, pointer=new_pointer)
                elif 'array' in prop_type:
                    items_type = _coerce_to_list(value['items'], 'type')
                    object_action(value['items'])

                    # Recursing into arrays of arrays or arrays of objects hasn't been implemented.
                    if (
                        'object' in items_type
                        or 'array' in items_type
                        and new_pointer != '/Location/geometry/coordinates'
                    ):
                        raise NotImplementedError(f'{new_pointer}/items has unexpected type {items_type}')
        elif pointer != '/Observation/dimensions':
            warnings.warn(f'Missing "properties" key at {pointer}')

        for key, value in schema.get('definitions', {}).items():
            _method(value, pointer=f'{pointer}/{key}')

    return _method


@click.group()
def cli():
    pass


@cli.command()
def pre_commit():
    """
    Update docs/reference/schema.md and _static/i8n.csv
    """

    def _get_definition_references(schema, defn, parents=None, project_schema=None, include_nested=True):
        """
        Recursively generate a list of JSON pointers that reference a definition in JSON schema.

        :param schema: The JSON schema
        :param defn: The name of the definition
        :param parents: A list of the parents of schema
        :param project_schema: The full project schema
        :param include_nested: Whether to include nested references
        """
        references = []

        if parents is None:
            parents = []

        if project_schema is None:
            project_schema = schema

        if 'properties' in schema:
            for key, value in schema['properties'].items():
                if value.get('type') in ['array', ['array']] and '$ref' in value['items']:
                    if value['items']['$ref'] == f"#/definitions/{defn}":
                        references.append(parents + [key, '0'])
                    elif include_nested:
                        references.extend(_get_definition_references(
                            project_schema['definitions'][value['items']['$ref'].split('/')[-1]],
                            defn,
                            parents + [key, '0'],
                            project_schema, include_nested))
                elif '$ref' in value:
                    if value['$ref'] == f"#/definitions/{defn}":
                        references.append(parents + [key])
                    elif include_nested:
                        references.extend(_get_definition_references(
                            project_schema['definitions'][value['$ref'].split('/')[-1]],
                            defn,
                            parents + [key],
                            project_schema, include_nested))
                elif 'properties' in value:
                    references.extend(
                        _get_definition_references(value, defn, parents + [key], project_schema, include_nested)
                    )

        if 'definitions' in schema:
            for key, value in schema['definitions'].items():
                references.extend(_get_definition_references(value, defn, [key], project_schema, include_nested))

        return references

    def _update_sub_schema_reference(schema):
        """
        Update docs/reference/schema.md
        """
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

        # Generate standard reference content for each definition
        for defn, definition in schema["definitions"].items():
            definition["content"] = definition.get("content", [])

            # Add heading
            definition["content"].insert(0, f"\n### {defn}\n")

            # Add description
            if definition["content"][-1] != "\n":
                definition["content"].append("\n")

            definition["content"].extend([
                f"`{defn}` is defined as:\n\n",
                f"```{{field-description}} ../../build/current_lang/project-schema.json /definitions/{defn}\n",
                "```\n\n"
            ])

            # Add a list of properties that reference this definition
            definition["references"] = _get_definition_references(schema, defn, include_nested=False)
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
                if value.get('type') not in ['object', ['object']]:
                    properties_to_collapse.append(key)

            definition["content"].extend([
                f"\nEach `{defn}` has the following fields:\n\n",
                "`````{tab-set}\n\n",
                "````{tab-item} Schema\n\n",
                "```{jsonschema} ../../build/current_lang/project-schema.json\n",
                f":pointer: /definitions/{defn}\n",
                f":collapse: {','.join(properties_to_collapse)}\n"
                ":addtargets:\n"
                "```\n\n",
                "````\n\n",
                "````{tab-item} Examples\n\n"
            ])

            # Paths that don't appear in the example data at all
            paths_to_skip = [
                'forecasts/0/observations/0/value',
                'metrics/0/observations/0/value',
                'parties/0/beneficialOwners/0',
                'parties/0/people/0/address',
                'parties/0/people/0/identifier',
                'contractingProcesses/0/summary/finance',
                'contractingProcesses/1/summary/finance',
                'contractingProcesses/2/summary/finance',
                'social/consultationMeetings/0/publicOffice',
            ]

            # Add examples
            definition["references"] = _get_definition_references(schema, defn)
            for ref in definition["references"]:
                if ref[0] not in schema['definitions'] and not any(p == '/'.join(ref)[:len(p)] for p in paths_to_skip):
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
                "`````\n"
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

    with (basedir / 'schema' / 'project-level' / 'project-schema.json').open() as f:
        schema = json.load(f)

    # Update schema reference documentation
    _update_sub_schema_reference(schema)

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


# https://raw.githubusercontent.com/open-contracting-extensions/public-private-partnerships/1.0-dev/schema/patched/
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

    def _edit_code(row, oc4ids_codes, source):
        """
        If the row's Code is in the ``oc4ids_codes`` list, add " or project" after "contracting process" in the row's
        Description and sets the row's Source to ``"OC4IDS"``. Otherwise, set the row's Source to ``source``.
        """
        if row['Code'] in oc4ids_codes:
            row['Description'] = re.sub(r'(?<=contracting process\b)', ' or project', row['Description'])
            row['Description'] = re.sub(r'(?<=contracting processes\b)', ' or projects', row['Description'])
            row['Source'] = 'OC4IDS'
        else:
            row['Source'] = source
        return row

    def _merge_codes(sources, fieldnames, basename, ignore, oc4ids_codes, oc4ids_rows):
        io = StringIO()
        writer = csv.DictWriter(io, fieldnames, lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        seen = []

        for source in sources:
            reader = csv_reader(f"{ocds_base_url if source == 'OCDS' else ppp_base_url}codelists/{basename}")
            for row in reader:
                if row['Code'] not in seen and row['Code'] not in ignore:
                    seen.append(row['Code'])
                    _edit_code(row, oc4ids_codes, source)
                    writer.writerow(row)

        # Add pre-existing codes from OC4IDS.
        writer.writerows(row for row in oc4ids_rows if row['Code'] not in seen)

        return io.getvalue()

    def _copy_element(name, replacements=None, root='definitions'):
        """
        Copy definitions or properties from the OCDS for PPPs schema to the OC4IDS schema.

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

    # Similar in structure to `add_versioned` in the standard's `make_versioned_release_schema.py`.
    def _remove_null_and_pattern_properties(*args):
        """
        Remove the "patternProperties" key, ``"null"`` from the "type" key, and ``None`` from the "enum" key.
        """

        def __schema_action(schema, pointer):
            schema.pop('patternProperties', None)

        def __object_action(value):
            if 'type' in value and isinstance(value['type'], list) and 'null' in value['type']:
                value['type'].remove('null')
            if 'enum' in value and None in value['enum']:
                value['enum'].remove(None)

        traverse(__schema_action, __object_action)(*args)

    def _remove_deprecated_properties(*args):
        """
        Remove "deprecated" properties.
        """

        def __schema_action(schema, pointer):
            if 'properties' in schema:
                for key in list(schema['properties']):
                    if 'deprecated' in schema['properties'][key]:
                        del schema['properties'][key]
            elif pointer != '/Observation/dimensions':
                warnings.warn(f'Missing "properties" key at {pointer}')

        traverse(__schema_action)(*args)

    def _remove_integer_identifier_types(*args):
        """
        Set all ``id`` fields to allow only strings, not integers.
        """

        def __schema_action(schema, pointer):
            if 'properties' in schema:
                if 'id' in schema['properties']:
                    schema['properties']['id']['type'] = 'string'
            elif pointer != '/Observation/dimensions':
                warnings.warn(f'Missing "properties" key at {pointer}')

        traverse(__schema_action)(*args)

    def _compare(actual, infra_list, ocds_list, prefix, suffix):
        """
        Exit if ``infra_list`` contains values not in ``actual``, or if ``actual`` contains values not in ``ocds_list``
        or ``infra_list``. This ensures editors update this script when codelists or definitions are added to OC4IDS.
        """
        actual = set(actual)

        # An editor might've added an infrastructure codelist or copied an OCDS codelist, without updating this script.
        added = actual - infra_list - ocds_list
        if added:
            sys.exit(f'{prefix} has unexpected {", ".join(added)}: add to infra_{suffix} or ocds_{suffix}?')

        # An editor might've removed an infrastructure codelist, without updating this script.
        removed = infra_list - actual
        if removed:
            sys.exit(f'{prefix} is missing {", ".join(removed)}: remove from infra_{suffix}?')

    ocds_base_url = 'https://standard.open-contracting.org/1.1/en/'

    builder = ProfileBuilder(
        '1__1__5',
        {
            'budget': 'master',
            'transaction_milestones': 'master',
            'beneficialOwners': 'master',
            'organizationClassification': '1.1',
        }
    )
    response = get(f'{ppp_base_url}release-schema.json')
    ppp_schema = json.loads(response.text.replace('{{version}}', '1.1').replace('{{lang}}', 'en'))
    ppp_schema = builder.patched_release_schema(schema=ppp_schema)

    schema_dir = basedir / 'schema' / 'project-level'
    codelists_dir = schema_dir / 'codelists'

    with (schema_dir / 'project-schema.json').open() as f:
        schema = json.load(f)

    infra_codelists = {
        'classificationScheme.csv',
        'climateMeasures.csv',
        'climateOversightTypes.csv',
        'conservationMeasure.csv',
        'constructionMaterial.csv',
        'contractingProcessStatus.csv',
        'contractNature.csv',
        'costCategory.csv',
        'country.csv',  # move to ocds_codelists for OCDS 1.2
        'environmentalGoal.csv',
        'laborObligations.csv',
        'metricID.csv',
        'modificationType.csv',
        'policyAlignment.csv',
        'projectSector.csv',
        'projectStatus.csv',
        'projectType.csv',
        'relatedProject.csv',
        'relatedProjectScheme.csv',
        'sustainabilityStrategy.csv',
    }
    ocds_codelists = {
        'currency.csv',
        'documentType.csv',
        'geometryType.csv',
        'locationGazetteers.csv',
        'method.csv',
        'partyRole.csv',
        'releaseTag.csv',
        'unitClassificationScheme.csv',
        'milestoneType.csv',
        'milestoneStatus.csv',
        'milestoneCode.csv',
        'assetClass.csv',
        'debtRepaymentPriority.csv',
        'financingArrangementType.csv',
        'financingPartyType.csv',
    }
    _compare(
        [path.name for path in codelists_dir.iterdir()],
        infra_codelists, ocds_codelists, 'schema/project-level/codelists', 'codelists'
    )

    infra_definitions = {
        'Beneficiary',
        'Benefit',
        'BudgetBreakdowns',
        'ClimateMeasure',
        'ConservationMeasure',
        'ContractingProcess',
        'ContractingProcessSummary',  # Similar to individual release in OCDS
        'Cost',
        'CostGroup',
        'CostMeasurement',
        'HealthAndSafety',
        'LaborObligations',
        'LinkedRelease',  # Similar to linked release in OCDS
        'Meeting',
        'Modification',
        'PublicOffice',
        'RelatedProject',  # Similar to relatedProcess in OCDS
        'SimpleIdentifier',
        'Social',
        'Sustainability',
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
        'Milestone',
        'MilestoneReference',
        'Person',
        'Finance',
    }
    _compare(
        schema['definitions'],
        infra_definitions, ocds_definitions, 'schema/project-level/project-schema.json#/definitions', 'definitions'
    )

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

        if basename in ('documentType.csv', 'locationGazetteers.csv', 'partyRole.csv'):
            with open(path) as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames
                oc4ids_rows = []
                oc4ids_codes = []
                for row in reader:
                    if row.get('Source', row.get('Extension')) == 'OC4IDS':
                        oc4ids_rows.append(row)
                        oc4ids_codes.append(row['Code'])

        with open(path, 'w') as f:
            if basename == 'documentType.csv':
                text = _merge_codes(['OCDS for PPPs', 'OCDS'], fieldnames, basename, ignore, oc4ids_codes, oc4ids_rows)
            elif basename == 'locationGazetteers.csv':
                text = _merge_codes(['OCDS for PPPs'], fieldnames, basename, [], oc4ids_codes, oc4ids_rows)
            elif basename == 'partyRole.csv':
                text = _merge_codes(['OCDS'], fieldnames, basename, [], oc4ids_codes, oc4ids_rows)
            else:
                text = get(f'{ppp_base_url}codelists/{basename}').text

            f.write(text)

    # Copy properties

    _copy_element('language', {
        ('title',): lambda s: s.replace('Release language', 'Language'),
    }, root='properties')

    # Copy definitions. The following definitions follow the same order as in project-schema.json.

    _copy_element('Period', {
        # Refer to project.
        ('description',): lambda s: s.replace('contracting process', 'project or contracting process'),
    })

    _copy_element('Classification', {
        # Replace line item classification scheme codelist with classification scheme codelist
        ('properties', 'scheme', 'description'): lambda s: s.replace(
            '. For line item classifications, this uses the open [itemClassificationScheme](https://standard.open-contracting.org/1.1/en/schema/codelists/#item-classification-scheme) codelist.',  # noqa: E501
            ', using the open [classificationScheme](https://standard.open-contracting.org/infrastructure/{{version}}/{{lang}}/reference/codelists/#classificationscheme) codelist.'  # noqa: E501
        ),
    })
    # Replace line item classification scheme codelist with classification scheme codelist
    schema['definitions']['Classification']['properties']['scheme']['codelist'] = 'classificationScheme.csv'

    _copy_element('Location')
    # Original from extension:     "The location where activity related to this tender, contract or license will be delivered, or will take place. A location can be described by either a geometry (point location, line or polygon), or a gazetteer entry, or both." # noqa: E501
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
    schema['definitions']['Location']['properties'] = OrderedDict(schema['definitions']['Location']['properties'])
    schema['definitions']['Location']['properties'].move_to_end('id', last=False)
    schema['definitions']['Location']['required'] = ['id']

    # Set stricter validation on gazetteer identifiers.
    schema['definitions']['Location']['properties']['gazetteer']['properties']['identifiers']['uniqueItems'] = True

    _copy_element('Value')

    _copy_element('Organization', {
        # Refer to project instead of contracting process, link to infrastructure codelist instead of PPP codelist.
        ('properties', 'roles', 'description'): lambda s: (
            s.replace('contracting process', 'project').replace(
                'profiles/ppp/latest/en/',
                'infrastructure/{{version}}/{{lang}}/'
            )
        ),
    })
    # Remove unneeded fields from Organization.
    del schema['definitions']['Organization']['properties']['shareholders']
    # Remove OCDS-specific merging properties.
    del schema['definitions']['Organization']['properties']['additionalIdentifiers']['wholeListMerge']
    del schema['definitions']['Organization']['properties']['details']['properties']['classifications']['wholeListMerge']  # noqa: E501
    # Remove details wrapper from Organization.
    schema['definitions']['Organization']['properties']['classifications'] = schema['definitions']['Organization']['properties']['details']['properties']['classifications']  # noqa: E501
    del schema['definitions']['Organization']['properties']['details']
    # Set stricter validation on party roles.
    schema['definitions']['Organization']['properties']['roles']['uniqueItems'] = True
    # Add people field to Organization.
    schema['definitions']['Organization']['properties']['people'] = {
        "title": "People",
        "description": "People associated with, representing, or working on behalf of this organization in respect of this project.",  # noqa: E501
        "type": "array",
        "items": {
            "$ref": "#/definitions/Person"
        },
        "uniqueItems": True
    }

    _copy_element('OrganizationReference')

    _copy_element('Address')

    _copy_element('ContactPoint', {
        # Refer to project instead of contracting process.
        ('properties', 'name', 'description'): lambda s: s.replace('contracting process', 'project'),
    })

    _copy_element('BudgetBreakdown', {
        # Refer to project instead of contracting process.
        ('properties', 'amount', 'description'): lambda s: s.replace('contracting process', 'project',)
    })
    # Add approval date.
    schema['definitions']['BudgetBreakdown']['properties']['approvalDate'] = deepcopy(schema['properties']['budget']['properties']['approvalDate'])  # noqa: E501
    schema['definitions']['BudgetBreakdown']['properties']['approvalDate']['description'] = "The date on which this budget entry was approved. Where documentary evidence for this exists, it may be included among the project documents with `.documentType` set to 'budgetApproval'."  # noqa: E501

    _copy_element('Document', {
        # Link to infrastructure codelist instead of PPP codelist.
        ('properties', 'documentType', 'description'): lambda s: (
            s.replace('profiles/ppp/latest/en/', 'infrastructure/{{version}}/{{lang}}/')
        ),
    })
    del schema['definitions']['Document']['properties']['accessDetailsURL']
    del schema['definitions']['Document']['properties']['unofficialTranslations']
    # Original from standard: "A short description of the document. We recommend descriptions do not exceed 250 words. In the event the document is not accessible online, the description field can be used to describe arrangements for obtaining a copy of the document.", # noqa: E501
    schema['definitions']['Document']['properties']['description']['description'] = "Where a link to a full document is provided, the description should provide a 1 - 3 paragraph summary of the information the document contains, and the `pageStart` field should be used to make sure readers can find the correct section of the document containing more information. Where there is no linked document available, the description field may contain all the information required by the current `documentType`. \n\nLine breaks in text (represented in JSON using `\\n\\n`) must be respected by systems displaying this information, and systems may also support basic HTML tags (H1-H6, B, I, U, strong, A and optionally IMG) or [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for formatting. "  # noqa: E501
    # Original from standard: " direct link to the document or attachment. The server providing access to this document should be configured to correctly report the document mime type." # noqa: E501
    schema['definitions']['Document']['properties']['url']['description'] = "This should be a direct link to the document or web page where the information described by the current documentType exists."  # noqa: E501

    _copy_element('Identifier')

    _copy_element('Metric', {
        ('properties', 'id', 'description'): lambda s: (
            s.replace('contracting process', 'contracting process or project')
        ),
    })

    # Original from standard: "Metrics are used to set out targets and results from a contracting process. During the planning and tender sections, a metric indicates the anticipated results. In award and contract sections it indicates the awarded/contracted results. In the implementation section it is used to provide updates on actually delivered results, also known as outputs." # noqa: E501
    schema['definitions']['Metric']['description'] = "Metrics are used to set out forecast and actual metrics targets for a project: for example, planned and actual physical and financial progress over time."  # noqa: E501

    _copy_element('Observation')
    # Remove the relatedImplementationMilestone field.
    del schema['definitions']['Observation']['properties']['relatedImplementationMilestone']

    _copy_element('Transaction')
    # Original from standard: "A spending transaction related to the contracting process. Draws upon the data models of the [Fiscal Data Package](https://frictionlessdata.io/specs/fiscal-data-package/) and the [International Aid Transparency Initiative](http://iatistandard.org/activity-standard/iati-activities/iati-activity/transaction/) and should be used to cross-reference to more detailed information held using a Fiscal Data Package, IATI file, or to provide enough information to allow a user to manually or automatically cross-reference with some other published source of transactional spending data." # noqa: E501
    schema['definitions']['Transaction']['description'] = "A financial transaction related to a project or contracting process. Draws upon the data models of the Fiscal Data Package and the International Aid Transparency Initiative and should be used to cross-reference to more detailed information held using a Fiscal Data Package, IATI file, or to provide enough information to allow a user to manually or automatically cross-reference with some other published source of transactional data."  # noqa: E501

    _copy_element('Milestone')
    # Original from standard: "The milestone block can be used to represent a wide variety of events in the lifetime of a contracting process." # noqa: E501
    schema['definitions']['Milestone']['description'] = "An event in the lifetime of a project or contracting process."
    # Original from standard: "A local identifier for this milestone, unique within this block. This field is used to keep track of multiple revisions of a milestone through the compilation from release to record mechanism." # noqa: E501
    schema['definitions']['Milestone']['properties']['id']['description'] = "A local identifier for this milestone, unique within this block."  # noqa: E501
    # Original from standard: "Milestone codes can be used to track specific events that take place for a particular kind of contracting process. For example, a code of 'approvalLetter' can be used to allow applications to understand this milestone represents the date an approvalLetter is due or signed." # noqa: E501
    schema['definitions']['Milestone']['properties']['code']['description'] = "Milestone codes can be used to track specific events that take place for a particular kind of project or contracting process. For example, a code of 'approvalLetter' can be used to allow applications to understand this milestone represents the date an approvalLetter is due or signed."  # noqa: E501
    # Add Milestone.value from OCDS 1.2.
    schema['definitions']['Milestone']['properties']['value'] = {
          "title": "Value",
          "description": "The payment's value, if the milestone represents a planned payment.",
          "$ref": "#/definitions/Value"
        }
    # Remove deprecated Milestone.documents field.
    del schema['definitions']['Milestone']['properties']['documents']

    _copy_element('MilestoneReference', {
        # Remove reference to release, add reference to project.
        ('properties', 'id', 'description'): lambda s: (
            s.replace(
                ' described elsewhere in a release about this contracting process.',
                " in this project or contracting process's `.milestones`."
            )
        ),
    })
    # Original from standard: "The title of the milestone being referenced, this must match the title of a milestone described elsewhere in a release about this contracting process." # noqa: E501
    schema['definitions']['MilestoneReference']['properties']['title']['description'] = "The title of the milestone being referenced, this must match the title of a milestone in this project or contracting process's `.milestones`."  # noqa: E501

    _copy_element('Person')
    schema['definitions']['Person']['properties']['jobTitle'] = {
          "title": "Job title",
          "description": "The job title of the person (for example, Financial Manager).",
          "type": "string",
          "minLength": 1
        }

    _remove_null_and_pattern_properties(schema)
    _remove_integer_identifier_types(schema)
    _remove_deprecated_properties(schema)
    add_validation_properties(schema)

    with (schema_dir / 'project-schema.json').open('w') as f:
        json.dump(schema, f, ensure_ascii=False, indent=2)
        f.write('\n')


@cli.command()
@click.argument("filename", type=click.Path(exists=True, dir_okay=False))
@click.option("-a", "--additional-properties", is_flag=True, help="Allow additional properties")
@click.option("-l", "--link-fields", is_flag=True, help="Link field names to jsonschema directives")
def lint(filename, additional_properties, link_fields):

    # From standard-maintenance-scripts/tests/test_readme.py
    def _set_additional_properties(data, additional_properties):
        if isinstance(data, list):
            for item in data:
                _set_additional_properties(item, additional_properties)
        elif isinstance(data, dict):
            if "properties" in data:
                data["additionalProperties"] = additional_properties
            for value in data.values():
                _set_additional_properties(value, additional_properties)

    def _get_fields(schema, parents=()):
        """
        Generate field names (as tuples) in the JSON Schema.
        """
        for name, value in schema.get('properties', {}).items():
            path = (*parents, name)
            if 'properties' in value:
                yield from _get_fields(value, path)
            else:
                yield path

    def _link(name, fields, text):
        """
        Generate a link to a field in a jsonschema directive HTML table. Prompt if the field's name is ambiguous.

        :param name: The property name
        :param fields: A list of fields (as tuples) in the JSON schema
        :param text: The text in which the property name appears
        """
        if name[1:] in {"`true`", "`false`"}:
            return name

        path = tuple(part for part in name[2:-1].split(".") if part != '')
        occurrences = [field for field in fields if field[-len(path):] == path]

        # Track the match index to highlight the current match.
        global matches
        matches[name] += 1
        match_number = matches[name]

        match len(occurrences):
            case 0:
                raise ValueError(f"Field {name} not in schema")
            case 1:
                choice = 0
            # Resolve ambiguous field names, like `title`.
            case _:
                click.secho(f"{name[1:]} is ambiguous in:\n", fg="yellow")

                splits = text.split(name, match_number)
                click.echo(f"{name.join(splits[:match_number])}{click.style(name, fg='red')}{splits[-1]}\n")

                occurrences.sort()
                for i, field in enumerate(occurrences, 1):
                    click.secho(f"    {i}: {'.'.join(field)}", fg="blue")
                prompt = click.style(f"\nChoose the field to link to (1-{len(occurrences)}):", fg="yellow")
                choices = click.Choice([str(i) for i in range(1, len(occurrences) + 1)])
                choice = int(click.prompt(prompt, type=choices, prompt_suffix="", show_choices=False)) - 1

        definition = occurrences[choice][0] if occurrences[choice][0][0].isupper() else None

        url = f"project-schema.json,{f'/definitions/{definition}' if definition else ''},{'/'.join(path)}"
        return f"{name[0]}[`{'.' if name[2] == '.' else ''}{'.'.join(path)}`]({url})"

    minimal_project = {
        "id": "oc4ids-bu3kcz-1",
    }

    unlinked_backticked_field = re.compile(r"[^\[]`[A-Za-z.]+`")

    with open(filename) as f:
        elements = yaml.safe_load(f)

    with (basedir / 'schema' / 'project-level' / 'project-schema.json').open() as f:
        schema = json.load(f)

    _set_additional_properties(schema, additional_properties)

    fields = set(_get_fields(schema))
    for name, definition in schema['definitions'].items():
        fields.update(_get_fields(definition, (name,)))

    validator = Draft4Validator(schema, format_checker=FormatChecker())

    additional_fields = defaultdict(list)
    missing_data = defaultdict(list)
    for element in elements:
        identifier = element["id"]
        title = element["title"]

        # Check for missing data
        for key, value in element.items():
            if value == '' or value is None:
                # Don't report missing examples for cross-referenced mappings
                if key != 'example' and 'See [' not in value:
                    missing_data[key].append(f"{identifier} {title}")

        # Format Markdown.
        for key in ("title", "module", "indicator", "disclosure format", "mapping"):
            value = element.get(key, "")

            if link_fields and key == "mapping":
                global matches
                matches = defaultdict(int)
                value = unlinked_backticked_field.sub(lambda match: _link(match.group(0), fields, value), value)

            element[key] = mdformat.text(value, options={"number": True}).rstrip()

        # Format and validate JSON.
        example = element["example"]
        if example and example != "N/A":
            try:
                data = json.loads(example)

                project = deepcopy(minimal_project)
                json_merge_patch.merge(project, data)

                for e in validator.iter_errors(project):
                    if e.validator == "additionalProperties":
                        e.absolute_schema_path[-1] = "properties"
                        e.absolute_schema_path.append("")
                        for match in re.findall(r"'(\S+)'", e.message):
                            e.absolute_schema_path[-1] = match
                            additional_fields[
                                "/".join(e.absolute_schema_path)
                                .replace("items/properties/", "")
                                .replace("properties/", "")
                            ].append([identifier, title])
                    else:
                        click.echo(f"{identifier} ({title}): OC4IDS is invalid: "
                                   f"{e.message} ({'/'.join(e.absolute_schema_path)})")
            except json.decoder.JSONDecodeError as e:
                click.echo(f"{identifier} ({title}): JSON is invalid: {e}: {example}")

    if additional_fields:
        click.echo(f"\nAdditional fields ({len(additional_fields)}):")
        click.echo("   field,id,title")
        for field, occurrences in sorted(additional_fields.items(), key=lambda item: item[1]):
            click.echo(f"   {field}{''.join(f',{identifier},{title}' for identifier, title in occurrences)}")

    if missing_data:
        for key, occurrences in missing_data.items():
            click.echo(f"\nMissing {key}:")
            for occurrence in occurrences:
                click.echo(f"   {occurrence}")

    write_yaml_file(filename, elements)


@cli.command()
def update_sustainability_elements():
    """
    Update mapping/sustainability.yaml from CoST IDS sustainability elements spreadsheet
    """

    filename = basedir / 'mapping' / 'sustainability.yaml'

    # CoST IDS sustainability elements are maintained in https://docs.google.com/spreadsheets/d/165epI69oQ5YyL4-2q8VubFn9VuNham2Pi1u0P49id9o # noqa: E501
    source = csv_reader(
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vTHlHTshFw7PMbPsNz5ecYZsIy7aEHl0pN4sENGgesTT7kR8eZ0GjJjPVf54iMA6eK3ZpQZ2k5e6rQn/pub?gid=0&single=true&output=csv") # noqa
    source = {element["id"]: element for element in source}

    # Load sustainability modules mapping
    with open(filename) as f:
        mapping = yaml.safe_load(f)

    mapping = {element["id"]: element for element in mapping}

    new_elements = []
    deleted_elements = []

    # Update common elements
    for identifier, properties in source.items():
        element = mapping.get(identifier)

        if element:
            for prop in ['title', 'module', 'indicator', 'disclosure format']:
                element[prop] = properties[prop]
        else:
            new_elements.append(identifier)

    # Add new elements
    for identifier in new_elements:
        properties = source[identifier]

        for prop in ['mapping', 'example']:
            properties[prop] = ''

        mapping[identifier] = properties

    # Remove deleted elements
    for identifier in mapping:
        if identifier not in source:
            deleted_elements.append(identifier)

    for identifier in deleted_elements:
        mapping.pop(identifier)

    write_yaml_file(filename, list(mapping.values()))


@cli.command()
def update_sustainability_docs():
    """
    Update docs/cost/ids/sustainability.md from mapping/sustainability.yaml
    """

    # Load sustainability mapping documentation
    with (basedir / 'docs' / 'cost' / 'ids' / 'sustainability.md').open() as f:
        docs = f.readlines()

    # Preserve content that appears before the content generated by this function
    module_index = docs.index("## Economic and fiscal\n")
    docs = docs[:module_index]

    # Generate mapping documentation for each module
    modules = {}
    with (basedir / 'mapping' / 'sustainability.yaml').open() as f:
        elements = yaml.safe_load(f)

    for element in elements:
        module = element.get("module")
        if module not in modules:
            modules[module] = []

        title = element.get("title", "")
        target = nodes.make_id(f"{module}-{title}")
        modules[module].extend(
            [
              f"\n({target})=",
              "\n\n`````{grid} 2",
              f"\n\n````{{grid-item-card}} {title}",
              "\n:columns: 4",
              "\nCoST IDS element",
              "\n^^^\n",
              element.get("disclosure format", ""),
              "\n````",
              "\n\n````{grid-item-card}",
              "\n:columns: 8",
              "\nOC4IDS mapping",
              "\n^^^\n",
              element.get("mapping", ""),
              f"\n```json\n{element['example']}\n```" if element.get('example') else '',
              "\n````",
              "\n\n`````\n\n"
            ]
        )

    for name, content in modules.items():
        docs.append(f"## {name}\n\n"),
        docs.extend(content)

    with (basedir / 'docs' / 'cost' / 'ids' / 'sustainability.md').open('w') as f:
        f.writelines(docs)


if __name__ == '__main__':
    cli()
