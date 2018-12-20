# Evaluating disclosures against the Infrastructure Data Standard

The CoST Infrastructure Data Standard (IDS) is a framework for disclosure which is adapted by CoST national programmes to meet their local needs. This section sets out how to use the **project-level schema** and **OCDS** to assess coverage of published data against the IDS. For example, to monitor which elements of IDS are being supplied and whether they are available for all projects or only some.

```eval_rst
.. admonition:: Note
    :class: Note

    .. markdown::

      It is not possible to fully automate checks of whether disclosures from a particular publisher, or disclosures about a particular project, meet the requirements of the CoST IDS. For example, a human check may be needed to determine whether documents linked to from the data contain the required information.

```

## Getting started

*The following steps may require support from a technical expert. You can also contact the OCDS Helpdesk (<a href="mailto:data@open-contracting.org">data@open-contracting.org</a>) for guidance.*

### (1) Check your data formats

First, check that the disclosures you want to analyse are in the correct format. If they are not in the correct format, you will need to convert the data.

#### Project level data

Check whether the project-level data is published using the [project-level data specification](../projects/index.md)

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use a [JSON schema validator](https://json-schema.org/implementations.html#validators) to check that whether your data is in the correct format.

```

If the data isn’t published using the project-level data specification, use the [OC for Infrastructure Field-Level Mapping Template](https://docs.google.com/spreadsheets/d/1xHLf_w193pp97zfzhLc_LI-yEXrR_eyscga06Qo1blk/copy) to map the data to the specification and create an OC for Infrastructure JSON file for each project.

#### Contracting data

Check whether the contracting data is published using OCDS (Tip: You can use the OCDS Data Review tool for this).

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use the [OCDS Data Review Tool](http://standard.open-contracting.org/review/) to check that whether your data is published in OCDS format.

```

If the contracting data is published using OCDS then use it to populate the contracting processes section of the project-level data, following the guidance on [using contracting data to understand infrastructure projects](contracts-to-projects.md).

If the data isn’t published using OCDS, use the [OC for Infrastructure Field-Level Mapping Template](https://docs.google.com/spreadsheets/d/1xHLf_w193pp97zfzhLc_LI-yEXrR_eyscga06Qo1blk/copy) to map the data to the contracting processes section of the [project-level data specification](../projects/reference.md) and add the data to the OC for Infrastructure JSON files for each project.

### (2) Check which elements of IDS are disclosed

Use the [CoST IDS Mapping](../cost/index.md) to construct queries to determine which elements of the IDS are provided in the data.

For example, the CoST IDS mapping describes how the project name element of the IDS should be disclosed:

> Project-Level: Publish as `title`

Based on this description, the following pseudo code checks a folder containing OC for Infrastructure JSON files to count the number of  projects in which the project name is disclosed:

```
for each json file in folder
  load json
  if top-level "title" field exists in json and its value is not an empty string
    increment project name count by 1    
```
