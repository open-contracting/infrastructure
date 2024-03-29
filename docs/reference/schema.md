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
:collapse: identifiers,period,identificationPeriod,preparationPeriod,implementationPeriod,completionPeriod,maintenancePeriod,decommissioningPeriod,budget/finance,costMeasurements,milestones,transactions,lobbyingMeetings,social,environment/impactCategories,environment/conservationMeasures,environment/abatementCost,benefits,additionalClassifications,relatedProjects,assetLifetime,locations,budget/amount,budget/budgetBreakdowns,forecasts,parties,publicAuthority,documents,contractingProcesses,metrics,completion/finalValue
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
:collapse: ocid,externalReference,nature,title,description,status,suppliers,contractValue,contractPeriod,finalValue,documents,modifications,transactions,milestones,finance
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
* [`identificationPeriod`](project-schema.json,,identificationPeriod)
* [`preparationPeriod`](project-schema.json,,preparationPeriod)
* [`implementationPeriod`](project-schema.json,,implementationPeriod)
* [`completionPeriod`](project-schema.json,,completionPeriod)
* [`maintenancePeriod`](project-schema.json,,maintenancePeriod)
* [`decommissioningPeriod`](project-schema.json,,decommissioningPeriod)
* [`ContractingProcessSummary/contractPeriod`](project-schema.json,/definitions/ContractingProcessSummary,contractPeriod)
* [`Modification/oldContractPeriod`](project-schema.json,/definitions/Modification,oldContractPeriod)
* [`Modification/newContractPeriod`](project-schema.json,/definitions/Modification,newContractPeriod)
* [`BudgetBreakdown/period`](project-schema.json,/definitions/BudgetBreakdown,period)
* [`Observation/period`](project-schema.json,/definitions/Observation,period)
* [`Finance/period`](project-schema.json,/definitions/Finance,period)
* [`Finance/paymentPeriod`](project-schema.json,/definitions/Finance,paymentPeriod)

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
:jsonpointer: /projects/0/budget/budgetBreakdowns/0/budgetBreakdown/0/period
:title: budget/budgetBreakdowns/0/budgetBreakdown/0/period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/finance/0/period
:title: budget/finance/0/period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/finance/0/paymentPeriod
:title: budget/finance/0/paymentPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/period
:title: period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/assetLifetime
:title: assetLifetime
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/identificationPeriod
:title: identificationPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/preparationPeriod
:title: preparationPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/implementationPeriod
:title: implementationPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/completionPeriod
:title: completionPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/maintenancePeriod
:title: maintenancePeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/decommissioningPeriod
:title: decommissioningPeriod
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/forecasts/0/observations/0/period
:title: forecasts/0/observations/0/period
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/metrics/0/observations/0/period
:title: metrics/0/observations/0/period
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

````

`````

### Classification

`Classification` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Classification
```

This sub-schema is referenced by the following properties:
* [`additionalClassifications`](project-schema.json,,additionalClassifications)
* [`environment/impactCategories`](project-schema.json,,environment/impactCategories)
* [`Organization/classifications`](project-schema.json,/definitions/Organization,classifications)
* [`Cost/classification`](project-schema.json,/definitions/Cost,classification)

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

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/parties/0/classifications
:title: parties/0/classifications
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/costMeasurements/0/costGroups/0/costs/0/classification
:title: costMeasurements/0/costGroups/0/costs/0/classification
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/environment/impactCategories
:title: environment/impactCategories
```

````

`````

### Location

`Location` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Location
```

This sub-schema is referenced by the following properties:
* [`locations`](project-schema.json,,locations)
* [`Beneficiary/location`](project-schema.json,/definitions/Beneficiary,location)

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

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/benefits/0/beneficiaries/0/location
:title: benefits/0/beneficiaries/0/location
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
* [`environment/abatementCost`](project-schema.json,,environment/abatementCost)
* [`ContractingProcessSummary/tender/costEstimate`](project-schema.json,/definitions/ContractingProcessSummary,tender/costEstimate)
* [`ContractingProcessSummary/contractValue`](project-schema.json,/definitions/ContractingProcessSummary,contractValue)
* [`ContractingProcessSummary/finalValue`](project-schema.json,/definitions/ContractingProcessSummary,finalValue)
* [`ContractingProcessSummary/social/laborBudget`](project-schema.json,/definitions/ContractingProcessSummary,social/laborBudget)
* [`Modification/oldContractValue`](project-schema.json,/definitions/Modification,oldContractValue)
* [`Modification/newContractValue`](project-schema.json,/definitions/Modification,newContractValue)
* [`BudgetBreakdown/amount`](project-schema.json,/definitions/BudgetBreakdown,amount)
* [`Observation/value`](project-schema.json,/definitions/Observation,value)
* [`Transaction/value`](project-schema.json,/definitions/Transaction,value)
* [`Milestone/value`](project-schema.json,/definitions/Milestone,value)
* [`Finance/value`](project-schema.json,/definitions/Finance,value)
* [`CostMeasurement/lifeCycleCosting/value`](project-schema.json,/definitions/CostMeasurement,lifeCycleCosting/value)
* [`Cost/value`](project-schema.json,/definitions/Cost,value)
* [`Social/landCompensationBudget`](project-schema.json,/definitions/Social,landCompensationBudget)

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
:jsonpointer: /projects/0/budget/budgetBreakdowns/0/budgetBreakdown/0/amount
:title: budget/budgetBreakdowns/0/budgetBreakdown/0/amount
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/finance/0/value
:title: budget/finance/0/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/milestones/0/value
:title: milestones/0/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/completion/finalValue
:title: completion/finalValue
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/costMeasurements/0/lifeCycleCosting/value
:title: costMeasurements/0/lifeCycleCosting/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/costMeasurements/0/costGroups/0/costs/0/value
:title: costMeasurements/0/costGroups/0/costs/0/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/value
:title: transactions/0/value
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
:jsonpointer: /projects/0/contractingProcesses/0/summary/milestones/0/value
:title: contractingProcesses/0/summary/milestones/0/value
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/social/laborBudget
:title: contractingProcesses/0/summary/social/laborBudget
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/social/landCompensationBudget
:title: social/landCompensationBudget
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/environment/abatementCost
:title: environment/abatementCost
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
:collapse: name,id,identifier,additionalIdentifiers,address,contactPoint,roles,beneficialOwners,classifications,people
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
* [`Finance/financingParty`](project-schema.json,/definitions/Finance,financingParty)
* [`PublicOffice/organization`](project-schema.json,/definitions/PublicOffice,organization)

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
:jsonpointer: /projects/0/publicAuthority
:title: publicAuthority
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/budgetBreakdowns/0/budgetBreakdown/0/sourceParty
:title: budget/budgetBreakdowns/0/budgetBreakdown/0/sourceParty
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/finance/0/financingParty
:title: budget/finance/0/financingParty
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/payer
:title: transactions/0/payer
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/transactions/0/payee
:title: transactions/0/payee
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
:jsonpointer: /projects/0/lobbyingMeetings/0/publicOffice/organization
:title: lobbyingMeetings/0/publicOffice/organization
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
* [`Meeting/address`](project-schema.json,/definitions/Meeting,address)

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

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/benefits/0/beneficiaries/0/location/address
:title: benefits/0/beneficiaries/0/location/address
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/social/consultationMeetings/0/address
:title: social/consultationMeetings/0/address
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/lobbyingMeetings/0/address
:title: lobbyingMeetings/0/address
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

### BudgetBreakdowns

`BudgetBreakdowns` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/BudgetBreakdowns
```

This sub-schema is referenced by the following properties:
* [`budget/budgetBreakdowns`](project-schema.json,,budget/budgetBreakdowns)

Each `BudgetBreakdowns` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/BudgetBreakdowns
:collapse: id,description,budgetBreakdown
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/budgetBreakdowns
:title: budget/budgetBreakdowns
```

````

`````

### BudgetBreakdown

For more information about this sub-schema, see the [OCDS Budget Breakdown extension documentation](https://extensions.open-contracting.org/en/extensions/budget/master/). `BudgetBreakdown` can also be extended further to include budget classifications data following the pattern described in the [OCDS Budgets and Spend extension](https://extensions.open-contracting.org/en/extensions/budget_and_spend/master/).

`BudgetBreakdown` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/BudgetBreakdown
```

This sub-schema is referenced by the following properties:
* [`BudgetBreakdowns/budgetBreakdown`](project-schema.json,/definitions/BudgetBreakdowns,budgetBreakdown)

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
:jsonpointer: /projects/0/budget/budgetBreakdowns/0/budgetBreakdown
:title: budget/budgetBreakdowns/0/budgetBreakdown
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
:jsonpointer: /projects/0/transactions
:title: transactions
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions
:title: contractingProcesses/0/summary/transactions
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
:collapse: id,title,type,description,code,dueDate,dateMet,dateModified,status,value
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/milestones
:title: milestones
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/milestones
:title: contractingProcesses/0/summary/milestones
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
:jsonpointer: /projects/0/transactions/0/relatedImplementationMilestone
:title: transactions/0/relatedImplementationMilestone
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/transactions/0/relatedImplementationMilestone
:title: contractingProcesses/0/summary/transactions/0/relatedImplementationMilestone
```

````

`````

### ClimateMeasure

`ClimateMeasure` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/ClimateMeasure
```

This sub-schema is referenced by the following properties:
* [`environment/climateMeasures`](project-schema.json,,environment/climateMeasures)

Each `ClimateMeasure` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/ClimateMeasure
:collapse: type,description
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/environment/climateMeasures
:title: environment/climateMeasures
```

````

`````

### ConservationMeasure

`ConservationMeasure` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/ConservationMeasure
```

This sub-schema is referenced by the following properties:
* [`environment/conservationMeasures`](project-schema.json,,environment/conservationMeasures)

Each `ConservationMeasure` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/ConservationMeasure
:collapse: type,description
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/environment/conservationMeasures
:title: environment/conservationMeasures
```

````

`````

### EnvironmentalMeasure

`EnvironmentalMeasure` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/EnvironmentalMeasure
```

This sub-schema is referenced by the following properties:
* [`environment/environmentalMeasures`](project-schema.json,,environment/environmentalMeasures)

Each `EnvironmentalMeasure` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/EnvironmentalMeasure
:collapse: type,description
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/environment/environmentalMeasures
:title: environment/environmentalMeasures
```

````

`````

### Finance

`Finance` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Finance
```

This sub-schema is referenced by the following properties:
* [`budget/finance`](project-schema.json,,budget/finance)
* [`ContractingProcessSummary/finance`](project-schema.json,/definitions/ContractingProcessSummary,finance)

Each `Finance` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Finance
:collapse: id,title,description,value,financingParty,financingPartyType,source,assetClass,type,repaymentPriority,concessional,resultsBased,period,paymentPeriod,paymentFrequency,exchangeRateGuarantee,stepInRights,relatedLots
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/budget/finance
:title: budget/finance
```

````

`````

### CostMeasurement

`CostMeasurement` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/CostMeasurement
```

This sub-schema is referenced by the following properties:
* [`costMeasurements`](project-schema.json,,costMeasurements)

Each `CostMeasurement` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/CostMeasurement
:collapse: id,date,costGroups
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/costMeasurements
:title: costMeasurements
```

````

`````

### CostGroup

`CostGroup` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/CostGroup
```

This sub-schema is referenced by the following properties:
* [`CostMeasurement/costGroups`](project-schema.json,/definitions/CostMeasurement,costGroups)

Each `CostGroup` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/CostGroup
:collapse: id,category,costs
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/costMeasurements/0/costGroups
:title: costMeasurements/0/costGroups
```

````

`````

### Cost

`Cost` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Cost
```

This sub-schema is referenced by the following properties:
* [`CostGroup/costs`](project-schema.json,/definitions/CostGroup,costs)

Each `Cost` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Cost
:collapse: id,classification,value
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/costMeasurements/0/costGroups/0/costs
:title: costMeasurements/0/costGroups/0/costs
```

````

`````

### LaborObligations

`LaborObligations` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/LaborObligations
```

This sub-schema is referenced by the following properties:
* [`ContractingProcessSummary/social/laborObligations`](project-schema.json,/definitions/ContractingProcessSummary,social/laborObligations)

Each `LaborObligations` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/LaborObligations
:collapse: obligations,description
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/social/laborObligations
:title: contractingProcesses/0/summary/social/laborObligations
```

````

`````

### Benefit

`Benefit` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Benefit
```

This sub-schema is referenced by the following properties:
* [`benefits`](project-schema.json,,benefits)

Each `Benefit` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Benefit
:collapse: title,description,beneficiaries
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/benefits
:title: benefits
```

````

`````

### Beneficiary

`Beneficiary` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Beneficiary
```

This sub-schema is referenced by the following properties:
* [`Benefit/beneficiaries`](project-schema.json,/definitions/Benefit,beneficiaries)

Each `Beneficiary` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Beneficiary
:collapse: location,description,numberOfPeople
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/benefits/0/beneficiaries
:title: benefits/0/beneficiaries
```

````

`````

### Sustainability

`Sustainability` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Sustainability
```

This sub-schema is referenced by the following properties:
* [`ContractingProcessSummary/tender/sustainability`](project-schema.json,/definitions/ContractingProcessSummary,tender/sustainability)

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

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/contractingProcesses/0/summary/tender/sustainability
:title: contractingProcesses/0/summary/tender/sustainability
```

````

`````

### Meeting

`Meeting` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Meeting
```

This sub-schema is referenced by the following properties:
* [`lobbyingMeetings`](project-schema.json,,lobbyingMeetings)
* [`Social/consultationMeetings`](project-schema.json,/definitions/Social,consultationMeetings)

Each `Meeting` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Meeting
:collapse: id,date,address,numberOfParticipants,publicOffice
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/social/consultationMeetings
:title: social/consultationMeetings
```

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/lobbyingMeetings
:title: lobbyingMeetings
```

````

`````

### PublicOffice

`PublicOffice` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/PublicOffice
```

This sub-schema is referenced by the following properties:
* [`Meeting/publicOffice`](project-schema.json,/definitions/Meeting,publicOffice)

Each `PublicOffice` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/PublicOffice
:collapse: organization,jobTitle
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/lobbyingMeetings/0/publicOffice
:title: lobbyingMeetings/0/publicOffice
```

````

`````

### Social

`Social` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/Social
```

This sub-schema is referenced by the following properties:
* [`social`](project-schema.json,,social)

Each `Social` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Social
:collapse: consultationMeetings,landCompensationBudget,inIndigenousLand,healthAndSafety
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/social
:title: social
```

````

`````

### HealthAndSafety

`HealthAndSafety` is defined as:

```{field-description} ../../build/current_lang/project-schema.json /definitions/HealthAndSafety
```

This sub-schema is referenced by the following properties:
* [`Social/healthAndSafety`](project-schema.json,/definitions/Social,healthAndSafety)

Each `HealthAndSafety` has the following fields:

`````{tab-set}

````{tab-item} Schema

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/HealthAndSafety
:collapse: 
:addtargets:
```

````

````{tab-item} Examples

```{jsoninclude} ../../docs/examples/example.json
:jsonpointer: /projects/0/social/healthAndSafety
:title: social/healthAndSafety
```

````

`````
