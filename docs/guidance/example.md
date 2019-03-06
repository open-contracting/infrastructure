# Worked example

The [OC for infrastructure schema](../../../../projects/schema) sets out the fields that should be included in each section. We have generated some fictional data as an example. This page outliens how key sections of this data are populated.

## Overview  

An OC for infrastructure document is made up of a number of sections. These include:
* **Project metadata** - contextual information about the project e.g. title, description, location and status.
* **Budget** - information about the projected costs or allocated budget for this project.
* **Parties** - information about the organizations and other participants involved in this project.
* **Documents** - information about documentation relating to this project.
* **Contracting processes** - information about related contracting processes across different project phases.
* **Completion** - final timing and values relating to the project.

The schema makes use of simple components to represent data, e.g. budget breakdown components within budget, parties (organizational entities), documents, contracting processes, and a completion component.

Our example is a fictional project to upgrade a motorway in the UK, which has been completed. The project is represented in a JSON document as follows:

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer:  
```   

## Sections

### Project metadata
This provides contextual information about the project, including:
* *status*, from the [Project Status codelist](../../../../projects/reference/#projectstatus). In this example, the project status is *"completed"*.
* *type*, from the [Project Type codelist](../../../../projects/reference/#projecttype). In this example, the project type is *"construction"*.
* *sector*, the main sector this project relates to, from the [type of assets by sector guidance](https://ppp-certification.com/ppp-certification-guide/4-where-ppps-are-used-%E2%80%93-infrastructure-sectors). In this example, the sector is *"Economic– transport > roads"*.
* one or more *locations*, which may be expressed in a variety of ways as [outlined in the specification reference](../../../../projects/reference/#locations). In this example, a motorway junction location is given, using a point location, a gazetteer entry and an address.
```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /locations
   :expand:  geometry, gazetteer, address
   :title: location 1

```

### Budget and budget breakdown
Multiple *budget breakdown* components within the *budget* section provide details of the budget by period and/or participating funders. In this example, from the overall budget, £10,000,000 was allocated in 2016, as shown in the first *budget breakdown* component.
  ```eval_rst

  .. jsoninclude:: ../examples/example.json
     :jsonpointer: /budget
     :expand: amount, budgetBreakdown/0
     :title: budget

  ```

  ```eval_rst

  .. jsoninclude:: ../examples/example.json
     :jsonpointer: /budget/budgetBreakdown/0
     :expand: amount, period, sourceParty
     :title: budgetBreakdown

  ```
### Parties (Organizations)

An array of *party* components provide details about organizations, economic operators and other participants involved in the project and their roles. Organization references elsewhere in the data refer back to entries in this list. In this example, details are given about the fictional Motorways UK entity, which is referred to from the *sourceParty* section in the *budget breakdown* example above, using its *name* and *id*.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /parties/0
   :expand: address, contactPoint, roles
   :title: party

```


### Documents

An array of *document* components provide information about a piece of documentation relating to this project. During different phases of the project, different *document types* are expected. In this example, a consultation document is provided. The publisher has provided an additional entry to the [document type open codelist](../../../../projects/reference/#documenttype) by prefixing an x_.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /documents/0
   :expand: address, contactPoint, roles
   :title: document

```
### Contracting processes

An array of *contracting process* components provide an index, summary and change history about related contracting processes across the different project phases of design, construction and supervision. This example provides information about a design phase (specified in the *summary/nature* array), with one related *document* (a tender notice), and 2 releated OCDS releases (given in the *releases* array), one for the tender and one for the award.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /contractingProcesses/0
   :expand: summary, documents, releases
   :title: contractingProcess

```

#### Variations

Contracting processes also contain *variation* components to detail any changes to its duration, price, scope or other significant features. This example shows a change in duration using the *oldContractPeriod* and *newContractPeriod* components.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /contractingProcesses/2/summary/variations/0
   :expand: oldContractPeriod, newContractPeriod
   :title: variation

```

### Completion
The single *completion* component provides final timing and values relating to the project. Since in this example there were variations to related contracting processes, the *finalValue* of the project exceeds its original planned budget.

```eval_rst
.. jsoninclude:: ../examples/example.json
   :jsonpointer: /completion
   :expand:  finalValue
   :title: Completion

```

## Full example
The full worked example JSON file is available [here](../../../../_static/example.json).
