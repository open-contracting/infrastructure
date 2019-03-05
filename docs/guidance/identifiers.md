# Project identifiers

A project identifier is a globally unique identifier for an infrastructure project. Every project in OC4IDS has a project identifier in the `id` field.

Project identifiers can be used to join up information published at different times or from different systems, for example, including a project identifier in contracting data enables information on the design, construction and supervision contracts for a single infrastructure project to be joined up.

## Project identifiers in contracting data

With an authoritative list of infrastructure projects in a country to draw on, and if the identifiers it assigned are used within contracting systems, it would be possible to automatically check which projects have published contracting information, and to analyse that data to identify projects where further scrutiny, monitoring and data collection should take place.

There are different approaches to including project identifiers in contracting data, with the best solution depending on the context of an implementation:

* **Include an open field for project identifiers in procurement systems** and work with each department entering data to make sure this is populated according to some defined pattern.

  This would allow some checks to be run, for example, checking that all the contracting processes over a certain value from a given agency have a project identifier, and that the identifier matches a known pattern or a local identifier list.

  This would also allow data on several contracting processes relating to a single project to be joined up, however allowing free-text entry of project identifiers would likely lead to issues with data quality and could result in identifier clash between projects from different agencies or departments.
  

* **Establish a national project register managed by a central agency and integrated into procurement systems.** In this model, officials entering procurement information would look up a project from the national register to include its identifier in contracting data, and would have to request its addition if it was not already in the register.

  This would allow validation ‘at source’ of the project identifier and would support checks on how many projects have no associated contracts, however it would require the availability of a central actor, the political will and the technical capacity to establish and maintain a register.

## Globally unique identifiers

The project identifier should be globally unique, this means that across data from all OC4IDS publishers, it should refer to one specific infrastructure project.

To make the project identifier globally unique the OC4IDS helpdesk assigns a prefix which publishers must add to existing project identifiers, using the following identifier structure: `[project identifier prefix]-[existing project identifier]`

```eval_rst
.. admonition:: Request a project identifier prefix
    :class: tip

    .. markdown::

        To request a project identifier prefix, contact the OC4IDS helpdesk by emailing <a href="mailto:data@open-contracting.org">data@open-contracting.org</a> and provide the name of your organization.

```
