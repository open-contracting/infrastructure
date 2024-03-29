# Assessing compliance with the CoST IDS

The CoST Infrastructure Data Standard (IDS) is a framework for disclosure which is adapted by CoST national programmes to meet their local needs. This section sets out how to use **OC4IDS** and **OCDS** to assess coverage of published data against the IDS. For example, to monitor which elements of IDS are being supplied and whether they are available for all projects or only some.

```{note}
It is not possible to fully automate checks of whether disclosures from a particular publisher, or disclosures about a particular project, meet the requirements of the CoST IDS. For example, a human check might be needed to determine whether documents linked to from the data contain the necessary information.
```

## Getting started

*The following steps might require support from a technical expert. You can also contact the OC4IDS Helpdesk ([data@open-contracting.org](mailto:data@open-contracting.org)) for guidance.*

### (1) Check your data formats

First, check that the disclosures you want to analyze are in the correct format. If they are not in the correct format, you will need to convert the data.

#### Project level data

Check whether the project-level data is published using [OC4IDS](../../projects/index)

```{tip}
You can use the [OC4IDS Data Review Tool](https://review-oc4ids.standard.open-contracting.org/) to check that whether your data is in the correct format.
```

If the data isn’t published using OC4IDS, use the [OC4IDS Field-Level Mapping Template](https://www.open-contracting.org/resources/oc4ids-field-level-mapping-template/) to map the data to the specification and create an OC4IDS JSON file for each project.

```{tip}
You can use a [blank example OC4IDS JSON file](../examples/blank.json) to get started.
```

#### Contracting data

Check whether the contracting data is published using OCDS.

```{tip}
You can use the [OCDS Data Review Tool](https://review.standard.open-contracting.org/) to check that whether your data is published in OCDS format.
```

If the contracting data is published using OCDS then use it to populate the contracting processes section of the project-level data, following the guidance on [using contracting data to understand infrastructure projects](using).

If the data isn’t published using OCDS, use the [OC4IDS Field-Level Mapping Template](https://www.open-contracting.org/resources/oc4ids-field-level-mapping-template/) to map the data to the [contracting processes](../reference/schema.md#contractingprocess) section of OC4IDS and add the data to the OC4IDS JSON file for each project.

### (2) Check which elements of IDS are disclosed

Use the [CoST IDS Mapping](../../cost/index) to construct queries to determine which elements of the IDS are provided in the data.

For example, the CoST IDS mapping describes how the project name element of the IDS ought to be disclosed:

> Project-Level: Publish as `title`

Based on this description, the following pseudo code checks a folder containing OC4IDS JSON files to count the number of projects in which the project name is disclosed:

```none
for each json file in folder
  load json
  if top-level "title" field exists in json and its value is not an empty string
    increment project name count by 1    
```
