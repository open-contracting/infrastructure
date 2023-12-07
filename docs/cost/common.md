# Common operations

To avoid repetition in the mapping, we refer and link to the following common operations.

## Add a project document

Add a [`Document`](../reference/schema.md#document) object to the [`documents`](project-schema.json,,documents) array and set its:

* [`.id`](project-schema.json,/definitions/Document,id) incrementally
* [`.url`](project-schema.json,/definitions/Document,url) to a direct link to the document
* [`.title`](project-schema.json,/definitions/Document,title) to the title of the document
* [`.pageStart`](project-schema.json,/definitions/Document,pageStart) and [`.pageEnd`](project-schema.json,/definitions/Document,pageEnd) to the page range containing the information described in its [`.documentType`](project-schema.json,/definitions/Document,documentType)

## Add a contracting process document

Add a [`Document`](../reference/schema.md#document) object to the [`contractingProcesses.summary.documents`](project-schema.json,/definitions/ContractingProcessSummary,documents) array and set its:

* [`.id`](project-schema.json,/definitions/Document,id) incrementally
* [`.url`](project-schema.json,/definitions/Document,url) to a direct link to the document
* [`.title`](project-schema.json,/definitions/Document,title) to the title of the document
* [`.pageStart`](project-schema.json,/definitions/Document,pageStart) and [`.pageEnd`](project-schema.json,/definitions/Document,pageEnd) to the page range containing the information described in its [`.documentType`](project-schema.json,/definitions/Document,documentType)

## Add an organization

1. Add an [`Organization`](../reference/schema.md#organization) object to the [`parties`](project-schema.json,,parties) array and set its [`.name`](project-schema.json,/definitions/Organization,name) to the name of the organization.
1. If you collect organization identifiers, set [`.identifier`](project-schema.json,/definitions/Organization,identifier) according to the [identifier reference](../reference/schema.md#identifier) and set [`.id`](project-schema.json,/definitions/Organization,id) to `{identifier.scheme}-{identifier.id}(-{department-identifier})`. Otherwise, set [`.id`](project-schema.json,/definitions/Organization,id) incrementally.

## Add a financing arrangement

1. If the project is a public-private partnership (PPP), get the [`ContractingProcess`](../reference/schema.md#contractingprocess) in [`.contractingProcesses`](project-schema.json,,contractingProcesses) that represents the contracting process for the PPP contract and add a [`Finance`](../reference/schema.md#finance) object to its [`.summary.finance`](project-schema.json,/definitions/ContractingProcessSummary,finance) array. Otherwise, add a [`Finance`](../reference/schema.md#finance) object to the [`.budget.finance`](project-schema.json,,budget/finance) array.
2. Set the [`Finance`](../reference/schema.md#finance) object's [`.id`](project-schema.json,/definitions/Finance,id) incrementally.
