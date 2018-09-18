# Project level data

Structured data on infrastructure projects should be provided using the project level schema. 

This includes:

* Overview information about the project, summary text and links to external projects
* A list of the contracting processes the project involves
* Summary details about each of those contracting processes - most of which should be derived automatically from OCDS data
* A change history for each contracting process, with details of variations in value, timing and scope and explanations of these changes
* Project completion information

## Project level

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :include: 
    :collapse: period,sector,additionalClassifications,locations,budget/amount,budget/budgetBreakdown,parties,documents,contractingProcesses

```

## ContractingProcess


```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :include: 
    :pointer: /definitions/ContractingProcess
    :collapse: releaseList

```


## ReleaseList

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :include: 
    :pointer: /definitions/ReleaseListEntry
    :collapse: releaseList

```


## Components

### Classification

A classification consists of an identifier for the codelist (the `scheme`) and a code from that codelist (the `id`), and then a human-readable label for the classification (the `description`). 

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
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

### Organization

For each organization, provide as much structured data as you can.

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Organization
    :include: 
    :collapse: identifier,additionalIdentifiers,address,contactPoint

```

### OrganizationReference

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/OrganizationReference
    :include: 
    :collapse: 

```

### Identifier

Use of stable official organisation identifiers can help join up data between systems. 

Organization identifiers should be constructed by collecting an official company (or government body) registration number for the organisation, and then finding the [org-id.guide list code](http://www.org-id.guide) for the list this identifier is taken from to use in the `scheme` field. 

For example, if identifying a company in Colombia, look up its identifier in the [Unified Commercial and Social Registry](http://org-id.guide/list/CO-RUE) and use the list code `CO-RUE`. 

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Identifier
    :include: 
    :collapse: 

```


### Locations

A project may have one or more locations. Locations may be expressed in a number of different ways, using one or more of:

* A point location or geometry (e.g. trace of a road, or polygon giving the boundary of a site);
* A gazetteer entry (e.g. town name);
* An address.

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Identifier
    :include: 
    :collapse: 

```

### Address

We use properties from schema.org and vCard for address components. In the event source data cannot be broken down into these parts, data SHOULD contain at least a streetAddress value and postal code. 

When working with data, users should be aware that addresses may not always be broken down using all the properties the specification provides.

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Address
    :include: 
    :collapse: 

```

### ContactPoint

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/ContactPoint
    :include: 
    :collapse: 

```

### Document

For each document the following structured information may be provided. 

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Document
    :include: 
    :collapse: 

```


### Value

All values should be published along with their currency using the following structure. 

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Value
    :include: 
    :collapse: 

```


### BudgetBreakdown

A budget breakdown is provided through an array of `BudgetBreakdown` objects, each of which represents budget for a particular period, from a particular source, or a combination of the two. 

See the [documentation of the OCDS Budget Breakdown extension](https://github.com/open-contracting/ocds_budget_breakdown_extension) for more details of this data model. BudgetBreakdown can also be extended further to included budget classifications data following the pattern described in the [OCDS Budgets and Spend extension](https://github.com/open-contracting/ocds_budget_and_spend_extension).

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/BudgetBreakdown
    :include: 
    :collapse: 

```

### Period

Dates MUST be expressed using a full ISO 8601 date-time including a timezone. E.g.:

> 2018-09-18T11:26:04+01:00

Where the source system does not contain time information, a judgement should be made as to the relevant time to attach (e.g. start of the day; end of the working day etc.). 

```eval_rst

.. jsonschema:: ../../build/current_lang/project-schema.json
    :pointer: /definitions/Period
    :include: 
    :collapse: 

```

## Worked example

