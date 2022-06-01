# Project identifiers

A project identifier is a unique identifier for an infrastructure project. Every project in OC4IDS has a project identifier in the `id` field.

Project identifiers can be used to join up data published at different times or from different systems; for example, including a project identifier in contracting data makes it possible to join up data on the design, construction and supervision contracts within a single infrastructure project.

## Local project identifiers in contracting data

A common need is to access data about the contracting processes related to an infrastructure project. When contracting systems use consistent identifiers to refer to infrastructure projects, this becomes possible. An example use case is automatically checking which projects have related contracting data, and then manually filtering projects for further scrutiny, monitoring or data collection.

Project identifiers in contracting data ought to be locally unique; this means that across all contracting data from a particular system or country, each project identifier refers to exactly one infrastructure project.

There are different approaches to including project identifiers in contracting data, with the best solution depending on the context of an implementation:

* **Include a free-text field for project identifiers in procurement systems** and work with officials entering procurement information to make sure this is populated according to a defined pattern.

  Free-text entry of project identifiers can lead to data quality issues; for example, project identifiers can be mistyped or two groups can accidentally choose to use the same identifier for different projects.

  However, this approach allows some data quality checks to be run; for example, checking that all the contracting processes over a certain value from a given agency have a project identifier, and that the identifier matches a defined pattern or a local list of project identifiers.

  This approach also enables the joining up of data on multiple contracting processes relating to a single infrastructure project.

* **Establish a national project register managed by a central agency and integrated into procurement systems.** In this model, officials entering procurement information would look up and use the project's identifier from the national register. If the project is not yet in the register, they would request its addition.

  This approach supports more comprehensive and effective data quality checks; for example, project identifiers entered into procurement systems can be immediately checked against the project register to prevent errors in data entry ("validation at source").

  A central register can ensure that project identifiers are locally unique, and more robustly supports use cases like identifying projects lacking related contracts.

  However, this approach requires political will and technical capacity to establish the central register and integrate it into procurement systems, and it requires an appropriate central actor to manage it.

### Project identifiers in OCDS

In OCDS, the identifier for the individual infrastructure project to which a contracting process is related ought to be disclosed using the `planning/project/id` field, introduced in the [Project extension](https://extensions.open-contracting.org/en/extensions/project/).

The `planning/budget/projectID` field in OCDS ought **not** be used to disclose the identifier for an individual infrastructure project. This field is used to disclose the identifier for a project in the national budget to which the contracting process is related. Since projects in the national budget might include many individual infrastructure projects, it is necessary to disclose these identifiers separately.

## Project identifier prefixes

Project identifiers in OC4IDS need to be globally unique; this means that, across all the data of all OC4IDS publishers, each project identifier refers to exactly one infrastructure project.

If local project identifiers are available in existing systems or data, these ought to be re-used to create globally unique project identifiers for use in OC4IDS. Otherwise, if local project identifiers are not available, publishers are allowed to assign local identifiers to projects in the new systems used to generate OC4IDS data.

To make local project identifiers globally unique for use in OC4IDS, a publisher requests a project identifier prefix from the [OC4IDS Helpdesk](mailto:data@open-contracting.org). The publisher needs to then use the assigned prefix in all its project identifiers, according to following structure: `[project identifier prefix]-[local project identifier]`.

For example: CoST Honduras requests a project identifier prefix from the OC4IDS Helpdesk. The OC4IDS Helpdesk assigns the randomly-generated prefix `oc4ids-qu8r7p`. CoST Honduras then creates globally unique project identifiers, by combining its assigned prefix with each local project identifier from its SISOCS system.

Project identifier prefixes are typically unique to each publisher. However, multiple publishers in the same jurisdiction can collaboratively decide to use the same project identifier prefix: for example, if multiple agencies are independently responsible for different projects. As such, the prefix serves to identify a series of infrastructure projects (to which many publishers can contribute), rather than to identify one publisher.

```{admonition} Request a project identifier prefix
:class: tip

To request a project identifier prefix, please e-mail [data@open-contracting.org](mailto:data@open-contracting.org) with the name of your organization and a brief description of your OC4IDS implementation.
```

### Existing prefixes

The list below shows all registered prefixes. You can [download the list as CSV](https://docs.google.com/spreadsheets/d/e/2PACX-1vTWtoIa_26k35bmZVGiAziNMvdUgDS93ZM2j99XidgHaoQxm9C2dbnblckB0ZF7NUKJ6RrpDS7OQvxl/pub?gid=506986894&single=true&output=csv).

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTWtoIa_26k35bmZVGiAziNMvdUgDS93ZM2j99XidgHaoQxm9C2dbnblckB0ZF7NUKJ6RrpDS7OQvxl/pubhtml?gid=506986894&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="500"></iframe>
