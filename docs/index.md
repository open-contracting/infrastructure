# Open Contracting for Infrastructure

The Open Contracting Data Standard is already used to describe millions of procurement processes around the world relating to goods, services and public works. 

This site describes how to combine **contract level disclosures using OCDS** with **project level disclosure**, in order to support scalable monitoring of infrastructure project design, delivery and impact. 

Trillions of dollars are spent every year on infrastructure, and estimates suggest between 10 and 30% of infrastructure investment is lost through inefficiency, mismanagement and corruption. Access to better and more joined up data is essential to drive better quality, more affordable infrastructure for government, citizens and business.

This Open Contracting for Infrastructure site will show you how to:

* Publish standardised contracting data for major infrastructure projects using the **open contracting data standard (OCDS)**;

* Extract infrastructure contracting data from existing procurement portals;

* Connect contract and project level information using the [project level schema](project/index.md).

* Assess published data against the [CoST Infrastructure Data Standard](project/mapping.md);

* Make use of data in infrastructure monitoring.




## Contents

```eval_rst
.. toctree::
   :maxdepth: 2
   :glob:


   projects/index
   projects/schema
   projects/reference
   cost/mapping
```


## Why we need open contracting for infrastructure? 



## I want to... use open contracting data to understand infrastructure projects

An increasing number of procurement portals now publish data using the Open Contracting Data Standard (OCDS). When OCDS is implemented in full, then:

* Each contracting process is given a unique identifier (`ocid`);

* Every update to that process, from planning through to implementation, should be published under the same `ocid`, and in a structured open data format;

* It should be possible to download bulk data in OCDS format, or access this structured data via an API. 

Even when an OCDS publisher does not provide data for every stage of the contracting process, it is still possible to use OCDS data to:

* Discover contracts related to infrastructure projects;

* Track these contracting processes, including changes to tenders, details of suppliers selected, and, in some cases, details of contract variations. 

### Getting started

*The following steps may require support from a technical expert. You can also contact the OCDS Helpdesk ([data@open-contracting.org](mailto:data@open-contracting.org)) for guidance.*

#### (1) Evaluate the Open Contracting Data

Check that the data you plan to analyse is in OCDS format (Tip: you can use the [data validator/review tool](http://standard.open-contacting.org/validator) for this). 

Check which stages of the contracting process the data covers.

Check whether the publisher keeps a change history (multiple releases for each contracting process), or whether as a user of the data you will need to keep the change history. 

#### (2) Identify how you will query the data

Some OCDS publishers provide an API that can be used to query data. Others provide access to bulk data that you can download into your own tools for querying.

Tip: [OCDS Kingfisher](https://github.com/open-contracting/kingfisher/) is an open source tool that can load OCDS data into a PostGres database. It includes scrapers for many known OCDS data sources.

#### (3) Develop a search strategy to discover infrastructure projects

Ideally, the procurement data source will include some sort of project or budget identifier fields that relate to a register of infrastructure projects. 

However, where this is not the case, it may be possible to search for tenders with a particular set of item classifications, or from a particular buyer.

This may be possible by downloading and filtering spreadsheets of the data, or may require queries written against your chosen data storage tool. 

For example, using the UK Contracts Finder dataset in OCDS format, and [OCDS Kingfisher](https://github.com/open-contracting/kingfisher/), we can use the following query to fetch contracting processes classified under the ['Architectural, construction, engineering and inspection services'](http://cpv.data.ac.uk/code-71000000.html) hierarchy of the EU Common Procurement Vocabulary. 

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

        /* We us a sub-query in order to select only contracting processes where there is at least one tender/item with a particular classification */
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

#### (4) Populate project level data

If your analysis of OCDS data reveals infrastructure projects to monitor, you can:

* Use the information from a contracting process data to start populating a **project level disclosure**;

(TODO: READ MORE HERE ABOUT POPULATING PROJECT LEVEL DATA SCHEMA FROM OCDS RELEASES)

* Search for **related contracts** in order to link any other design, construction or monitoring contracts to this project;

Tip: When searching for related contracts, you may be looking for contracts from the same buyer, mentioning similar words or localities. 

You may not be able to fill all the project-level details from the contracts, and may need to undertake additional research to find:

* The project owner and name
* The full scope of the project
* The total project budget and cost estimates
* Any environmental impact or land and settlement impact studies that have been undertaken

#### (5) Monitoring contracting process updates

When a publisher is using OCDS correctly, and is providing updates on a contracting process under the same `ocid`, you should be able to regularly fetch the latest data for each contracting process you are monitoring, and to compare it with the existing data you have, looking for changes.

Keep a copy each time the data changes, and if you see variations to:

* Price
* Duration
* Scope

check whether an adequate explanation has been given for these.

You can use the Project Level Data Specification to record each time a change is detected, and the reasons that are given for the change. 

#### (6) Add project completion data

When there is evidence that a project has reached completion, it is important to further update the **project level disclosure**. 

If the OCDS data includes implementation data, including transactions or final spending information, then it may be possible to compare the total sum of all contract spending against the original anticipated contract spend, and overall project budget. It may also be possible to compare final contract delivery dates with originally planned dates. This can be used to identify possible variations that are in need to explanation. 

In other cases, you may need to identify other data sources (such as treasury or public spending data) that you can draw upon to check whether a project spend was as anticipated or not. 

### Tools and platform

You can use OCDS data as part of a manual monitoring process, or you can integrate OCDS into a comprehensive transparency portal. 

Tools to help you with manual monitoring include:

* [OCDS Kingfisher](https://github.com/open-contracting/kingfisher/) - a framework for regularly fetching, storing and querying OCDS data.
* [OCDS Merge](https://github.com/open-contracting/ocds-merge) - a library to combine multiple releases of OCDS data into a summary (compiledRelease), and to identify changes over time (versionedReleased).
* [OCDS Show](https://github.com/open-contracting/ocds-show) - a flexible framework for presenting templated views of OCDS data. Given a merged OCDS record, OCDS Show can highlight change over time. 

When building an integrated tool that integrates OCDS data into infrastructure project monitoring:

* The [Project Level Data Specification](project/index) provides a common data structure for recording project-level information;

* The [Open Contracting for Infrastructure - CoST Mapping](cost/mapping) provides guidance on how to use OCDS data to populate project level, and project:contracting data. 

(TODO UPDATE MAPPING LINK ABOVE)


## I want to... publish open data about infrastructure projects




## I want to... assess my data against the CoST Infrastructure Data Standard



