# OCDS to OC4IDS mapping

<style>
.wy-nav-content {
  max-width: 1200px;
}
</style>

This page provides guidance and documents a mapping from OCDS fields and codes to OC4IDS fields and codes. The organization of the mapping tables reflects the structure of the CoST IDS.

## Guidance

### Command-line tool and reference implementation

OC4IDS Kit's [convert-from-ocds](https://oc4idskit.readthedocs.io/en/latest/cli.html#convert-from-ocds) command is a command-line tool and reference implementation for converting OCDS data to OC4IDS format.

`convert-from-ocds` covers most mappings in the following categories:

* project-level identification
* project-level preparation
* process-level procurement

However, `convert-from-ocds` does not cover all mappings, nor does it perform currency conversions. Mappings that `convert-from-ocds` does not cover are shown in *italics*.

### Mapping codelists

Mappings that depend on the specific classification or codelist used in the OCDS data are not documented in detail, as they can differ by publisher. For example, mapping to the OC4IDS projectSector codelist.

### Alternative mappings

Some mappings offer alternatives in case the primary mapping isn't available. For example, for OCDS data in which `planning.project.title` isn't available, you can set the project `title` based on the `tender.title`.

In order to provide analysts with additional context, some alternative mappings copy additional fields which don't appear in OC4IDS schema. You ought to remove these fields if you plan to publish your OC4IDS data.

### OCDS extensions

Some mappings use fields from [OCDS extensions](https://standard.open-contracting.org/latest/en/guidance/map/extensions/#extensions). In these cases, the names of extensions are noted in parentheses; where possible, alternative mappings are provided that use only fields from the core OCDS schema.

### Handling conflicts and duplicates

Implementations of the mapping ought to give consideration to:

* OCDS data that contains fields that differ between contracting processes but map to a single field in OC4IDS: for example, where `planning.project.title` differs for two contracting processes that relate to the same project, but OC4IDS has a single `title` field at the project level.
* OCDS data that contains multiple `Organization` objects with the same `.role` that map to a single field in OC4IDS: for example, where a contracting process has two `Organization`s with the 'procuringEntity' role, but OC4IDS has a single `.summary.tender.procuringEntity` field at the contract level.
* Checking for duplicates when copying objects from OCDS. For example, checking whether an `Organization` object has already been copied before copying it again.
* Handling identifier conflicts when copying objects from OCDS. For example, where two contracting processes both contain a ``Document`` with the same `.id`.

Read the `convert-from-ocds` [transformation notes](https://oc4idskit.readthedocs.io/en/latest/cli.html#transformation-notes) to learn about how OC4IDS Kit handles the above scenarios.

### Handling multiple currencies

Some mappings involve converting values in OCDS, which can be in different currencies, to a base currency.

Implementations which include multiple currencies ought to give consideration to [value dating](https://en.wikipedia.org/wiki/Value_date). One approach is to use the compiled release's `date`.

## Mapping

### Project level

#### Identification

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/project-level-identification.csv
```

#### Preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/project-level-preparation.csv
```

#### Project completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/project-level-completion.csv
```

#### Reactive disclosures

##### Identification and preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-project-level-identification-preparation.csv
```

##### Completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-project-level-completion.csv
```

### Process level

The mappings in this section relate to the `contractingProcesses` section of the OC4IDS schema, unless otherwise specified.

#### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/process-level-procurement.csv
```

#### Implementation

Disclosures in the implementation section of the CoST IDS relate to changes to a contract's value, duration or scope that were made after the contract was awarded.

If OCDS data is available, these changes can be determined by comparing the most recent OCDS release to a compiled release created from all prior releases (to better understand these concepts, refer to the [OCDS documentation](https://standard.open-contracting.org/1.1/en/getting_started/releases_and_records/)). The specific fields to monitor for changes between releases are described in the mapping table below.

In some cases, OCDS data might include an explanation of changes in the relevant `amendments` block. In other cases, the reason might need to be manually entered.

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/process-level-implementation.csv
```

#### Reactive disclosures

##### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-process-level-procurement.csv
```

##### Contract

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-process-level-contract.csv
```

##### Implementation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,3
:file: ../../build/current_lang/reactive-process-level-implementation.csv
```
