# Core standard

<style>
.wy-nav-content {
  max-width: 1200px;
}
</style>

## Project level

### Identification

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/project-level-identification.csv
```

### Preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/project-level-preparation.csv
```

### Project completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/project-level-completion.csv
```

### Reactive disclosures

#### Identification and preparation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/reactive-project-level-identification-preparation.csv
```

#### Completion

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/reactive-project-level-completion.csv
```

#### Implementation progress reports

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

## Process level

The mappings in this section relate to the `contractingProcesses` section of the OC4IDS schema, unless otherwise specified.

### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/process-level-procurement.csv
```

### Implementation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/process-level-implementation.csv
```

### Reactive disclosures

#### Procurement

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/reactive-process-level-procurement.csv
```

#### Contract

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/reactive-process-level-contract.csv
```

#### Implementation

```{csv-table-no-translate}
:header-rows: 1
:included_cols: 0,1,2
:file: ../../../build/current_lang/reactive-process-level-implementation.csv
```
