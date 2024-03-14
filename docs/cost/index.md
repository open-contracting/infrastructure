# CoST IDS & OCDS mapping

<style>
.wy-nav-content {
  max-width: 1200px;
}
</style>

CoST – the Infrastructure Transparency Initiative (CoST) is the leading global initiative improving transparency and accountability in public infrastructure.

The [CoST approach](https://infrastructuretransparency.org/our-approach/) is based on four core features:

* **Disclosure** - where procuring entities are asked to follow the CoST Infrastructure Data Standard. This describes 40 items of data that ought to be proactively disclosed at key stages of an infrastructure project cycle.

* **Assurance** - an independent review of the disclosed data by assurance teams based within CoST national programmes. Teams identify key issues of concern analyzing the data that has been disclosed, and will put technical terms into plain language to allow stakeholders to understand the issues, and hold decision makers to account.

* **Multi-stakeholder working** - each CoST national programme is managed by a stakeholder group including government, private sector and civil society.

* **Social accountability** - raising awareness of key issues arising from the assurance process, and engaging civil society and media to hold decision makers to account.

The 'Infrastructure Data Standard' is a **framework for disclosure** which has been adapted by a range of CoST national programmes, who have variously prioritized different elements based on their local needs, or who have included additional elements that they wish to monitor: particularly additional kinds of documentation that ought to be provided for each infrastructure project.

You can read more about the Infrastructure Data Standard on the [CoST website](https://infrastructuretransparency.org/our-approach/disclosure/).

```{admonition} Frameworks and standards
:class: note

There is an important distinction between the Infrastructure Data Standard (IDS) and the Open Contracting Data Standard (OCDS). IDS provides a framework to identify *categories of information* that ought to be disclosed. OCDS describes *specific fields* and how they should be structured as data.

The [Open Contracting for Infrastructure Data Standard (OC4IDS)](../projects/index) documented on this site acts as a bridge between the IDS framework, and the idea of a more structured technical data standard.
```

<!-- Note - mappings come from https://docs.google.com/spreadsheets/d/1tpXKCrNY1vUEPo6O1j-GPhxgSna7CZ5uwz_eTNLEOr8/edit#gid=2054628701 -->

The pages in this section document two mappings:

* The [**CoST IDS to OC4IDS**](ids/index.md) mapping describes how to represent each element of the CoST IDS as structured data using OC4IDS. Use this mapping if you already collect data according to the CoST IDS and you want to publish your data using OC4IDS, or if you want to make sure that your OC4IDS publication conforms to the CoST IDS.
* The [**OCDS to OC4IDS**](ocds.md) mapping describes how to use OCDS data to populate the sections of an OC4IDS file which relate to the CoST IDS. Use this mapping if you have access to OCDS data on infrastructure contracting processes and you want to create a summary by project in OC4IDS format, or if you want to check which CoST IDS elements your OCDS data covers.

The organization of the mapping tables reflects the structure of the CoST IDS, which is described in [Getting Started](../projects/index).

The mapping tables use `/` notation to reference fields in OCDS data, e.g. `/tender/status`, and `.` notation to reference fields in the OC4IDS schema, e.g. `.budget.approvalDate`.

```{toctree}
:maxdepth: 1
:hidden:

ids/index.md
ocds
common
```
