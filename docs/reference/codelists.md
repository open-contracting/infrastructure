# Codelist reference

Some schema fields refer to codelists, to limit and standardize the possible values of the fields, in order to promote data interoperability.

Codelists are either be open or closed. **Closed codelists** are intended to be comprehensive; for example, the currency codelist covers all currencies in the world. **Open codelists** are intended to be representative, but not comprehensive.

Publishers must use the codes in the codelists, unless no code is appropriate. If no code is appropriate and the codelist is **open**, then a publisher may use a new code outside those in the codelist. If no code is appropriate and the codelist is **closed**, then a publisher should instead create an issue in the [OC4IDS GitHub repository](https://github.com/open-contracting/infrastructure/issues).

```{admonition} Extending open codelists
:class: Tip

If you use new codes outside those in an open codelist, please create an issue in the [OC4IDS GitHub repository](https://github.com/open-contracting/infrastructure/issues), so that the codes can be considered for inclusion in the codelist.
```

For more information on open and closed codelists, refer to the Open Contracting Data Standard [codelists documentation](https://standard.open-contracting.org/1.1/en/schema/codelists/).

## OCDS codelists

OC4IDS reuses some codelists from the Open Contracting Data Standard and its extensions:

* [Currency](https://standard.open-contracting.org/1.1/en/schema/codelists/#currency)
* [Geometry type](https://extensions.open-contracting.org/en/extensions/location/master/codelists/#geometryType.csv)
* [Location gazetteers](https://extensions.open-contracting.org/en/extensions/location/master/codelists/#locationGazetteers.csv)
* [Method](https://standard.open-contracting.org/1.1/en/schema/codelists/#method)
* [Organization identifier scheme](https://standard.open-contracting.org/1.1/en/schema/codelists/#organization-identifier-scheme)
* [Release tag](https://standard.open-contracting.org/1.1/en/schema/codelists/#release-tag)
* [Unit classification scheme](https://standard.open-contracting.org/1.1/en/schema/codelists/#unit-classification-scheme)
* [Milestone status](https://standard.open-contracting.org/1.1/en/schema/codelists/#milestone-status)
* [Milestone code](https://standard.open-contracting.org/profiles/ppp/latest/en/reference/codelists/#milestonecode)

## Closed codelists

### ContractingProcessStatus

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/contractingProcessStatus.csv
```

### ContractNature

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/contractNature.csv
```

### ProjectStatus

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/projectStatus.csv
```

Projects with a `status` of 'completed' may be displayed in a list of archived projects.

### ProjectType

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/projectType.csv
```

### MilestoneType

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/milestoneType.csv
```

### EnvironmentalGoal

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/environmentalGoal.csv
```

### country

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/country.csv
```

## Open codelists

### DocumentType

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/documentType.csv
```

### ModificationType

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/modificationType.csv
```

### PartyRole

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/partyRole.csv
```

### ProjectSector

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/projectSector.csv
```

### RelatedProject

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/relatedProject.csv
```

### RelatedProjectScheme

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/relatedProjectScheme.csv
```

### classificationScheme

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/classificationScheme.csv
```

### CostCategory

```{csv-table-no-translate}
:header-rows: 1
:file: ../../build/current_lang/codelists/costCategory.csv
```
