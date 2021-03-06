<style>
.wy-nav-content {
  max-width: 1200px;
}
</style>

# Schema reference

The tables below describe each of the fields and objects in OC4IDS. To see how they fit together, consult the [schema browser](browser).

## Project

```{jsonschema} ../../build/current_lang/project-schema.json
:include:
:collapse: period,assetLifetime,sector,additionalClassifications,locations,budget/amount,budget/budgetBreakdown,parties,documents,contractingProcesses,relatedProjects
```

## ContractingProcess

```{jsonschema} ../../build/current_lang/project-schema.json
:include:
:pointer: /definitions/ContractingProcess
:collapse: releases,summary
```

## ContractingProcessSummary

```{jsonschema} ../../build/current_lang/project-schema.json
:include:
:pointer: /definitions/ContractingProcessSummary
:collapse: documents
```

## LinkedRelease

```{jsonschema} ../../build/current_lang/project-schema.json
:include:
:pointer: /definitions/LinkedRelease
```

## Components

### Address

We use properties from schema.org and vCard for address components. In the event source data cannot be broken down into these parts, data SHOULD contain at least a streetAddress value and postal code.

When working with data, users should be aware that addresses may not always be broken down using all the properties the specification provides.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Address
:include:
:collapse:
```

### BudgetBreakdown

A budget breakdown is provided through an array of `BudgetBreakdown` objects, each of which represents budget for a particular period, from a particular source, or a combination of the two.

See the [documentation of the OCDS Budget Breakdown extension](https://github.com/open-contracting-extensions/ocds_budget_breakdown_extension) for more details of this data model. BudgetBreakdown can also be extended further to include budget classifications data following the pattern described in the [OCDS Budgets and Spend extension](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension).

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/BudgetBreakdown
:include:
:collapse:
```

### Classification

A classification consists of an identifier for the codelist (the `scheme`) and a code from that codelist (the `id`), and then a human-readable label for the classification (the `description`).

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Classification
:include:
:collapse:
```

For example:

```json
{
    "scheme":"COFOG",
    "id":"05.2",
    "description":"Waste water management"
}
```

### ContactPoint

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/ContactPoint
:include:
:collapse:
```

### Document

For each document the following structured information may be provided.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Document
:include:
:collapse:
```

### Identifier

Use of stable official organization identifiers can help join up data between systems.

Organization identifiers should be constructed by collecting an official company (or government body) registration number for the organization, and then finding the [org-id.guide list code](http://www.org-id.guide) for the list this identifier is taken from to use in the `scheme` field.

For example, if identifying a company in Colombia, look up its identifier in the [Unified Commercial and Social Registry](http://org-id.guide/list/CO-RUE) and use the list code `CO-RUE`.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Identifier
:include:
:collapse:
```

### Location

A project may have one or more locations. Locations may be expressed in a number of different ways, using one or more of:

* A point location or geometry (e.g. trace of a road, or polygon giving the boundary of a site);
* A gazetteer entry (e.g. town name);
* An address.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Location
:include:
:collapse: address
```

### Modification

For each modification, the following structured information may be provided.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Modification
:include:
:collapse:
```

### Organization

For each organization, provide as much structured data as you can.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Organization
:collapse: identifier,additionalIdentifiers,address,contactPoint
```

### OrganizationReference

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/OrganizationReference
:include:
:collapse:
```

### Period

Dates MUST be expressed using a full ISO 8601 date-time including a timezone. E.g.:

> 2018-09-18T11:26:04+01:00

Where the source system does not contain time information, a judgment should be made as to the relevant time to attach (e.g. start of the day; end of the working day etc.).

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Period
:include:
:collapse:
```

### Person

Use this object when you need to disclose the details of people associated with, representing or working on behalf of an organization involved in the project.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Person
:include:
:collapse:
```

### RelatedProject

A reference to a project related to the same set of infrastructure assets as the current project.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/RelatedProject
:include:
:collapse:
```

### Transaction

A spending transaction related to a contracting process.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Transaction
:include:
:collapse:
```

### Value

All values should be published along with their currency using the following structure.

```{jsonschema} ../../build/current_lang/project-schema.json
:pointer: /definitions/Value
:include:
:collapse:
```
