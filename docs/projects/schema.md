# Schema browser

The Infrastructure Project-Level Data Specification is described using JSON Schema 0.4. The [schema file is available here](../../_static/project-level/project-schema.json) and can be explored using the browser below.

Full schema and codelist [reference documentation is also available](reference.md). 

<script src="../../_static/docson/widget.js" data-schema="../../_static/project-level/project-schema.json"></script>

## Data validation

The Project-Level Data Specification uses a permissive schema. It does not enforce strong technical validation requirements on data, other than some structural rules and data type rules (dates, numbers and strings). 

The fact that data validates against the schema cannot be used to make any judgement about the quality of that data. 

## Extending the schema

The schema does not restrict the use of additional objects or fields. As a result, publishers of data are free to add extra details to their data.

No formal extensions mechanism currently exists for the Project-Level Data Specification. However, the extensions mechanism from the Open Contracting Data Standard should be used as a reference model if such a mechanism is required in future. 