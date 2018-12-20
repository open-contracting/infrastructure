<style>
.wy-nav-content {
max-width: 1200px;
}</style>

# CoST IDS & OCDS Mapping

CoST – the Infrastructure Transparency Initiative (CoST) is the leading global initiative improving transparency and accountability in public infrastructure.

The [CoST approach](http://infrastructuretransparency.org/our-approach/) is based on four core features:

* **Disclosure** - where procuring entities are asked to follow the CoST Infrastructure Data Standard. This describes 40 items of data that should be disclosed at key stages of an infrastructure project cycle.

* **Assurance** -  an independent review of the disclosed data by assurance teams based within CoST national programmes. Teams may identify key issues of concern from the data that has been disclosed, and will put technical terms into plain language to allow stakeholders to understand the issues, and hold decision makers to account.

* **Multi-stakeholder working** - each CoST national programme is managed by a stakeholder group including government, private sector and civil society.

* **Social accountability** - raising awareness of key issues arising from the assurance process, and engaging civil society and media to hold decision makers to account.

The 'Infrastructure Data Standard' is a **framework for disclosure** which has been adapted by a range of CoST national programmes, who have variously prioritised different elements based on their local needs, or who have included additional elements that they wish to monitor: particularly additional kinds of documentation that should be provided for each infrastructure project.

You can read more about the Infrastructure Data Standard in [CoST Guidance Note 6](http://infrastructuretransparency.org/resource/guidance-note-6-designing-a-disclosure-process/).

```eval_rst
.. admonition:: Frameworks and standards
    :class: Note

    .. markdown::

        There is an important distinction between the Infrastructure Data Standard (IDS) and the Open Contracting Data Standard (OCDS). IDS provides a framework to identify *categories of information* that should be disclosed. OCDS describes *specific fields* and how they should be structured as data.

        The Project-Level Data Specification on this site acts as a bridge between the IDS framework, and the idea of a more structured technical data standard.

```

## Mapping to IDS and from OCDS

<!-- Note - mappings come from https://docs.google.com/spreadsheets/d/1tpXKCrNY1vUEPo6O1j-GPhxgSna7CZ5uwz_eTNLEOr8/edit#gid=2054628701 -->

The following mapping tables describe:

* How each element of the CoST Infrastructure Data Standard can be represented as **structured data** using the [Project-Level Data Specification](../projects/index.md), in the 'Mapping to OC for Infrastructure' column.

* How existing OCDS data can be used to populate project-level and contracting process summary data, in the 'Mapping from OCDS' column.

```eval_rst
.. admonition:: Mapping from OCDS
    :class: Note

    .. markdown::

        Some mappings use fields from [OCDS extensions](http://standard.open-contracting.org/latest/en/extensions/). In these cases, the names of extensions are noted in parentheses; where possible, alternative mappings are provided that use only fields from the core OCDS schema.

```

### Project level

#### Project identification

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 30 30 10
   :file: ../../build/current_lang/project-level-identification.csv
```

#### Project preparation

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 30 30 10
   :file: ../../build/current_lang/project-level-preparation.csv
```

#### Project completion

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 30 30 10
   :file: ../../build/current_lang/project-level-completion.csv
```

### Process level

#### Procurement

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 30 30 10
   :file: ../../build/current_lang/process-level-procurement.csv
```

#### Implementation

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 30 30 10
   :file: ../../build/current_lang/process-level-implementation.csv
```

### Reactive disclosures

The CoST IDS also sets out a number of data points under the heading of 'reactive disclosure'. It is possible to also disclose many of these fields **pro-actively** either as **document** entries with free text or linked documents, or using structured OCDS fields and extensions.

Specifically:

* Details of a individuals involved at the project or contract level can be included in the ``parties`` array with a suitable role. Role is an open codelist. As individuals will not have an 'organization identifier' a locally defined identifier may be used instead.

* Plans, reports and assessments may be included in the project or contracting process level `documents` blocks, or may be published within individual OCDS releases.

* The [budget_breakdown](https://github.com/open-contracting-extensions/ocds_budget_breakdown_extension) and [budget_and_spend](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension) extensions can be used to provide guidance on modelling detailed financial information.
