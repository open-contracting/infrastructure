# Schema reference

The Open Contracting for Infrastructure Data Standard (OC4IDS) provides a common approach for the disclosure of structured data on infrastructure projects and their related contracting processes.

OC4IDS is comprised of a schema file and codelist files, and reference documentation is available for the [schema](reference.md) and [codelists](codelists.md).

The schema can be explored using the [schema browser](schema.md) and can be [downloaded here](../../../../project-schema.json). The schema is expressed using [JSON Schema, draft 4](https://tools.ietf.org/html/draft-zyp-json-schema-04).

OC4IDS data must be published as part of a [project package](package.md), which serves as a container for data on multiple projects and adds important metadata about the data publication.

The OC4IDS schema reuses many of the building blocks from the Open Contracting Data Standard; these are introduced in the [Getting Started section of the OCDS documentation](http://standard.open-contracting.org/latest/en/getting_started/).

```eval_rst
.. toctree::
   :maxdepth: 1
   :glob:

   schema
   reference
   package

```

## Data validation

OC4IDS uses a permissive schema. It does not enforce strong technical validation requirements on data, other than some structural rules and data type rules (dates, numbers and strings).

The fact that data validates against the schema cannot be used to make any judgement about the quality of that data.

## Extending the schema

The schema does not restrict the use of additional objects or fields. As a result, publishers of data are free to add extra details to their data.

No formal extensions mechanism currently exists for OC4IDS. However, the extensions mechanism from the Open Contracting Data Standard should be used as a reference model if such a mechanism is required in future.
