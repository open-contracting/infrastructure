# Assessing compliance with the CoST IDS

The CoST Infrastructure Data Standard (IDS) is a framework for disclosure which is adapted by CoST national programmes to meet their local needs. This section sets out how to use **OC4IDS** and **OCDS** to assess coverage of published data against the IDS. For example, to monitor which elements of IDS are being supplied and whether they are available for all projects or only some.

```eval_rst
.. admonition:: Note
    :class: Note

    .. markdown::

      It is not possible to fully automate checks of whether disclosures from a particular publisher, or disclosures about a particular project, meet the requirements of the CoST IDS. For example, a human check may be needed to determine whether documents linked to from the data contain the required information.

```

## Getting started

*The following steps may require support from a technical expert. You can also contact the OC4IDS Helpdesk (<a href="mailto:data@open-contracting.org">data@open-contracting.org</a>) for guidance.*

### (1) Check your data formats

First, check that the disclosures you want to analyze are in the correct format. If they are not in the correct format, you will need to convert the data.

#### Project level data

Check whether the project-level data is published using [OC4IDS](../projects/index.md)

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use the [OC4IDS Data Review Tool](https://standard.open-contracting.org/infrastructure/review/) to check that whether your data is in the correct format.

```

If the data isn’t published using OC4IDS, use the [OC4IDS Field-Level Mapping Template](https://www.open-contracting.org/resources/oc4ids-field-level-mapping-template/) to map the data to the specification and create an OC4IDS JSON file for each project.

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use a [blank example OC4IDS JSON file](../../../_static/blank.json) to get started.

```

#### Contracting data

Check whether the contracting data is published using OCDS (Tip: You can use the OCDS Data Review tool for this).

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use the [OCDS Data Review Tool](https://standard.open-contracting.org/review/) to check that whether your data is published in OCDS format.

```

If the contracting data is published using OCDS then use it to populate the contracting processes section of the project-level data, following the guidance on [using contracting data to understand infrastructure projects](using.md).

If the data isn’t published using OCDS, use the [OC4IDS Field-Level Mapping Template](https://www.open-contracting.org/resources/oc4ids-field-level-mapping-template/) to map the data to the [contracting processes](../../../../reference/schema/#contractingprocess) section of OC4IDS and add the data to the OC4IDS JSON file for each project.

### (2) Check which elements of IDS are disclosed

Use the [CoST IDS Mapping](../cost/index.md) to construct queries to determine which elements of the IDS are provided in the data.

For example, the CoST IDS mapping describes how the project name element of the IDS should be disclosed:

> Project-Level: Publish as `title`

Based on this description, the following pseudo code checks a folder containing OC4IDS JSON files to count the number of  projects in which the project name is disclosed:

```
for each json file in folder
  load json
  if top-level "title" field exists in json and its value is not an empty string
    increment project name count by 1    
```
