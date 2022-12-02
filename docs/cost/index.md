# CoST IDS & OCDS Mapping

<style>
.wy-nav-content {
  max-width: 1200px;
}
</style>

CoST – the Infrastructure Transparency Initiative (CoST) is the leading global initiative improving transparency and accountability in public infrastructure.

The [CoST approach](http://infrastructuretransparency.org/our-approach/) is based on four core features:

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

The following tables document two mappings:

* The [**CoST IDS to OC4IDS**](#cost-ids-to-oc4ids-mapping) mapping describes how to represent each element of the CoST IDS as structured data using OC4IDS. Use this mapping if you already collect data according to the CoST IDS and you want to publish your data using OC4IDS, or if you want to make sure that your OC4IDS publication conforms to the CoST IDS.
* The [**OCDS to OC4IDS**](#ocds-to-oc4ids-mapping) mapping describes how to use OCDS data to populate the sections of an OC4IDS file which relate to the CoST IDS. Use this mapping if you have access to OCDS data on infrastructure contracting processes and you want to create a summary by project in OC4IDS format, or if you want to check which CoST IDS elements your OCDS data covers.

The organization of the mapping tables reflects the structure of the CoST IDS, which is described in [Getting Started](../projects/index).

The mapping tables use `/` notation to reference fields in OCDS data, e.g. `/tender/status`, and `.` notation to reference fields in the OC4IDS schema, e.g. `.budget.approvalDate`.

The CoST IDS also sets out a number of disclosure requirements under the heading of 'information for disclosure upon request', also known as 'reactive disclosure'. You can disclose these elements proactively using OC4IDS. Separate tables are provided for reactive disclosures in each mapping.

## Common operations

To avoid repetition in the mapping, we refer and link to the following common operations.

### Add a project document

Add a `Document` object to the `documents` array and set its fields as follows:

* Set its `.id` incrementally
* Set its `.url` to a direct link to the document
* Set its `.title` to the title of the document

### Add a contracting process document

Add a `Document` object to the `contractingProcesses.summary.documents` array and set its fields as follows:

* Set its `.id` incrementally
* Set its `.url` to a direct link to the document
* Set its `.title` to the title of the document

## CoST IDS to OC4IDS Mapping

### Project level

#### Identification

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/project-level-identification.csv
```

#### Preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/project-level-preparation.csv
```

#### Project completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/project-level-completion.csv
```

#### Reactive disclosures

##### Identification and preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/reactive-project-level-identification-preparation.csv
```

##### Completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/reactive-project-level-completion.csv
```

###### Implementation progress reports

In addition to the documents listed in the mapping table, you can use OC4IDS to publish structured data on planned and actual physical and financial progress.

Choose from the following options, depending on the data you collect and the data needed by your use cases.

**Actual progress over time**

* Add a `Metric` object to the `metrics` array and:
  * For financial progress, set its `id` to 'financialProgress' and set its title to 'Financial progress', or the equivalent in the language of your publication.
  * For physical progress, set its `id` to 'physicalProgress' and set its title to 'Physical progress', or the equivalent in the language of your publication.
* For each progress update, add an `Observation` object to the `Metric` object's `.observations` array and:
  * Set its `.id` incrementally
  * Set its `.measure` to the financial progress of the project. For example, for a project that is 75% complete, set `.measure` to `75`
  * Set its `.unit.name` to 'percent', set its `unit.id` to 'P1' and set its `unit.scheme` to 'UNCEFACT'
  * Set its `period.startDate` and `period.endDate` to the date on which the financial progress was measured

*Example:*

```json
{
  "metrics": [
    {
      "id": "physicalProgress",
      "title": "Physical progress",
      "observations": [
        {
          "id": "1",
          "measure": "4.04",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-03-31T23:59:59Z",
            "endDate": "2017-03-31T23:59:59Z"
          }
        },
        {
          "id": "2",
          "measure": "7.98",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-04-30T23:59:59Z",
            "endDate": "2017-04-30T23:59:59Z"
          }
        },
        {
          "id": "3",
          "measure": "8.38",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-05-31T23:59:59Z",
            "endDate": "2017-05-31T23:59:59Z"
          }
        }
      ]
    }
  ]
}
```

**A single progress figure**

If your implementation does not store a change history, you can publish a single `Observation` object for each `Metric` and update the `Observation` object's `.measure` each time there is a progress update.

*Example:*

```json
{
  "metrics": [
    {
      "id": "financialProgress",
      "title": "Financial progress",
      "observations": [
        {
          "id": "1",
          "measure": "4.04",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-03-31T23:59:59Z",
            "endDate": "2017-03-31T23:59:59Z"
          }
        }
      ]
    }
  ]
}
```

**Planned progress over time**

You can use the `forecasts` array to publish progress forecasts for different points in time.

* Add a `Metric` object to the `forecasts` array and:
  * For financial progress, set its `id` to 'financialProgress' and set its title to 'Financial progress', or the equivalent in the language of your publication.
  * For physical progress, set its `id` to 'physicalProgress' and set its title to 'Physical progress', or the equivalent in the language of your publication.
* For each forecast, add an `Observation` object to the `Metric` object's `.observations` array and:
  * Set its `.id` incrementally
  * Set its `.measure` to the forecast progress of the project. For example, to forecast when the project is expected to be complete, set `.measure` to `100`.
  * Set its `.unit.name` to 'percent', set its `unit.id` to 'P1' and set its `unit.scheme` to 'UNCEFACT'
  * Set its `period.startDate` and `period.endDate` to the date on which you expect the progress to be achieved

*Example:*

```json
{
  "forecasts": [
    {
      "id": "physicalProgress",
      "title": "Physical progress",
      "observations": [
        {
          "id": "1",
          "measure": "4.04",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-03-31T23:59:59Z",
            "endDate": "2017-03-31T23:59:59Z"
          }
        },
        {
          "id": "2",
          "measure": "7.98",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-04-30T23:59:59Z",
            "endDate": "2017-04-30T23:59:59Z"
          }
        },
        {
          "id": "3",
          "measure": "8.38",
          "unit": {
            "name": "percent",
            "id": "P1",
            "scheme": "UNCEFACT"
          },
          "period": {
            "startDate": "2017-05-31T23:59:59Z",
            "endDate": "2017-05-31T23:59:59Z"
          }
        }
      ]
    }
  ]
}
```

### Process level

The mappings in this section relate to the `contractingProcesses` section of the OC4IDS schema, unless otherwise specified.

#### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/process-level-procurement.csv
```

#### Implementation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/process-level-implementation.csv
```

#### Reactive disclosures

##### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/reactive-process-level-procurement.csv
```

##### Contract

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/reactive-process-level-contract.csv
```

##### Implementation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../build/current_lang/reactive-process-level-implementation.csv
```

## OCDS to OC4IDS Mapping

### Guidance

#### Command-line tool and reference implementation

OC4IDS Kit's [convert-from-ocds](https://oc4idskit.readthedocs.io/en/latest/cli.html#convert-from-ocds) command is a command-line tool and reference implementation for converting OCDS data to OC4IDS format.

`convert-from-ocds` covers most mappings in the following categories:

* project-level identification
* project-level preparation
* process-level procurement

However, `convert-from-ocds` does not cover all mappings, nor does it perform currency conversions. Mappings that `convert-from-ocds` does not cover are shown in *italics*.

#### Mapping codelists

Mappings that depend on the specific classification or codelist used in the OCDS data are not documented in detail, as they can differ by publisher. For example, mapping to the OC4IDS projectSector codelist.

#### Alternative mappings

Some mappings offer alternatives in case the primary mapping isn't available. For example, for OCDS data in which `planning.project.title` isn't available, you can set the project `title` based on the `tender.title`.

In order to provide analysts with additional context, some alternative mappings copy additional fields which don't appear in OC4IDS schema. You ought to remove these fields if you plan to publish your OC4IDS data.

#### OCDS extensions

Some mappings use fields from [OCDS extensions](https://standard.open-contracting.org/latest/en/guidance/map/extensions/#extensions). In these cases, the names of extensions are noted in parentheses; where possible, alternative mappings are provided that use only fields from the core OCDS schema.

#### Handling conflicts and duplicates

Implementations of the mapping ought to give consideration to:

* OCDS data that contains fields that differ between contracting processes but map to a single field in OC4IDS: for example, where `planning.project.title` differs for two contracting processes that relate to the same project, but OC4IDS has a single `title` field at the project level.
* OCDS data that contains multiple `Organization` objects with the same `.role` that map to a single field in OC4IDS: for example, where a contracting process has two `Organization`s with the 'procuringEntity' role, but OC4IDS has a single `.summary.tender.procuringEntity` field at the contract level.
* Checking for duplicates when copying objects from OCDS. For example, checking whether an `Organization` object has already been copied before copying it again.
* Handling identifier conflicts when copying objects from OCDS. For example, where two contracting processes both contain a ``Document`` with the same `.id`.

Read the `convert-from-ocds` [transformation notes](https://oc4idskit.readthedocs.io/en/latest/cli.html#transformation-notes) to learn about how OC4IDS Kit handles the above scenarios.

#### Handling multiple currencies

Some mappings involve converting values in OCDS, which can be in different currencies, to a base currency.

Implementations which include multiple currencies ought to give consideration to [value dating](https://en.wikipedia.org/wiki/Value_date). One approach is to use the compiled release's `date`.

### Mapping

#### Project level

##### Identification

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/project-level-identification.csv
```

##### Preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/project-level-preparation.csv
```

##### Project completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/project-level-completion.csv
```

##### Reactive disclosures

###### Identification and preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-project-level-identification-preparation.csv
```

###### Completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-project-level-completion.csv
```

#### Process level

The mappings in this section relate to the `contractingProcesses` section of the OC4IDS schema, unless otherwise specified.

##### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/process-level-procurement.csv
```

##### Implementation

Disclosures in the implementation section of the CoST IDS relate to changes to a contract's value, duration or scope that were made after the contract was awarded.

If OCDS data is available, these changes can be determined by comparing the most recent OCDS release to a compiled release created from all prior releases (to better understand these concepts, refer to the [OCDS documentation](https://standard.open-contracting.org/1.1/en/getting_started/releases_and_records/)). The specific fields to monitor for changes between releases are described in the mapping table below.

In some cases, OCDS data might include an explanation of changes in the relevant `amendments` block. In other cases, the reason might need to be manually entered.

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/process-level-implementation.csv
```

##### Reactive disclosures

###### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-process-level-procurement.csv
```

###### Contract

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-process-level-contract.csv
```

###### Implementation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-process-level-implementation.csv
```
