# Publishing data from an infrastructure transparency portal

OC4IDS can be used to publish standardized open data on infrastructure projects where information is already collected and disclosed through infrastructure transparency portals, whether by CoST Multi-Stakeholder Groups, government agencies or civil society organizations.

Publishing standardized open data reduces barriers to use of data and supports the development of reusable tools and methodologies for working with data on infrastructure projects.

If you also collect detailed data on contracting processes, this can be published using the [Open Contracting Data Standard (OCDS)](https://standard.open-contracting.org/1.1/en/).

```{admonition} Linking to related information
:class: Tip

Infrastructure transparency portal creators ought to consider what other types of information might be important to citizens, in addition to the in depth scrutiny related information in OC4IDS.

For example, [Highways England](https://highwaysengland.co.uk/roads/) provides links to congestion and traffic restriction information alongside information on roads projects.
```

## Getting started

*Some of the following steps might require support from a technical expert. You can also contact the OC4IDS Helpdesk ([data@open-contracting.org](mailto:data@open-contracting.org)) for guidance.*

### (1) Make a commitment

Consider making or advocating for a public commitment to publish standardized open data using OC4IDS and OCDS.

Commitments are important to help align implementation with the goals of publishing open data and to help overcome technical, political or bureaucratic barriers to publication.

Applications to join [CoST](http://infrastructuretransparency.org/) can be used to make a commitment or if your country is a member of the [Open Government Partnership](https://www.opengovpartnership.org/), your National Action Plan is another great place to start.

Refer to the [OCDS implementation journey](https://standard.open-contracting.org/latest/en/guidance/design/) for information and resources about making commitments related to OCDS. Refer to the [CoST and OGP guidance note](http://infrastructuretransparency.org/wp-content/uploads/2018/07/Guidance-Note-CoST-and-OGP-.pdf) for guidance on making OGP commitments related to CoST.

### (2a) Map project-level data and summary contracting process data

Map existing data structures to [OC4IDS](../../projects/index).

```{tip}
The [OC4IDS Field-Level Mapping Template](https://www.open-contracting.org/resources/oc4ids-field-level-mapping-template/) can be used to document your mapping.

To learn how to use the mapping template, see the [tutorial](https://www.open-contracting.org/resources/oc4ids-field-level-mapping-template-tutorial/).
```

Your mapping might identify:

* **Gaps in your data** where data in OC4IDS is not currently collected or disclosed in your system. Use OC4IDS as a guide to the information that is important to users and consider whether your system and business processes could be updated to collect and publish additional information.

* **Gaps in OC4IDS** where data is collected by your system but doesn't map to OC4IDS. Rather than being excluded from your publication, such information ought to be included as additional fields in your data. Refer to [extending the schema](../reference/index.md#extending-the-schema) for information on including additional fields in your data.

### (2b) Map detailed contracting process data

If you collect detailed data on contracting processes, refer to the [OCDS implementation journey](https://standard.open-contracting.org/latest/en/guidance/map/) for information and resources about mapping and publishing your contracting data using OCDS.

Include an identifier for the infrastructure project that each contracting process relates to in your OCDS data, following the guidance on [project identifiers in OCDS](identifiers.md#project-identifiers-in-ocds).

### (3) Build your data, systems and processes

Create an OC4IDS JSON file for each project your system has information on and use the [OC4IDS Data Review Tool](https://standard.open-contracting.org/infrastructure/review/) to check that the files are structurally correct against OC4IDS.

```{tip}
You can use a {download}`blank example OC4IDS JSON file <../examples/blank.json>` to get started.
```

If you are also publishing contracting data using OCDS, create an OCDS release each time the data about a contracting process changes and use the [OCDS Data Review Tool](https://standard.open-contracting.org/review/) to check your OCDS releases.

Make sure you have systems and/or business processes in place to keep the data you produce up to date.

### (4) Publish your data

Publish your OC4IDS JSON fields (as either static files or via an API) at a stable URL, such as:

> `http://{your-website}/opendata/projects/{project-id}.json`

If you are also publishing contracting data using OCDS, publish each new release of data as a JSON file at a stable URL such as:

> `http://{your-website}/opendata/contracting/{ocid}/{release-id}.json`

Make sure your project-level files include links in the `contractingProcesses/releases` section to each related OCDS file.

To make your data easier to access, consider providing:

* A regularly updated bulk file of all your data for download
* Flattened (spreadsheet or CSV) representations of your data
* A page on your website with details of how users can access your data

````{tip}
You can use [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/) to convert OC4IDS data between JSON and CSV/Excel formats. For example, the following command converts the [example project package](https://standard.open-contracting.org/infrastructure/latest/en/_static/example.json) to Excel format:

```shell
flatten-tool flatten -f xlsx example.json --root-id=id --root-list-path=projects
```
````

Refer to the [OCDS documentation](https://standard.open-contracting.org/1.1/en/guidance/build/hosting/#data-files-apis-and-discovery) for more information on providing data in multiple formats.
