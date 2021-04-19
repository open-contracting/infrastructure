# Using data from procurement systems for infrastructure monitoring

An increasing number of procurement portals now publish data using the Open Contracting Data Standard (OCDS). When OCDS is implemented in full, then:

* Each contracting process is given a unique identifier (`ocid`);

* Every update to that process, from planning through to implementation, should be published under the same `ocid`, and in a structured open data format;

* It should be possible to download bulk data in OCDS format, or access this structured data via an API.

Even when an OCDS publisher does not provide data for every stage of the contracting process, it is still possible to use OCDS data to:

* Discover contracts related to infrastructure projects;

* Track these contracting processes, including changes to tenders, details of suppliers selected, and, in some cases, details of contract modifications.

### Getting started

*The following steps may require support from a technical expert. You can also contact the OC4IDS Helpdesk ([data@open-contracting.org](mailto:data@open-contracting.org)) for guidance.*

#### (1) Evaluate the Open Contracting Data

Check that the data you plan to analyze is in OCDS format

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use the [OCDS Data Review Tool](https://standard.open-contracting.org/review/) to check whether your data is in the correct format

```

Check which stages of the contracting process the data covers.

Check whether the publisher keeps a change history (multiple releases for each contracting process), or whether as a user of the data you will need to keep the change history.

#### (2) Identify how you will query the data

Some OCDS publishers provide an API that can be used to query data. Others provide access to bulk data that you can download into your own tools for querying.

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      If you are working with OCDS data from an unreliable source, consider caching a copy of the OCDS releases that relate to the infrastructure projects you are monitoring, and consider linking to the copies from your OC4IDS data in order to ensure they are available to users.
```

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      [OCDS Kingfisher](https://github.com/open-contracting/kingfisher/) is an open source tool that can load OCDS data into a PostgreSQL database. It includes scrapers for many known OCDS data sources

```

#### (3) Develop a search strategy to discover infrastructure projects

Ideally, the procurement data source will include some sort of project or budget identifier fields that relate to a register of infrastructure projects.

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      If the procurement data you are working with is in OCDS format, refer to the guidance on [project identifiers in OCDS](identifiers) for more information on where to find identifiers for projects.

```

However, where this is not the case, it may be possible to search for tenders with a particular set of item classifications, or from a particular buyer.

This may be possible by downloading and filtering spreadsheets of the data, or may require queries written against your chosen data storage tool.

```eval_rst
.. admonition:: Worked example
    :class: Tip

    .. markdown::

      Using the UK Contracts Finder dataset in OCDS format, and [OCDS Kingfisher](https://github.com/open-contracting/kingfisher/), we can use the following query to fetch contracting processes classified under the ['Architectural, construction, engineering and inspection services'](http://cpv.data.ac.uk/code-71000000.html) hierarchy of the EU Common Procurement Vocabulary.

      ```sql
      /* The following query runs against a filtered set of data in Kingfisher */
      SELECT
          data,
              /* The 'data' field contains the JSON representation of a contracting process. The data -> 'object' ->> 'value' syntax
                 is used to navigate this structure and select values.

                 data -> 'tender' -> 'tenderPeriod' ->> 'endDate' for example is analogous to the json path tender/tenderPeriod/endDate
              */
          data->'buyer'->>'name' as buyer,
          data->'tender'->'tenderPeriod'->>'endDate' as tenderEndDate,
          EXTRACT(YEAR from cast(data->'tender'->'tenderPeriod'->>'endDate' as timestamp)) as tenderYear,
          data->'tender'->>'title' as title,
          data->'tender'->'value'->>'currency' as currency,
          data->'tender'->'value'->>'amount' as value

              /* We use a sub-query in order to select only contracting processes where there is at least one tender/item with a particular classification */
      FROM (
          SELECT DISTINCT data from data
              /* In Kingfisher, OCDS data is sorted as 'json blobs' (jsonb). The next line expands the items array into a table we can join against */
          LEFT JOIN LATERAL jsonb_array_elements(data->'tender'->'items') items on TRUE
              /* All 'Architectural, construction, engineering and inspection services' have CPV codes starting with 71 */
          WHERE items->'classification'->>'id' LIKE '71%'  
       ) data

          /* We sort by value (highest first). We cast values from the JSON before sorting. */
      ORDER BY cast(data -> 'tender' -> 'value' ->> 'amount' as float) DESC
      ```

      This returns over 11,000 procurement processes related to infrastructure, covering frameworks and procurements, with a value of up to £25bn a year. These processes include design work, construction and monitoring, and each needs to be reviewed to identify if it should be subject to monitoring.

```

#### (4) Populate project-level data

If your analysis of OCDS data reveals infrastructure projects to monitor, you can:

* Use the information from a contracting process data to start populating a **project-level disclosure**;

* Search for **related contracts** in order to link any other design, construction or monitoring contracts to this project;

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      When searching for related contracts, you may be looking for contracts from the same buyer, mentioning similar words or localities.

```

You may not be able to fill all the project-level details from the contracts, and may need to undertake additional research to find:

* The project owner and name
* The full scope of the project
* The total project budget and cost estimates
* Any environmental impact or land and settlement impact studies that have been undertaken

```eval_rst
.. admonition:: Tip
    :class: Tip

    .. markdown::

      You can use a [blank example OC4IDS JSON file](../../_static/blank.json) to get started.

```

#### (5) Monitoring contracting process updates

When a publisher is using OCDS correctly, and is providing updates on a contracting process under the same `ocid`, you should be able to regularly fetch the latest data for each contracting process you are monitoring, and to compare it with the existing data you have, looking for changes.

Keep a copy each time the data changes, and if you see modifications to:

* Price
* Duration
* Scope

check whether an adequate explanation has been given for these.

You can use OC4IDS to record each time a change is detected, and the reasons that are given for the change.

#### (6) Add project completion data

When there is evidence that a project has reached completion, it is important to further update the **project-level disclosure**.

If the OCDS data includes implementation data, including transactions or final spending information, then it may be possible to compare the total sum of all contract spending against the original anticipated contract spend, and overall project budget. It may also be possible to compare final contract delivery dates with originally planned dates. This can be used to identify possible modifications that are in need to explanation.

In other cases, you may need to identify other data sources (such as treasury or public spending data) that you can draw upon to check whether a project spend was as anticipated or not.

### Tools and platform

You can use OCDS data as part of a manual monitoring process, or you can integrate OCDS into a comprehensive transparency portal.

Tools to help you with manual monitoring include:

* [OCDS Kingfisher](https://github.com/open-contracting/kingfisher/) - a framework for regularly fetching, storing and querying OCDS data.
* [OCDS Merge](https://github.com/open-contracting/ocds-merge) - a library to combine multiple releases of OCDS data into a summary (compiledRelease), and to identify changes over time (versionedRelease).
* [OCDS Show](https://github.com/open-contracting/ocds-show) - a flexible framework for presenting templated views of OCDS data. Given a merged OCDS record, OCDS Show can highlight change over time.

When building an integrated tool that integrates OCDS data into infrastructure project monitoring:

* The [OC4IDS](../../projects/index) provides a common data structure for recording project-level information;

* The [CoST IDS and OCDS Mapping](../../cost/index) provides guidance on how to use OCDS data to populate project-level and contracting process summary data.
