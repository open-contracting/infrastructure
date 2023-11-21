# Schema reference

<style>
.wy-nav-content {
  max-width: 1200px;
}
</style>

This page presents the fields in the OC4IDS schema in tables with additional information in paragraphs. Required fields are indicated in the **Required** column.

For fields that reference a sub-schema, a link is provided to a table with details of the sub-schema. To see how the fields and sub-schemas fit together, consult the [schema browser](browser).

**Examples** are provided for each table, showing how to represent the fields in the table in JSON format. For more information on the examples, see [examples](../guidance/example).

## Project

The top-level object in OC4IDS is a project.

A project is defined as:

> The development of a set of infrastructure assets in a specified location, generally the responsibility of a single procuring entity and budget authority: for example, a highway overpass or a university campus.

A project's fields include:

 * Metadata, such as the project's `title`, `description` and `status`.
 * Budget data, which describes the projected costs or allocated budget for the project.
 * Data about the parties (organizations and other participants) involved in the project.
 * Links to documents relating to the project, such as needs assessments and project evaluations.
 * Data about contracting processes for different aspects of the project, such as design, construction and supervision.
 * Completion data, such as the final scope, duration and costs for the project.
 
Each project has the following fields.

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:include:
:collapse: identifiers,period,additionalClassifications,relatedProjects,assetLifetime,locations,budget/amount,budget/budgetBreakdown,forecasts,parties,publicAuthority,documents,contractingProcesses,metrics,completion/finalValue
:addtargets:
```
````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0
:title: Project
```

````

`````

## Sub-schemas

This section lists each sub-schema in the OC4IDS schema. Sub-schemas are parts of the schema that are represented as objects in OC4IDS data. Some sub-schemas are referenced from multiple places in the schema.

### ContractingProcess

`ContractingProcess` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/ContractingProcess
```

This sub-schema is referenced by the following properties:
* [`contractingProcesses`](project-schema.json,,contractingProcesses)

Each `ContractingProcess` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/ContractingProcess
:collapse: id,summary,releases
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses
:title: contractingProcesses
```

````

`````

### ContractingProcessSummary

`ContractingProcessSummary` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/ContractingProcessSummary
```

This sub-schema is referenced by the following properties:
* [`ContractingProcess/summary`](project-schema.json,/definitions/ContractingProcess,summary)

Each `ContractingProcessSummary` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/ContractingProcessSummary
:collapse: ocid,externalReference,nature,title,description,status,suppliers,contractValue,contractPeriod,finalValue,documents,modifications,transactions,milestones
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary
:title: contractingProcesses/0/summary
```

````

`````

### LinkedRelease

`LinkedRelease` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/LinkedRelease
```

This sub-schema is referenced by the following properties:
* [`ContractingProcess/releases`](project-schema.json,/definitions/ContractingProcess,releases)

Each `LinkedRelease` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/LinkedRelease
:collapse: id,tag,date,url
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/releases
:title: contractingProcesses/0/releases
```

````

`````

### Modification

`Modification` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Modification
```

This sub-schema is referenced by the following properties:
* [`ContractingProcessSummary/modifications`](project-schema.json,/definitions/ContractingProcessSummary,modifications)

Each `Modification` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Modification
:collapse: id,date,description,rationale,type,releaseID,oldContractValue,newContractValue,oldContractPeriod,newContractPeriod
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/modifications
:title: contractingProcesses/0/summary/modifications
```

````

`````

### Period

Dates MUST be expressed using a full ISO 8601 date-time including a timezone. E.g.:

> 2018-09-18T11:26:04+01:00

Where the source system does not contain time information, a judgment ought to be made as to the relevant time to attach (e.g. start of the day; end of the working day etc.).

`Period` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Period
```

This sub-schema is referenced by the following properties:
* [`period`](project-schema.json,,period)
* [`assetLifetime`](project-schema.json,,assetLifetime)
* [`ContractingProcessSummary/contractPeriod`](project-schema.json,/definitions/ContractingProcessSummary,contractPeriod)
* [`Modification/oldContractPeriod`](project-schema.json,/definitions/Modification,oldContractPeriod)
* [`Modification/newContractPeriod`](project-schema.json,/definitions/Modification,newContractPeriod)
* [`BudgetBreakdown/period`](project-schema.json,/definitions/BudgetBreakdown,period)
* [`Observation/period`](project-schema.json,/definitions/Observation,period)

Each `Period` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Period
:collapse: startDate,endDate,maxExtentDate,durationInDays
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/period
:title: period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/assetLifetime
:title: assetLifetime
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/budgetBreakdown/0/period
:title: budget/budgetBreakdown/0/period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/forecasts/0/observations/0/period
:title: forecasts/0/observations/0/period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/contractPeriod
:title: contractingProcesses/0/summary/contractPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/modifications/0/oldContractPeriod
:title: contractingProcesses/0/summary/modifications/0/oldContractPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/modifications/0/newContractPeriod
:title: contractingProcesses/0/summary/modifications/0/newContractPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/metrics/0/observations/0/period
:title: metrics/0/observations/0/period
```

````

`````

### Classification

`Classification` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Classification
```

This sub-schema is referenced by the following properties:
* [`additionalClassifications`](project-schema.json,,additionalClassifications)

Each `Classification` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Classification
:collapse: scheme,id,description,uri
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/additionalClassifications
:title: additionalClassifications
```

````

`````

### Location

`Location` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Location
```

This sub-schema is referenced by the following properties:
* [`locations`](project-schema.json,,locations)

Each `Location` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Location
:collapse: id,description,uri,address
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/locations
:title: locations
```

````

`````

### Value

`Value` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Value
```

This sub-schema is referenced by the following properties:
* [`budget/amount`](project-schema.json,,budget/amount)
* [`completion/finalValue`](project-schema.json,,completion/finalValue)
* [`ContractingProcessSummary/tender/costEstimate`](project-schema.json,/definitions/ContractingProcessSummary,tender/costEstimate)
* [`ContractingProcessSummary/contractValue`](project-schema.json,/definitions/ContractingProcessSummary,contractValue)
* [`ContractingProcessSummary/finalValue`](project-schema.json,/definitions/ContractingProcessSummary,finalValue)
* [`Modification/oldContractValue`](project-schema.json,/definitions/Modification,oldContractValue)
* [`Modification/newContractValue`](project-schema.json,/definitions/Modification,newContractValue)
* [`BudgetBreakdown/amount`](project-schema.json,/definitions/BudgetBreakdown,amount)
* [`Observation/value`](project-schema.json,/definitions/Observation,value)
* [`Transaction/value`](project-schema.json,/definitions/Transaction,value)

Each `Value` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Value
:collapse: amount,currency
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/amount
:title: budget/amount
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/budgetBreakdown/0/amount
:title: budget/budgetBreakdown/0/amount
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/tender/costEstimate
:title: contractingProcesses/0/summary/tender/costEstimate
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/contractValue
:title: contractingProcesses/0/summary/contractValue
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/finalValue
:title: contractingProcesses/0/summary/finalValue
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/modifications/2/oldContractValue
:title: contractingProcesses/0/summary/modifications/0/oldContractValue
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/modifications/2/newContractValue
:title: contractingProcesses/0/summary/modifications/0/newContractValue
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions/0/value
:title: contractingProcesses/0/summary/transactions/0/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/value
:title: transactions/0/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/completion/finalValue
:title: completion/finalValue
```

````

`````

### Organization

`Organization` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Organization
```

This sub-schema is referenced by the following properties:
* [`parties`](project-schema.json,,parties)

Each `Organization` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Organization
:collapse: name,id,identifier,additionalIdentifiers,address,contactPoint,roles,beneficialOwners,people
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties
:title: parties
```

````

`````

### OrganizationReference

`OrganizationReference` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/OrganizationReference
```

This sub-schema is referenced by the following properties:
* [`publicAuthority`](project-schema.json,,publicAuthority)
* [`ContractingProcessSummary/tender/tenderers`](project-schema.json,/definitions/ContractingProcessSummary,tender/tenderers)
* [`ContractingProcessSummary/tender/procuringEntity`](project-schema.json,/definitions/ContractingProcessSummary,tender/procuringEntity)
* [`ContractingProcessSummary/tender/administrativeEntity`](project-schema.json,/definitions/ContractingProcessSummary,tender/administrativeEntity)
* [`ContractingProcessSummary/suppliers`](project-schema.json,/definitions/ContractingProcessSummary,suppliers)
* [`BudgetBreakdown/sourceParty`](project-schema.json,/definitions/BudgetBreakdown,sourceParty)
* [`Transaction/payer`](project-schema.json,/definitions/Transaction,payer)
* [`Transaction/payee`](project-schema.json,/definitions/Transaction,payee)

Each `OrganizationReference` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/OrganizationReference
:collapse: name,id
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/budgetBreakdown/0/sourceParty
:title: budget/budgetBreakdown/0/sourceParty
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/publicAuthority
:title: publicAuthority
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/tender/tenderers
:title: contractingProcesses/0/summary/tender/tenderers
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/tender/procuringEntity
:title: contractingProcesses/0/summary/tender/procuringEntity
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/tender/administrativeEntity
:title: contractingProcesses/0/summary/tender/administrativeEntity
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/suppliers
:title: contractingProcesses/0/summary/suppliers
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions/0/payer
:title: contractingProcesses/0/summary/transactions/0/payer
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions/0/payee
:title: contractingProcesses/0/summary/transactions/0/payee
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/payer
:title: transactions/0/payer
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/payee
:title: transactions/0/payee
```

````

`````

### Address

The address sub-schema re-uses fields from schema.org and vCard. In the event source data cannot be broken down into these parts, data should contain at least a `streetAddress` and `postalCode`.

When working with data, users ought to be aware that addresses might not always be broken down using all the fields the schema provides.

`Address` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Address
```

This sub-schema is referenced by the following properties:
* [`Location/address`](project-schema.json,/definitions/Location,address)
* [`Organization/address`](project-schema.json,/definitions/Organization,address)
* [`Person/address`](project-schema.json,/definitions/Person,address)

Each `Address` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Address
:collapse: streetAddress,locality,region,postalCode,countryName
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/locations/0/address
:title: locations/0/address
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties/0/address
:title: parties/0/address
```

````

`````

### ContactPoint

`ContactPoint` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/ContactPoint
```

This sub-schema is referenced by the following properties:
* [`Organization/contactPoint`](project-schema.json,/definitions/Organization,contactPoint)

Each `ContactPoint` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/ContactPoint
:collapse: name,email,telephone,faxNumber,url
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties/0/contactPoint
:title: parties/0/contactPoint
```

````

`````

### BudgetBreakdown

For more information about this sub-schema, see the [OCDS Budget Breakdown extension documentation](https://extensions.open-contracting.org/en/extensions/budget/master/). `BudgetBreakdown` can also be extended further to include budget classifications data following the pattern described in the [OCDS Budgets and Spend extension](https://extensions.open-contracting.org/en/extensions/budget_and_spend/master/).

`BudgetBreakdown` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/BudgetBreakdown
```

This sub-schema is referenced by the following properties:
* [`budget/budgetBreakdown`](project-schema.json,,budget/budgetBreakdown)

Each `BudgetBreakdown` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/BudgetBreakdown
:collapse: id,description,amount,uri,period,sourceParty,approvalDate
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/budgetBreakdown
:title: budget/budgetBreakdown
```

````

`````

### Document

`Document` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Document
```

This sub-schema is referenced by the following properties:
* [`documents`](project-schema.json,,documents)
* [`ContractingProcessSummary/documents`](project-schema.json,/definitions/ContractingProcessSummary,documents)

Each `Document` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Document
:collapse: id,documentType,title,description,url,datePublished,dateModified,format,language,pageStart,pageEnd,accessDetails,author
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/documents
:title: documents
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/documents
:title: contractingProcesses/0/summary/documents
```

````

`````

### Identifier

Use of stable official organization identifiers can help join up data between systems.

Organization identifiers should be constructed by collecting an official company (or government body) registration number for the organization, and then finding the [org-id.guide list code](https://org-id.guide) for the list this identifier is taken from to use in the `scheme` field.

For example, if identifying a company in Colombia, look up its identifier in the [Unified Commercial and Social Registry](https://org-id.guide/list/CO-RUE) and use the list code `CO-RUE`.

`Identifier` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Identifier
```

This sub-schema is referenced by the following properties:
* [`Organization/identifier`](project-schema.json,/definitions/Organization,identifier)
* [`Organization/additionalIdentifiers`](project-schema.json,/definitions/Organization,additionalIdentifiers)
* [`Person/identifier`](project-schema.json,/definitions/Person,identifier)

Each `Identifier` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Identifier
:collapse: scheme,id,legalName,uri
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties/0/identifier
:title: parties/0/identifier
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties/0/additionalIdentifiers
:title: parties/0/additionalIdentifiers
```

````

`````

### RelatedProject

`RelatedProject` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/RelatedProject
```

This sub-schema is referenced by the following properties:
* [`relatedProjects`](project-schema.json,,relatedProjects)

Each `RelatedProject` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/RelatedProject
:collapse: id,scheme,identifier,relationship,title,uri
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/relatedProjects
:title: relatedProjects
```

````

`````

### Metric

`Metric` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Metric
```

This sub-schema is referenced by the following properties:
* [`forecasts`](project-schema.json,,forecasts)
* [`metrics`](project-schema.json,,metrics)

Each `Metric` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Metric
:collapse: id,title,description,observations
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/forecasts
:title: forecasts
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/metrics
:title: metrics
```

````

`````

### Observation

`Observation` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Observation
```

This sub-schema is referenced by the following properties:
* [`Metric/observations`](project-schema.json,/definitions/Metric,observations)

Each `Observation` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Observation
:collapse: id,period,value,measure,notes
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/forecasts/0/observations
:title: forecasts/0/observations
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/metrics/0/observations
:title: metrics/0/observations
```

````

`````

### Person

Use this object when you need to disclose the details of people associated with, representing or working on behalf of an organization involved in the project.

`Person` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Person
```

This sub-schema is referenced by the following properties:
* [`Organization/beneficialOwners`](project-schema.json,/definitions/Organization,beneficialOwners)
* [`Organization/people`](project-schema.json,/definitions/Organization,people)

Each `Person` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Person
:collapse: id,name,identifier,nationalities,address,email,faxNumber,telephone,jobTitle
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties/0/people
:title: parties/0/people
```

````

`````

### Transaction

A spending transaction related to a contracting process.

`Transaction` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Transaction
```

This sub-schema is referenced by the following properties:
* [`transactions`](project-schema.json,,transactions)
* [`ContractingProcessSummary/transactions`](project-schema.json,/definitions/ContractingProcessSummary,transactions)

Each `Transaction` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Transaction
:collapse: id,source,date,value,payer,payee,uri,relatedImplementationMilestone
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions
:title: contractingProcesses/0/summary/transactions
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions
:title: transactions
```

````

`````

### SimpleIdentifier

`SimpleIdentifier` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/SimpleIdentifier
```

This sub-schema is referenced by the following properties:
* [`identifiers`](project-schema.json,,identifiers)

Each `SimpleIdentifier` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/SimpleIdentifier
:collapse: id,scheme
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/identifiers
:title: identifiers
```

````

`````

### Milestone

`Milestone` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Milestone
```

This sub-schema is referenced by the following properties:
* [`milestones`](project-schema.json,,milestones)
* [`ContractingProcessSummary/milestones`](project-schema.json,/definitions/ContractingProcessSummary,milestones)

Each `Milestone` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Milestone
:collapse: id,title,type,description,code,dueDate,dateMet,dateModified,status
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/milestones
:title: contractingProcesses/0/summary/milestones
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/milestones
:title: milestones
```

````

`````

### MilestoneReference

`MilestoneReference` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/MilestoneReference
```

This sub-schema is referenced by the following properties:
* [`Transaction/relatedImplementationMilestone`](project-schema.json,/definitions/Transaction,relatedImplementationMilestone)

Each `MilestoneReference` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/MilestoneReference
:collapse: id,title
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions/0/relatedImplementationMilestone
:title: contractingProcesses/0/summary/transactions/0/relatedImplementationMilestone
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/relatedImplementationMilestone
:title: transactions/0/relatedImplementationMilestone
```

````

`````

### Sustainability

`Sustainability` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Sustainability
```

This sub-schema is referenced by the following properties:

Each `Sustainability` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Sustainability
:collapse: strategies
:addtargets:
```

````

````{tab-item} Examples

````

`````
