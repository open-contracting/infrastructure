# Examples

This page provides examples to help you understand and implement OC4IDS. There are two examples:

## Worked example

The worked example is a JSON file that conforms to the [project package schema](../../reference/package). It contains a single project that conforms to the [project schema](../../reference/schema). You can view the complete worked example below or [download the JSON file](../examples/example.json). You can also view excerpts from the worked example alongside each sub-schema in the [schema reference documentation](../../reference/schema).

The worked example describes a fictional infrastructure project to upgrade a motorway in the UK with three related contracting processes. An example value is provided for each field in the schema, including:

* [`forecasts`](../../reference/schema/) and [`metrics`](../../reference/schema) that describe planned and actual physical progress
* [`modifications`](../../reference/schema/) that describe changes to the duration, scope and value of contracting processes
* [`completion`](../../reference/schema/) data, describing the final end date, value and scope of the project.

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer:
:title: Worked example
```

## Blank example

The blank example is a JSON file that conforms to the structure of the [project schema](../../reference/schema). You can view the blank example below or [download the JSON file](../examples/blank.json). Field values are replaced with either:

* Empty strings (`""`) or empty arrays (`[]`)
* The type of the field, e.g. "string" or "array"
* The name of the codelist referenced by the field, e.g. "string from currency codelist"

```{jsoninclude} ../../docs/examples/blank.json
:jsonpointer:
:title: Blank example
```
