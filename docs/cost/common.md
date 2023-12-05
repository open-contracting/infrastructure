# Common operations

To avoid repetition in the mapping, we refer and link to the following common operations.

## Add a project document

Add a `Document` object to the `documents` array and set its:

* `.id` incrementally
* `.url` to a direct link to the document
* `.title` to the title of the document
* `.pageStart` and `.pageEnd` to the page range containing the information described in its `.documentType`

## Add a contracting process document

Add a `Document` object to the `contractingProcesses.summary.documents` array and set its:

* `.id` incrementally
* `.url` to a direct link to the document
* `.title` to the title of the document
* `.pageStart` and `.pageEnd` to the page range containing the information described in its `.documentType`

## Add an organization

1. Add an `Organization` object to the `parties` array and set its `.name` to the name of the organization.
1. If you collect organization identifiers, set `.identifier` according to the [identifier reference](../reference/schema.md#identifier) and set `.id` to {identifier.scheme}-{identifier.id}(-{department-identifier}). Otherwise, set `.id` incrementally.

## Add a financing arrangement

1. If the project is a public-private partnership (PPP), get the `ContractingProcess` in `.contractingProcesses` that represents the contracting process for the PPP contract and add a `Finance` object to its `.summary.finance` array. Otherwise, add a `Finance` object to the `.budget.finance` array.
2. Set the `Finance` object's `.id` incrementally.
