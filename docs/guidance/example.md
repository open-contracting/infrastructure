# Worked example

The [OC4IDS schema](../reference/index.md) sets out the structure and format of an OC4IDS JSON file.

This worked example is a fully completed OC4IDS JSON file representing a fictional, completed infrastructure project to upgrade a motorway in the UK.

The full OC4IDS JSON file for the worked example is available to download [here](../../../../_static/example.json) and this page contains excerpts from the example JSON file, showing how key sections of the schema should be populated.

## Overview

An OC4IDS document is made up of a number of sections. These include:

* **Project metadata** - contextual information about the project e.g. title, description, location and status.
* **Budget** - information about the projected costs or allocated budget for this project.
* **Parties** - information about the organizations and other participants involved in this project.
* **Documents** - documents and documentation relating to this project.
* **Contracting processes** - information about related contracting processes for different aspects of the project.
* **Completion** - information on the final scope, duration and costs for the project.

The full JSON file for the example project looks like this:

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer:  /projects/0
```   

## Sections

### Project metadata

This section provides contextual information about the project, including:

* `status` from the [Project Status codelist](../../../../reference/codelists/#projectstatus). In this example, the project status is 'completed'.

* `type` from the [Project Type codelist](../../../../reference/codelists/#projecttype). In this example, the project type is 'expansion'.

* `sector` from the [Project Sector codelist](../../../../reference/codelists/#projectsector). In this example, the sector is 'transport.road', the parent sector 'transport' is also included in the sector list, in line with the guidance in the schema.

* one or more `relatedProjects`, to reference other projects that are related to the same set of infrastructure assets, as [outlined in the schema reference](../../../../reference/schema/#relatedproject). In the relatedProject example below, a reference is made to the original project that initially constructed the motorway junctions, which are now being upgraded by this project.

* one or more `locations`, which may be expressed in a variety of ways as [outlined in the schema reference](../../../../reference/schema/#location). In this example, a motorway junction location is given, using a point location, a gazetteer entry and an address.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/relatedProjects
   :title: relatedProject

```

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/locations
   :expand:  geometry, gazetteer, address
   :title: location 1

```

### Budget and budget breakdown

The `budgetBreakdown` array in the `budget` section can be used to provide a breakdown of the budget by period and/or funding source.

In this example, the overall budget for the project covers 3 years and is broken down into amounts per year, with £10,000,000 allocated in 2016, as shown in the first `budgetBreakdown` component.

  ```eval_rst

  .. jsoninclude:: ../examples/example.json
     :jsonpointer: /projects/0/budget
     :expand: amount, budgetBreakdown/0
     :title: budget

  ```

  ```eval_rst

  .. jsoninclude:: ../examples/example.json
     :jsonpointer: /projects/0/budget/budgetBreakdown/0
     :expand: amount, period, sourceParty
     :title: budgetBreakdown

  ```

### Parties (organizations)

The `parties` array is used to provide details about organizations involved in the project and their roles. Organization references elsewhere in the data refer back to entries in this section.

In this example, details are given about the fictional Motorways UK entity, which is referred to from the `sourceParty` section in the `budgetBreakdown` example above, using the `name` and `id` from the entry in the `parties` section.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/parties/0
   :expand: address, contactPoint, roles
   :title: party

```

### Documents

The `documents` array is used to provide information and links to documents and documentation relating to the project. During different phases of the project, different document types are expected.

In this example, an environmental impact assessment is provided. The `documentType` field is used to categorize the document against the [Document Type codelist](../../../../reference/codelists/#documenttype).

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/documents/1
   :expand: address, contactPoint, roles
   :title: document

```
### Contracting processes

The `contractingProcesses` array is used to provide information about each contracting process associated with the project, including summary information, a list of modifications and a list of OCDS releases.

This example provides information about a contracting process for the design of the motorway upgrade, with one related document (a tender notice) and two related OCDS releases, one for the tender and one for the contract award.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/contractingProcesses/0
   :expand: summary, documents, releases
   :title: contractingProcess

```

#### Modifications

Each contracting process includes a `modifications` array which is used to list any changes to the duration, price, scope or other significant aspect of the contracting process.

This example shows a change in duration using the `oldContractPeriod` and `newContractPeriod` fields.

```eval_rst

.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/contractingProcesses/2/summary/modifications/0
   :expand: oldContractPeriod, newContractPeriod
   :title: modification

```

### Completion

The `completion` section provides final details of the scope, duration and cost for the project.

Since in this example there were variations to related contracting processes, the `finalValue` of the project exceeds its original planned budget.

```eval_rst
.. jsoninclude:: ../examples/example.json
   :jsonpointer: /projects/0/completion
   :expand:  finalValue
   :title: Completion

```
