<style>
.wy-nav-content {
max-width: 1200px;
}</style>

# CoST IDS & OCDS Mapping

CoST – the Infrastructure Transparency Initiative (CoST) is the leading global initiative improving transparency and accountability in public infrastructure.

The [CoST approach](http://infrastructuretransparency.org/our-approach/) is based on four core features:

* **Disclosure** - where procuring entities are asked to follow the CoST Infrastructure Data Standard. This describes 40 items of data that should be proactively disclosed at key stages of an infrastructure project cycle.

* **Assurance** -  an independent review of the disclosed data by assurance teams based within CoST national programmes. Teams may identify key issues of concern analyzing the data that has been disclosed, and will put technical terms into plain language to allow stakeholders to understand the issues, and hold decision makers to account.

* **Multi-stakeholder working** - each CoST national programme is managed by a stakeholder group including government, private sector and civil society.

* **Social accountability** - raising awareness of key issues arising from the assurance process, and engaging civil society and media to hold decision makers to account.

The 'Infrastructure Data Standard' is a **framework for disclosure** which has been adapted by a range of CoST national programmes, who have variously prioritized different elements based on their local needs, or who have included additional elements that they wish to monitor: particularly additional kinds of documentation that should be provided for each infrastructure project.

You can read more about the Infrastructure Data Standard in [CoST Guidance Note 6](http://infrastructuretransparency.org/resource/guidance-note-6-designing-a-disclosure-process/).

```eval_rst
.. admonition:: Frameworks and standards
    :class: Note

    .. markdown::

        There is an important distinction between the Infrastructure Data Standard (IDS) and the Open Contracting Data Standard (OCDS). IDS provides a framework to identify *categories of information* that should be disclosed. OCDS describes *specific fields* and how they should be structured as data.

        The [Open Contracting for Infrastructure Data Standard (OC4IDS)](../projects/index) documented on this site acts as a bridge between the IDS framework, and the idea of a more structured technical data standard.

```

<!-- Note - mappings come from https://docs.google.com/spreadsheets/d/1tpXKCrNY1vUEPo6O1j-GPhxgSna7CZ5uwz_eTNLEOr8/edit#gid=2054628701 -->

The following tables document two mappings:

* The **CoST IDS to OC4IDS** mapping describes how to represent each element of the CoST IDS as structured data using OC4IDS. Use this mapping if you already collect data according to the CoST IDS and you want to publish your data using OC4IDS, or if you want to make sure that your OC4IDS publication conforms to the CoST IDS.
* The **OCDS to OC4IDS** mapping describes how to use OCDS data to populate the sections of an OC4IDS file which relate to the CoST IDS. Use this mapping if you have access to OCDS data on infrastructure contracting processes and you want to create a summary by project in OC4IDS format, or if you want to check which CoST IDS elements your OCDS data covers.

The organization of the mapping tables reflects the structure of the CoST IDS, which is described in [Getting Started](../projects/index).

## CoST IDS to OC4IDS Mapping

### Project level

#### Identification

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/project-level-identification.csv
```

#### Preparation

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/project-level-preparation.csv
```

#### Project completion

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/project-level-completion.csv
```

### Process level

#### Procurement

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/process-level-procurement.csv
```

#### Implementation

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/process-level-implementation.csv
```

## OCDS to OC4IDS Mapping

### Guidance

#### Command-line tool and reference implementation

OCDS Kit's [convert-to-oc4ids](https://ocdskit.readthedocs.io/en/latest/cli/ocds.html#convert-to-oc4ids) command  is a command-line tool and reference implementation for converting OCDS data to OC4IDS format.

`convert-to-oc4ids` covers most mappings in the following categories:

* project-level identification
* project-level preparation
* process-level procurement

However, `convert-to-oc4ids` does not cover all mappings, nor does it perform currency conversions. Mappings which `convert-to-oc4ids` does not cover are shown in *italics*.

#### Mapping codelists

Mappings that depend the specific classifications or codelists used in the OCDS data are not documented in detail, as they may differ by publisher. For example, mapping to the OC4IDS projectSector codelist.

#### Alternative mappings

Some mappings offer optional alternatives in case the primary mapping isn't available. For example, for OCDS data in which `planning.project.title` isn't available, you can optionally set the project `title` based on the `tender.title`.

In order to provide analysts with additional context, alternative mappings may copy additional fields which don't appear in OC4IDS schema. You should remove these fields if you plan to publish your OC4IDS data.

#### OCDS extensions

Some mappings use fields from [OCDS extensions](https://standard.open-contracting.org/latest/en/guidance/map/extensions/#extensions). In these cases, the names of extensions are noted in parentheses; where possible, alternative mappings are provided that use only fields from the core OCDS schema.

#### Handling conflicts and duplicates

Implementations of the mapping should give consideration to:

* OCDS data that contains fields that differ between contracting processes but map to a single field in OC4IDS: for example, where `planning.project.title` differs for two contracting processes that relate to the same project, but OC4IDS has a single `title` field at the project level.
* OCDS data that contains multiple `Organization` objects with the same `.role` that map to a single field in OC4IDS: for example, where a contracting process has two `Organization`s with the 'procuringEntity' role, but OC4IDS has a single `.summary.tender.procuringEntity` field at the contract level.
* Checking for duplicates when copying objects from OCDS. For example, checking whether an `Organization` object has already been copied before copying it again.
* Handling identifier conflicts when copying objects from OCDS. For example, where two contracting processes both contain a ``Document`` with the same `.id`.

Read the `convert-to-oc4ids` [transformation notes](https://ocdskit.readthedocs.io/en/latest/cli/ocds.html#transformation-notes) to learn about how OCDS Kit handles the above scenarios.

#### Handling multiple currencies

Some mappings involve converting values in OCDS, which may be in different currencies, to a base currency.

Implementations which include multiple currencies should give consideration to [value dating](https://en.wikipedia.org/wiki/Value_date). One approach is to use the compiled release's `date`.

### Mapping

#### Project level

##### Identification

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/project-level-identification.csv
```

##### Preparation

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/project-level-preparation.csv
```

##### Project completion

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/project-level-completion.csv
```

#### Process level

The mappings in this section relate to the `contractingProcesses` section of the OC4IDS schema, unless otherwise specified.

##### Procurement

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/process-level-procurement.csv
```

##### Implementation

Disclosures in the implementation section of the CoST IDS relate to changes to a contract's value, duration or scope that were made after the contract was awarded.

If OCDS data is available, these changes can be determined by comparing the most recent OCDS release to a compiled release created from all prior releases (to better understand these concepts, refer to the [OCDS documentation](https://standard.open-contracting.org/1.1/en/getting_started/releases_and_records/)). The specific fields to monitor for changes between releases are described in the mapping table below.

In some cases, OCDS data may include an explanation of changes in the relevant `amendments` block. In other cases, the reason may need to be manually entered.

```eval_rst
.. csv-table-no-translate::
   :header-rows: 1
   :widths: 20 20 20 30
   :file: ../../build/current_lang/process-level-implementation.csv
```

### Reactive disclosures

The CoST IDS also sets out a number of data points under the heading of 'reactive disclosure'. It is possible to also disclose many of these fields **pro-actively** either as **document** entries with free text or linked documents, or using structured OCDS fields and extensions.

Specifically:

* Details of a individuals involved at the project or contract level can be included in the ``parties`` array with a suitable role. Role is an open codelist. As individuals will not have an 'organization identifier' a locally defined identifier may be used instead.

* Plans, reports and assessments may be included in the project or contracting process level `documents` blocks, or may be published within individual OCDS releases.

* The [budget_breakdown](https://github.com/open-contracting-extensions/ocds_budget_breakdown_extension) and [budget_and_spend](https://github.com/open-contracting-extensions/ocds_budget_and_spend_extension) extensions can be used to provide guidance on modelling detailed financial information.
