# Sustainability modules

<style>
.wy-nav-content {
  max-width: 1200px;
}

@media print
{
.sd-row {page-break-after:always}
}
</style>

This page documents a mapping from the elements in the CoST IDS sustainability modules to OC4IDS fields and codes.

```{admonition} Download this page in PDF format
:class: tip

 In Google Chrome, Microsoft Edge or Mozilla Firefox, open the **Print** dialog (Ctrl+P) and set **Destination** (**Printer**, in Microsoft Edge) to 'Save to PDF'. In Safari, open the **File** menu and click **Export as PDF**.

```

## Economic and fiscal


(Economic and fiscal-Procurement strategy)=

`````{grid} 2

````{grid-item-card} Procurement strategy
:columns: 4
CoST IDS element
^^^
Disclose the procurement strategy risk assessment. This tends to be part of the decision-making strategy and likely includes discussions regarding capabilities, the delivery model and the rationale for the risk allocation decision. (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
**Project Level:** [Add a project document](../common.md#add-a-project-document) and set `.documentType` to 'procurementStrategyRiskAssessment'.
```json
{
  "documents": [
    {
      "id": "1",
      "title": "Procurement strategy risk assessment",
      "documentType": "procurementStrategyRiskAssessment",
      "url": "http://example.com/documents/procurementStrategyRiskAssessment.pdf"
    }
  ]
}
```
````

`````


(Economic and fiscal-Life cycle cost)=

`````{grid} 2

````{grid-item-card} Life cycle cost
:columns: 4
CoST IDS element
^^^
Disclose the life cycle cost of the project, which is the cost of an asset throughout its life cycle while fulfilling the performance requirements (ISO 15686-5:2017) (E.g. \[value\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
**Project Level:** Add a `CostMeasurement` object to the `costMeasurements` array. Set `.date` to the date the analysis was prepared. If the cost measurement was performed as part of the project appraisal, set `.stage` to 'preConstruction'. Otherwise, choose an appropriate code from the stage codelist. Map to the cost measurement's `.lifeCycleCost.cost`.
```json
{
  "costMeasurements": [
    {
      "id": "1",
      "stage": "preConstruction",
      "date": "2014-05-01T00:00:00Z",
      "lifeCycleCost": {
        "cost": {
          "amount": 10000000,
          "currency": "usd"
        }
      }
    }
  ]
}
```
````

`````


(Economic and fiscal-Life cycle cost calculation methodology)=

`````{grid} 2

````{grid-item-card} Life cycle cost calculation methodology
:columns: 4
CoST IDS element
^^^
Disclose the methodology used to calculate the life-cycle cost. The methodology ought to specify whether income and externalities are included in the calculation and the common date, discount rate and period of analysis used.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
**Project Level:** Publish in documents, with `.documentType` set to 'lifecycleCostCalculationMethodology' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "lifecycleCostCalculationMethodology",
      "url": "http://example.com/documents/lifecycleCostCalculationMethodology.pdf"
    }
  ]
}
```
````

`````


(Economic and fiscal-Funding source for preparation, implementation and operation)=

`````{grid} 2

````{grid-item-card} Funding source for preparation, implementation and operation
:columns: 4
CoST IDS element
^^^
Name the funding organization(s)/sources of funding for Preparation, Implementation and Operation. If the information is not available for any of the stages, select \['funding/budget source not specified'\] for the respective stage where the nature of the funding/budget source could not be identified.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Economic and fiscal-Budget for preparation, implementation and operation)=

`````{grid} 2

````{grid-item-card} Budget for preparation, implementation and operation
:columns: 4
CoST IDS element
^^^
Specify the allocated budget for preparation, implementation, operation. If no amount is allocated for each of the stages, select the option 'amount not allocated" (E.g. Preparation \[currency and amount\], Implementation\[currency and amount\], Operation \[currency and amount\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Economic and fiscal-Cost benefit analysis)=

`````{grid} 2

````{grid-item-card} Cost benefit analysis
:columns: 4
CoST IDS element
^^^
Disclose the project cost-benefit analysis. This information tends to be part of the appraisal documents. (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
**Project Level:** Publish in `documents`, with `.documentType` set to 'costBenefitAnalysis' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "costBenefitAnalysis",
      "url": "http://example.com/documents/costBenefitAnalysis .pdf"
    }
  ]
}
```
````

`````


(Economic and fiscal-Value for money)=

`````{grid} 2

````{grid-item-card} Value for money
:columns: 4
CoST IDS element
^^^
A summary of the value for money analysis carried out for the project, along with supporting figures, calculations and business case, based on projected or actual procurement outcomes. This tends to include considerations of economy, efficiency, effectiveness and equity, and is part of the appraisal documents. (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Publish in `documents`, with `.documentType` set to 'valueForMoneyAnalysis' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "valueForMoneyAnalysis",
      "url": "http://example.com/documents/valueForMoneyAnalysis.pdf"
    }
  ]
}
```
````

`````


(Economic and fiscal-Budget projections)=

`````{grid} 2

````{grid-item-card} Budget projections
:columns: 4
CoST IDS element
^^^
In case of multiyear project implementation, disclose information on budget projection for all years of implementation (E.g. Y1: \[currency and amount\], Y2: \[currency and amount\], etc).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Economic and fiscal-Budget shortfall)=

`````{grid} 2

````{grid-item-card} Budget shortfall
:columns: 4
CoST IDS element
^^^
Disclose any shortfall in the allocated budget (E.g. \[currency and amount\] and \[free text: reasons for the funding shortfall\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Add a `Metric` object to the `.metrics` array, set its `.id` incrementally and set its `.title` to "Budget shortfall". Add an `Observation` object to the metric's `.observations` array and set

- `.id` incrementally
- `.value` to the value of the shortfall
- `.notes` to the reasons for the shortfall
- optionally, `.period` to the period to which the shortfall applies
```json
{
  "metrics": [
    {
      "id": "1",
      "title": "Budget shortfall",
      "observations": [
        {
          "id": "1",
          "period": {
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "202-12-31T00:00:00Z"
          },
          "value": {
            "amount": 2500000,
            "currency": "USD"
          },
          "notes": "Funding shortfall due to construction overruns and a lack of budgetary approval"
        }
      ]
    }
  ]
}
```
````

`````

## Environment and climate


(Environment and climate-Environmental impact category)=

`````{grid} 2

````{grid-item-card} Environmental impact category
:columns: 4
CoST IDS element
^^^
Indicate the category that reflects the magnitude of environmental impact. Consider the following to rate the project:

- Category A: projects with potential significant adverse environmental or social risks and/or impacts that are diverse, irreversible, or unprecedented.

- Category B: projects with potential limited adverse environmental or social risks and/or impacts that are few in number, generally site-specific, largely reversible, and readily addressed through mitigation measures.

- Category C: projects with minimal or no adverse environmental or social risks and/or impacts.

(Select from a list: A/B/C - Specify list as IFC's Environmental and Social Categorization).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

1. If an environmental impact assessment was conducted, set `.environment.hasImpactAssessment` to true. If an environmental impact assessment was not conducted, set `environmental.hasImpactAssessment` to false.

2. Add a `Classification` object to the `.environment.impactClassifications` array, set its `.scheme` to "ifc-environmental-social" and set its `.id` to the letter for the category into which the project falls.
```json
{
  "environment": {
    "hasImpactAssessment": true,
    "impactClassifications": [
      {
        "scheme": "ifc-environmental-social",
        "id": "a"
      }
    ]
  }
}
```
````

`````


(Environment and climate-Environmental measures)=

`````{grid} 2

````{grid-item-card} Environmental measures
:columns: 4
CoST IDS element
^^^
Disclose the measures adopted by the project to mitigate and/or remedy the environmental impact (E.g. \[free text justification/explaining the measures adopted\] and document).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Add a document, set its `.documentType` to 'environmentalMeasures', add a description of the environmental measures adopted to its `.description` and set  `.url` to the URL of the document that describes the project's environmental measures (if available).
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "environmentalMeasures",
      "description": "The following environmental measures are adopted by the project...",
      "url": "http://example.com/documents/environmentalMeasures.pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Environmental exceptions)=

`````{grid} 2

````{grid-item-card} Environmental exceptions
:columns: 4
CoST IDS element
^^^
Disclose all exemptions and/or amnesties obtained for the project. (E.g. \[Document\]). This can be planning, environmental, construction and/or operational related.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Publish in `documents`, with `.documentType` set to 'environmentalExemption' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "environmentalExemption",
      "url": "http://example.com/documents/environmentalExemption.pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Protected area)=

`````{grid} 2

````{grid-item-card} Protected area
:columns: 4
CoST IDS element
^^^
Identify whether the project is located in a protected area. Use the project location/coordinates at the WDPA - World Database of Protected Areas to disclose the information.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

If the project is located in a protected area:

1. Set `.environment.protectedArea` to true.
2. Add a `Location` object to the `.locations` array, set its `.id` incrementally and set its `.gazetteer.scheme` to 'WDPA_ID'
3. For each protected area in which the project is located, add the area's WDPA_ID to the `.gazetteer.identifiers` array.

If the project is not located in a protected area, set `.environment.protectedArea` to false.
```json
{
  "environment": {
    "protectedArea": true
  },
  "locations": [
    {
      "id": "1",
      "gazetteer": {
        "scheme": "WDPA_ID",
        "identifiers": [
          "555566673"
        ]
      }
    }
  ]
}
```
````

`````


(Environment and climate-Conservation measures)=

`````{grid} 2

````{grid-item-card} Conservation measures
:columns: 4
CoST IDS element
^^^
Disclose and provide further details on the measures adopted by the project to protect and enhance biodiversity. This can comprise, without limitation the following:

avoidance of ecological sitting
buffers for ecological land
nature-based solutions
land restoration
protection to landscape and historical sites
invasive species management
management of wildlife mortality risk
reduce habitat loss
pollution reduction
soil management
hazardous material management\])
others (explain)
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each measure add a `ConservationMeasure` object to the `environment.conservationMeasures` array, setting its `.type` according to the matching code in the open "conservationMeasuresType" codelist and mapping the further explanation to its `.description`.

If there is an accompanying document publish in `documents`, with `.documentType` set to 'conservationMeasures' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "environment": {
    "conservationMeasures": [
      {
        "type": "landRestoration",
        "description": "Land restoration measures for the project include..."
      }
    ]
  },
  "documents": [
    {
      "id": "1",
      "documentType": "conservationMeasures",
      "url": "http://example.com/conservationMeasures.pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Climate and disaster risk assessment)=

`````{grid} 2

````{grid-item-card} Climate and disaster risk assessment
:columns: 4
CoST IDS element
^^^
Clarify the type of climate and disaster risks to which the project is exposed to (E.g. \[document or free text to list and explain risks\]). This tends to be part of the appraisal documents..
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Add a document, set its `.documentType` to 'climateAndDisasterRiskAssessment', add a description of the type of climate and disaster risks to which the project is exposed to its `.description` and set  `.url` to the URL of the risk assessment document .
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "climateAndDisasterRiskAssessment",
      "description": "The project is exposed to the following climate and disaster risks...",
      "url": "http://example.com/documents/climateAndDisasterRiskAssessment .pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Climate measures)=

`````{grid} 2

````{grid-item-card} Climate measures
:columns: 4
CoST IDS element
^^^
Clarify whether the project design considered climate change mitigation and/or adaptation measures,. disclosing the design demonstrating how the measures were incorporated. This can comprise, without limitation the following:

use of lower-emission sources of energy
use of lower-emission materials
use of recycled and reused materials
regenerative design
retrofitting design
use of carbon capture technology
assessment of extreme weather events
assessment of precipitation patterns
assessment of rising temperatures
assessment of rising sea levels
others (explain)

And \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each measure add a `ClimateMeasure` object to the `environment.climateMeasures` array, setting it's `.type` according to the matching code in the open climateMeasuresType codelist and mapping the further explanation to its `.description`.

If there is an accompanying document publish in `documents`, with `.documentType` set to 'climateMeasures' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "environment": {
    "climateMeasures": [
      {
        "type": "regenerativeDesign",
        "description": "Regenerative design measures for the project include..."
      }
    ]
  },
  "documents": [
    {
      "id": "1",
      "documentType": "climateMeasures",
      "url": "http://example.com/climateMeasures.pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Forecast of greenhouse gas emissions)=

`````{grid} 2

````{grid-item-card} Forecast of greenhouse gas emissions
:columns: 4
CoST IDS element
^^^
Disclose the forecast greenhouse gas emissions related to the project, informing the calculation, the methodology applied and where the calculation can be found (E.g. \[amount\] and \[free text for methodology clarification\]). .
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project-level:

1. Add a `Metric` object to the `.forecasts` array.

2. Set the metric's `.title` to "Greenhouse gas emissions (carbon dioxide equivalent)" and map the methodology clarification to its `.description`.

3. Add an `Observation` object to the metric's `.observations` array and:

- Map the amount of greenhouse gas emissions in tonnes of CO2 equivalent to the observation's `.measure`
- Set the `.unit.name` to "Tonne (metric ton)", `.unit.scheme` to 'UNCEFACT' and `.unit.id` to "TNE"
- Set `.period` to the period covered by the forecast.

4. If supporting documentation is available, publish in documents, with `.documentType` set to 'GhgEmissionForecast' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "forecasts": [
    {
      "id": "1",
      "title": "Greenhouse gas emissions (carbon dioxide equivalent)",
      "description": "Emission forecasts are calculated using the following methodology...",
      "observations": [
        {
          "id": "1",
          "period": {
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "2049-12-31T00:00:00Z"
          },
          "measure": 1000000,
          "unit": {
            "name": "Tonne (metric ton)",
            "scheme": "UNCEFACT",
            "id": "TNE"
          }
        }
      ]
    }
  ],
  "documents": [
    {
      "id": "1",
      "documentType": "GhgEmissionForecast",
      "url": "http://example.com/GhgEmissionForecast.pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Environmental certifications)=

`````{grid} 2

````{grid-item-card} Environmental certifications
:columns: 4
CoST IDS element
^^^
Disclose environmental and/or climate related certifications issued for contractors and subcontractors such as ISO 14001 for environmental management (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Contracting process level: Publish in `documents`, with `.documentType` set to 'contractorEnvironmentalCertification' and include a short description and/or a link to a document providing details.
```json
{
  "contractingProcesses": [
    {
      "id": "1",
      "summary": {
        "documents": [
          {
            "id": "1",
            "documentType": "contractorEnvironmentalCertification",
            "url": "http://example.com/documents/contractorEnvironmentalCertification.pdf"
          }
        ]
      }
    }
  ]
}
```
````

`````


(Environment and climate-Decommissioning plans)=

`````{grid} 2

````{grid-item-card} Decommissioning plans
:columns: 4
CoST IDS element
^^^
Disclose the decommissioning plans for the project assets \[document\]..
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Publish in `documents`, with `.documentType` set to 'decommissioningPlans' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "decommissioningPlans",
      "url": "http://example.com/documents/decommissioningPlans.pdf"
    }
  ]
}
```
````

`````


(Environment and climate-Decommissioning cost forecast)=

`````{grid} 2

````{grid-item-card} Decommissioning cost forecast
:columns: 4
CoST IDS element
^^^
Disclose the forecast decommissioning costs for the project assets \[value, currency\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

1. Add a `CostMeasurement` object to the `.costMeasurements` array and set:

- `.id` incrementally
- `.status` to 'endOfLifeForecast'
- `.date` to the date that the forecast was prepared.

2. Add a `CostGroup` object to the cost measurement's `.costGroups` array, set its `.id` incrementally and set its `.category` to 'endOfLife'
3. Add a `Cost` object to the cost group's `.costs` array, set its `.id` incrementally and set its `.value` to the amount and currency of the forecast decommissioning costs.
```json
{
  "costMeasurements": [
    {
      "id": "1",
      "status": "endOfLifeForecast",
      "date": "2024-05-01T00:00:00Z",
      "costGroups": [
        {
          "id": "1",
          "category": "endOfLife",
          "costs": [
            {
              "id": "1",
              "value": {
                "amount": 50000000,
                "currency": "USD"
              }
            }
          ]
        }
      ]
    }
  ]
}
```
````

`````

## Climate finance


(Climate finance-Climate objective)=

`````{grid} 2

````{grid-item-card} Climate objective
:columns: 4
CoST IDS element
^^^
Disclose the main climate objective that the project addresses.

Select from a list:
Eg:

- mitigation
- adaptation
- cross-cutting
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Add the relevant code from the environmentalGoal codelist to the `environment.goals` array
```json
{
  "environment": {
    "goals": [
      "climateChangeMitigation"
    ]
  }
}
```
````

`````


(Climate finance-Financial instrument)=

`````{grid} 2

````{grid-item-card} Financial instrument
:columns: 4
CoST IDS element
^^^
Disclose the financial instrument type from the list:
loan
concessional
non-concessional
grant
equity
guarantees
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: For each instrument, add a `finance` object to the `budget.finance` array. Set the `.id` appropriately. Set the `.financeCategory` to the matching code from the financeCategory codelist.
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "financeCategory": "seniorDebt",
        "concessional": false
      }
    ]
  }
}
```
````

`````


(Climate finance-Climate transformation)=

`````{grid} 2

````{grid-item-card} Climate transformation
:columns: 4
CoST IDS element
^^^
Clarify the theory of change, systemic transition or transformation that is intended \[free text to explain\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Publish in documents, with `.documentType` set to 'climateTransformation' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "climateTransformation",
      "url": "http://example.com/climateFinanceReport",
      "pageStart": "13",
      "pageEnd": "14"
    }
  ]
}
```
````

`````


(Climate finance-Climate finance decision-maker)=

`````{grid} 2

````{grid-item-card} Climate finance decision-maker
:columns: 4
CoST IDS element
^^^
Identify who approved the climate finance investment in the country (organization, party, role)
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Nationally Determined Contributions (NDC))=

`````{grid} 2

````{grid-item-card} Nationally Determined Contributions (NDC)
:columns: 4
CoST IDS element
^^^
Select from a list of international commitments and clarify how the project is aligned with it \[codelist, free text to explain\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
See mapping for data point "Policy coherence" in Institutional extension adding the selected codes to the `policyAlighment.policies` array.
```json
{
  "policyAlignment": {
    "policies": [
      "nationallyDeterminedContributions"
    ],
    "description": "The project is intended to contribute towards the NDC set out in 2022."
  },
  "documents": [
    {
      "id": "1",
      "documentType": "policyAlignment",
      "url": "http://example.com/ndcAlignment.pdf",
      "pageStart": "13",
      "pageEnd": "14"
    }
  ]
}
```
````

`````


(Climate finance-Paris Agreement)=

`````{grid} 2

````{grid-item-card} Paris Agreement
:columns: 4
CoST IDS element
^^^
Select from a list of international commitments and clarify how the project is aligned with it \[codelist, free text to explain\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
See mapping for data point "Policy coherence" in Institutional extension adding `parisAgreement` to the `policyAlighment.policies` array.
```json

```
````

`````


(Climate finance-Beneficiaries)=

`````{grid} 2

````{grid-item-card} Beneficiaries
:columns: 4
CoST IDS element
^^^
Disclose who is the climate finance investment intended to benefit \[free text to explain the beneficiaries\] and number of beneficiaries. \[Select from the list:
Direct
Indirect\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Amount of investment)=

`````{grid} 2

````{grid-item-card} Amount of investment
:columns: 4
CoST IDS element
^^^
Disclose the quantum of the climate finance investment \[value, currency\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: For each financing instrument, add the value and currency to the`.value` in the `finance` object in `budget.finance`
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "value": {
          "amount": "3000000",
          "currency": "EUR"
        }
      }
    ]
  }
}
```
````

`````


(Climate finance-Funding source)=

`````{grid} 2

````{grid-item-card} Funding source
:columns: 4
CoST IDS element
^^^
Disclose who is providing the finance \[party/organization/role\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Add the organization to the `parties` array and add 'funder' to their `.roles` array.
Map the organization's `.id` from the party array to `financingParty.id` in the `budget.finance`
```json
{
  "parties": [
    {
      "id": "1",
      "name": "African Development Bank",
      "roles": [
        "funder"
      ]
    }
  ],
  "budget": {
    "finance": [
      {
        "id": "1",
        "financingParty": {
          "id": "1",
          "name": "African Development Bank"
        }
      }
    ]
  }
}
```
````

`````


(Climate finance-Green Climate Fund Accredited Entity)=

`````{grid} 2

````{grid-item-card} Green Climate Fund Accredited Entity
:columns: 4
CoST IDS element
^^^
For projects financed by the Green Climate Fund, disclose the accredited entities through which GCF resources are accessed.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

Add each accredited entity organization to the `parties` array and add 'gcfAccreditedEntity' to its `.roles` array.
```json
{
  "parties": [
    {
      "id": "1",
      "name": "Agency for Agricultural Development of Morocco",
      "roles": [
        "gcfAccreditedEntity"
      ]
    }
  ]
}
```
````

`````


(Climate finance-Accredited Entity Type)=

`````{grid} 2

````{grid-item-card} Accredited Entity Type
:columns: 4
CoST IDS element
^^^
Select from the lists:
Private
Public
non-governmental
sub-national
national
regional
international
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Project preparation costs)=

`````{grid} 2

````{grid-item-card} Project preparation costs
:columns: 4
CoST IDS element
^^^
Disclose the amounts invested in project preparation \[value, currency\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Project preparation period)=

`````{grid} 2

````{grid-item-card} Project preparation period
:columns: 4
CoST IDS element
^^^
Disclose dates for project preparation \[start date, end date\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Project approval period)=

`````{grid} 2

````{grid-item-card} Project approval period
:columns: 4
CoST IDS element
^^^
Disclose dates for project approval \[submission date, approval date\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Ratio of co-finance)=

`````{grid} 2

````{grid-item-card} Ratio of co-finance
:columns: 4
CoST IDS element
^^^
Disclose the ratio of co-finance. Select from a list to specify amounts.

Eg:\
Domestic mobilisations \[value or NA\]
Private Finance \[value or NA\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each co-financing arrangement add a new `finance` object to the `budget.finance` array. Map the value and currency to the objects `.value`. Add the financing party to the parties array and add `funder` to their `roles` array. Map the funders `id` and `name` to the `.financingParty` object in the `finance` object.
```json
{
  "parties": [
    {
      "id": "1",
      "name": "Green Climate Fund",
      "roles": [
        "funder"
      ]
    },
    {
      "id": "2",
      "name": "Agency for Agricultural Development of Morocco",
      "roles": [
        "funder"
      ]
    }
  ],
  "budget": {
    "finance": [
      {
        "id": "1",
        "financingParty": {
          "id": "1",
          "name": "Green Climate Fund"
        },
        "value": {
          "amount": "3000000",
          "currency": "USD"
        }
      },
      {
        "id": "2",
        "financingParty": {
          "id": "2",
          "name": "Agency for Agricultural Development of Morocco"
        },
        "value": {
          "amount": "15000",
          "currency": "USD"
        }
      }
    ]
  }
}
```
````

`````


(Climate finance-Terms of climate finance)=

`````{grid} 2

````{grid-item-card} Terms of climate finance
:columns: 4
CoST IDS element
^^^
This includes several financial terms:
maturity (years)
Grace period (years)
annual principal repayment years (% of initial principle)
Interest (%)
Service fee (per annum)
Commitment fee (per annum)
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Carbon efficiency)=

`````{grid} 2

````{grid-item-card} Carbon efficiency
:columns: 4
CoST IDS element
^^^
Disclose the cost per tonne of CO2 equivalent \[value, currency\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Publish the cost in `environment.abatementCost`. If supporting documentation is available, publish in documents with `.documentType` set to 'abatementCostMethodology'.
```json

```
````

`````


(Climate finance-Non-climate co-benefits)=

`````{grid} 2

````{grid-item-card} Non-climate co-benefits
:columns: 4
CoST IDS element
^^^
Identify potential non-climate impacts that have been factored into the project planning. Select from the list:
economic
social
environmental
gender empowerment
\[add free text to explain the co-benefits\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: For each impact identified add a `benefit` object to the `benefits` array and assign it a locally unique `id`. Set the `title` as the list code and add details explaining the benefit to `.description`.
```json
{
  "benefits": [
    {
      "id": "1",
      "title": "environmental",
      "description": "The new water management plant will mean less water is removed from the delta meaning more is left in place for use by the local biome."
    }
  ]
}
```
````

`````


(Climate finance-Public consultation meetings)=

`````{grid} 2

````{grid-item-card} Public consultation meetings
:columns: 4
CoST IDS element
^^^
Disclose the occurrence of public meetings with communities and impacted groups including the minutes, number of the participants, dates and location of these meetings (E.g. Meeting 1 \[date\] \[location\] \[number of participants\] \[Document\], Meeting 2 \[date\] \[location\] \[number of participants\], \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
See mapping for data point "Public consultation meetings" in the Social extension
```json

```
````

`````


(Climate finance-Disbursement records)=

`````{grid} 2

````{grid-item-card} Disbursement records
:columns: 4
CoST IDS element
^^^
Disbursements dates according to financial agreement versus actual disbursements dates \[value, currency, date\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
For each planned disbursement:

- If the disbursement relates to a contracting processes, for example a payment from a funder to a supplier or subcontractor of a supplier, get the `ContractingProcess` in the `.contractingProcesses` array to which the disbursement relates and add a `Milestone` object to its `.summary.milestones` array. Otherwise, if the disbursement relates to the project, for example a payment from a funder to the public authority, add a `Milestone` object to the project-level `.milestones` array.
- Set the milestone's:
  - `.id` incrementally
  - `.status` to 'scheduled'
  - `.dueDate` to the date on which the disbursement is planned to occur
  - `.type` to 'payment'
  - `.value` to the amount and currency of the planned disbursement

For each actual disbursement:

- If the disbursement relates to a contracting processes, for example a payment from a funder to a supplier or subcontractor of a supplier, get the `ContractingProcess` in the `.contractingProcesses` array to which the disbursement relates and add a `Transaction` object to its `.summary.transactions` array. Otherwise, if the disbursement relates to the project, for example a payment from a funder to the public authority, add a `Transaction` object to the project-level `.transactions` array.

- Set the transaction's:

  - `.id` incrementally
  - `.date` to the date of the disbursement
  - `.value` to the amount and currency of the disbursement

- Get the `Organization` in `.parties` that represents the payer. If none exists yet, [add an organization](../common.md#add-an-organization) for the payer:

  - Add 'payer' to the organization's `.roles` array
  - Set the transaction's `.payer` to the `.id` and `.name` of the organization

- Get the `Organization` in `.parties` that represents the payee. If none exists yet, [add an organization](../common.md#add-an-organization) for the payee:

  - Add 'payee' to the organization's `.roles` array.
  - Set the transaction's `.payee` to the `.id` and `.name` of the organization

- Get the `Milestone` in `.milestones` that represents that planned disbursement:

  - Set its `.status` to 'met'
  - Set its `.dateMet` to the date of the disbursement
  - Set the transaction's `.relatedImplementationMilestone` to the `.id` and `.title` of the milestone
```json
{
  "milestones": [
    {
      "id": "1",
      "title": "Grant disbursement",
      "status": "met",
      "dueDate": "2023-07-01T00:00:00Z",
      "dateMet": "2023-08-01T00:00:00Z",
      "type": "payment",
      "value": {
        "amount": 5000000,
        "currency": "USD"
      }
    }
  ],
  "transactions": [
    {
      "id": "1",
      "date": "2023-08-01T00:00:00Z",
      "value": {
        "amount": 5000000,
        "currency": "USD"
      },
      "payer": {
        "id": "1",
        "name": "United Nations Development Programme"
      },
      "payee": {
        "id": "2",
        "name": "Ministry of works"
      },
      "relatedImplementationMilestone": {
        "id": "1",
        "title": "Grant disbursement"
      }
    }
  ]
}
```
````

`````


(Climate finance-Type of project monitoring)=

`````{grid} 2

````{grid-item-card} Type of project monitoring
:columns: 4
CoST IDS element
^^^
Select from a list:
internal
external
mixed
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Performance monitoring)=

`````{grid} 2

````{grid-item-card} Performance monitoring
:columns: 4
CoST IDS element
^^^
Disclose Key Performance Indicators adopted by the project (E.g. \[free text\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each KPI add a `Metric` object to the `metrics` array and set the object's fields according to the schema. Prefix the metric's `.title` with "KPI".
```json
{
  "metrics": [
    {
      "id": "1",
      "title": "KPI: Capacity utilization"
    }
  ]
}
```
````

`````


(Climate finance-Reporting period)=

`````{grid} 2

````{grid-item-card} Reporting period
:columns: 4
CoST IDS element
^^^
It could be quarterly, annually, biannually, etc. \[free text\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each KPI metric add the sentence "To be reported XXX" where XXX is the reporting frequency to the metrics `.description`.
```json
{
  "metrics": [
    {
      "id": "1",
      "title": "KPI: Capacity utilization",
      "description": "To be reported annually."
    }
  ]
}
```
````

`````


(Climate finance-Oversight reports)=

`````{grid} 2

````{grid-item-card} Oversight reports
:columns: 4
CoST IDS element
^^^
\[document\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Independent monitoring)=

`````{grid} 2

````{grid-item-card} Independent monitoring
:columns: 4
CoST IDS element
^^^
Identify the entities acting as independent monitors of the project (E.g. \[free text\])
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Add an entry to `parties` with 'independentMonitor' included in its `.roles`.
```json
{
  "parties": [
    {
      "id": "1",
      "name": "Climate monitor Africa",
      "roles": [
        "independentMonitor"
      ]
    }
  ]
}
```
````

`````


(Climate finance-Independent evaluation)=

`````{grid} 2

````{grid-item-card} Independent evaluation
:columns: 4
CoST IDS element
^^^
Disclose technical audits produced at end of the project (E.g. \[free text\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Add a document, set its `.documentType` to 'technicalAuditReport', add a description of the reports findings to its `.description` and set `.url` to the URL of the document that details the audit (if available). If multiple reports have been produced add a document for each one.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "technicalAuditReport",
      "description": "The project has been constructed as specified...",
      "url": "http://example.com/technicalAuditReport.pdf",
      "pageStart": "13",
      "pageEnd": "14"
    }
  ]
}
```
````

`````


(Climate finance-Impact measurement)=

`````{grid} 2

````{grid-item-card} Impact measurement
:columns: 4
CoST IDS element
^^^
Clarify the methodology or system to measure the long-term impact of the project solution (E.g. \[free text\].
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Publish in documents, with `.documentType` set to 'impactMethodology' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "impactMethodology",
      "description": "The long term impact of this project will be measured according to...",
      "url": " http://example.com/impactMethodology.pdf "
    }
  ]
}
```
````

`````


(Climate finance-Carbon footprint)=

`````{grid} 2

````{grid-item-card} Carbon footprint
:columns: 4
CoST IDS element
^^^
Disclose the carbon footprint of the project \[value, tons CO2 equivalent, free text to describe the methodology used to measure the carbon footprint\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project-level:

1. Add a `Metric` object to the `.metrics` array.

2. Set the metric's `.title` to "Greenhouse gas emissions (carbon dioxide equivalent) - operation" and map the methodology clarification to its `.description`.

3. Add an `Observation` object to the metric's `.observations` array and:

- Map the amount of greenhouse gas emissions in tonnes of CO2 equivalent to the observation's `.measure`
- Set the `.unit.name` to "Tonne (metric ton)", `.unit.scheme` to 'UNCEFACT' and `.unit.id` to "TNE"
- Set `.period` to the period covered by the calculation.

4. If supporting documentation is available, publish in documents, with `.documentType` set to 'ghgEmissions' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "metrics": [
    {
      "id": "1",
      "title": "Greenhouse gas emissions (carbon dioxide equivalent) - operation",
      "description": "Emissions are calculated using the following methodology...",
      "observations": [
        {
          "id": "1",
          "period": {
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "2049-12-31T00:00:00Z"
          },
          "measure": 1000000,
          "unit": {
            "name": "Tonne (metric ton)",
            "scheme": "UNCEFACT",
            "id": "TNE"
          }
        }
      ]
    }
  ],
  "documents": [
    {
      "id": "1",
      "documentType": "GhgEmissions",
      "url": " http://example.com/ghgEmissions.pdf "
    }
  ]
}
```
````

`````


(Climate finance-Infrastructure assets to be decommissioned)=

`````{grid} 2

````{grid-item-card} Infrastructure assets to be decommissioned
:columns: 4
CoST IDS element
^^^
Identify the asset for disposal purpose \[free text\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Decommission period)=

`````{grid} 2

````{grid-item-card} Decommission period
:columns: 4
CoST IDS element
^^^
Intended start and end dates of decommissioning.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Climate finance-Decommission plan)=

`````{grid} 2

````{grid-item-card} Decommission plan
:columns: 4
CoST IDS element
^^^
Disclose the technical plan for decommissioning (E.g.: \[Doc\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
See decommissioning plan data point in environment extension
```json

```
````

`````


(Climate finance-Carbon decommission savings)=

`````{grid} 2

````{grid-item-card} Carbon decommission savings
:columns: 4
CoST IDS element
^^^
Disclose the evaluation of CO2 savings as a result of decommissioning \[value, tons CO2 equivalent\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project-level:

1. Add a `Metric` object to the `.forecasts` array.

2. Set the metric's `.title` to "Greenhouse gas emissions reduction (carbon dioxide equivalent)" and map the methodology clarification to its `.description`.

3. Add an `Observation` object to the metric's `.observations` array and:

- Map the amount of greenhouse gas emissions in tonnes of CO2 equivalent to the observation's `.measure`
- Set the `.unit.name` to "Tonne (metric ton)", `.unit.scheme` to 'UNCEFACT' and `.unit.id` to "TNE"
- Set `.period` to the period covered by the calculation.

4. If supporting documentation is available, publish in documents, with `.documentType` set to 'ghgEmissionsReduction' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "id": "oc4ids-bu3kcz-123456789",
  "forecasts": [
    {
      "id": "1",
      "title": "Greenhouse gas emissions reduction (carbon dioxide equivalent)",
      "description": "Emission reduction forecasts are calculated using the following methodology...",
      "observations": [
        {
          "id": "1",
          "period": {
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "2049-12-31T00:00:00Z"
          },
          "measure": 1000000,
          "unit": {
            "name": "Tonne (metric ton)",
            "scheme": "UNCEFACT",
            "id": "TNE"
          }
        }
      ]
    }
  ],
  "documents": [
    {
      "id": "1",
      "documentType": "ghgEmissionsReduction",
      "url": " http://example.com/GhgEmissionsReduction.pdf "
    }
  ]
}
```
````

`````


(Climate finance-Decommission mitigation plan)=

`````{grid} 2

````{grid-item-card} Decommission mitigation plan
:columns: 4
CoST IDS element
^^^
Disclose mitigation plan for people and communities affected by decommissioning (E.g.: \[Doc\]),
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

Publish in documents, with `.documentType` set to 'socialImpact' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "id": "oc4ids-bu3kcz-123456789",
  "documents": [
    {
      "id": "1",
      "documentType": "socialImpact",
      "url": "http://example.com/socialImpact.pdf",
      "pageStart": "13",
      "pageEnd": "14"
    }
  ]
}
```
````

`````

## Social


(Social-Number of beneficiaries)=

`````{grid} 2

````{grid-item-card} Number of beneficiaries
:columns: 4
CoST IDS element
^^^
Indicate the number of direct and indirect project beneficiaries (E.g. direct: \[number\]; indirect: "number"). Beneficiaries are the individuals who benefit directly or indirectly from the project; they are the target group of the infrastructure project and their needs are addressed by the intervention.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^

```json

```
````

`````


(Social-Inclusive design and implementation)=

`````{grid} 2

````{grid-item-card} Inclusive design and implementation
:columns: 4
CoST IDS element
^^^
Clarify whether gender, people with disabilities and vulnerable and disadvantaged populations were considered in the project design (e.g. "free text to explain how the design meets inclusion goals" and document to support - the project design) and project implementation (e.g. "free text to explain implementation practices targeting inclusion goals" and document to support - contractor policy and procedures).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project-level:

1. Add a document, set its `.documentType` to 'inclusiveDesign' and add an explanation of how the project design meets inclusion goals to its `.description`. If supporting documentation is available, add its URL to `.url`.

2. Add a document, set its `.documentType` to 'inclusiveImplementation' and add an explanation of how the project  imlpementation practices target inclusion goals to its `.description`. If supporting documentation is available, add its URL to `.url`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "inclusiveDesign",
      "description": "The project's design meets its inclusion goals by...",
      "url": "http://example.com/documents/inclusiveDesign.pdf"
    },
    {
      "id": "2",
      "documentType": "inclusiveImplementation",
      "description": "The project's implementation practices target inclusion goals by...",
      "url": "http://example.com/documents/inclusiveImplementation.pdf"
    }
  ]
}
```
````

`````


(Social-Indigenous land)=

`````{grid} 2

````{grid-item-card} Indigenous land
:columns: 4
CoST IDS element
^^^
Identify whether the project is located or cut through indigenous land. Use the information at the LandMark - Global Platform of Indigenous and Community Lands on both databases Indigenous Lands Acknowledged by Government and Not Acknowledged by Government (customary tenure or with formal land claim submitted) to disclose the information.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

If the project is located or cut through indigenous land:

1. Set `.social.indigenousLand` to `true`
   2 Add a `Location` object to the `.locations` array, set its `.id` incrementally and set its description to "Indigenous land: <Name> (<Category>)" substituting <Name>  and <Category> for the name and land category from the Landmark database.

If the project is not located or cut through indigenous land, set `.social.indigenousLand` to `false`.
```json
{
  "social": {
    "indigenousLand": true
  },
  "locations": [
    {
      "id": "1",
      "description": "Indigenous land: Section 1 Block III Rowallan Survey District (Maori Freehold Land)"
    }
  ]
}
```
````

`````


(Social-Public consultation meetings)=

`````{grid} 2

````{grid-item-card} Public consultation meetings
:columns: 4
CoST IDS element
^^^
Disclose the occurrence of public meetings with communities and impacted groups including meeting invite, the number of the participants, dates and location of these meetings.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level:

For each meeting:

1. Publish the meeting invite. Add a document, set its `.documentType` to 'consultationMeetingInvite' and its `.url` to the URL at which the meeting invite is available.

2. Publish the meeting details. Add a `Meeting` object to the `.social.consultationMeetings` array and set:

- `.id` incrementally
- `.date` to the date of the meeting
- `.address` to the address of the meeting
- `.participantCount` to the number of people that participated in the meeting

3. Publish the meeting minutes. Add a document, set its `.documentType` to 'consultationMeetingMinutes' and its `.url` to the URL at which the meeting minutes are available.
```json
{
  "social": {
    "consultationMeetings": [
      {
        "id": "1",
        "date": "2024-01-01T00:00:00Z",
        "address": {
          "streetAddress": "1600 Amphitheatre Pkwy",
          "locality": "Mountain View",
          "region": "CA",
          "postalCode": "94043",
          "countryName": "United States"
        },
        "participantCount": 12
      }
    ]
  },
  "documents": [
    {
      "id": "1",
      "documentType": "consultationMeetingInvite",
      "url": "http://example.com/consultationMeetingInvite.pdf"
    },
    {
      "id": "2",
      "documentType": "consultationMeetingMinutes",
      "url": "http://example.com/consultationMeetingMinutes.pdf"
    }
  ]
}
```
````

`````


(Social-Land compensation budget)=

`````{grid} 2

````{grid-item-card} Land compensation budget
:columns: 4
CoST IDS element
^^^
Disclose budget allocated to fund land compensation (E.g. \[value\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Set `.social.landCompensationBudget` to the amount and currency of the budget allocated for land compensation.
```json
{
  "social": {
    "landCompensationBudget": {
      "amount": 1000000,
      "currency": "USD"
    }
  }
}
```
````

`````


(Social-Labour obligations)=

`````{grid} 2

````{grid-item-card} Labour obligations
:columns: 4
CoST IDS element
^^^
Disclose labour obligations in the construction contract. This can include, without limitation, the following:

Minimum wage
Overtime
Prohibition of forced labour
Prohibition of child labour
Equal opportunity
Non-discrimination
Freedom of association
Grievance mechanism
Working at height
Underground work
Handling of materials/equipment
Monitoring of accidents
Traffic management
Accommodation
Protective equipment
Others (explain)
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Contracting process level:

Publish a summary of the labor obligations:

1. For each labor obligation in the contract, add a code from the laborObligations codelist to the`.summary.social.laborObligations.obligations` array.
2. Optionally, add a further explanation of the labor obligations to `.summary.social.laborObligations.description`.

Publish the bidding documents that specify labor obligations: Add a document to `.summary.documents`, set its `.id` incrementally, set its `.documentType` to 'biddingDocuments' and set its `.url` to the URL at which the documents are available.

Publish the signed contract that includes labor obligations:  Add a document to `.summary.documents`, set its `.id` incrementally, set its `.documentType` to 'contractSigned' and set its `.url` to the URL at which the signed contract that includes labor obligations is accessible.
```json
{
  "contractingProcesses": [
    {
      "id": "1",
      "summary": {
        "social": {
          "laborObligations": {
            "obligations": [
              "minimumWage",
              "overtime"
            ],
            "description": "The contract's labor obligations include a minimum wage of $20 per hour and an overtime limit of 10 hours per week."
          }
        },
        "documents": [
          {
            "id": "1",
            "documentType": "biddingDocuments",
            "url": "http://example.com/biddingDocuments.pdf"
          },
          {
            "id": "2",
            "documentType": "contractSigned",
            "url": "http://example.com/contractSigned.pdf"
          }
        ]
      }
    }
  ]
}
```
````

`````


(Social-Labour budget)=

`````{grid} 2

````{grid-item-card} Labour budget
:columns: 4
CoST IDS element
^^^
Disclose the amount allocated by the main contractor to cover for labour costs (E.g. \[value\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Contract level: Publish the amount and currency of the labor budget in `.summary.social.laborBudget`.
```json
{
  "contractingProcesses": [
    {
      "id": "1",
      "summary": {
        "social": {
          "laborBudget": {
            "amount": 10000000,
            "currency": "USD"
          }
        }
      }
    }
  ]
}
```
````

`````


(Social-Workers' accidents)=

`````{grid} 2

````{grid-item-card} Workers' accidents
:columns: 4
CoST IDS element
^^^
Disclose summary statistics on accidents and fatalities involving construction workers, and an explanation of these events.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

Publish summary statistics on worker accidents:

1. Add a `Metric` object to the `.metrics` array, set its `.id` incrementally and set its `.title` to "Worker accidents".
2. For each reporting period, add an `Observation` object to the metric's `.observations` array, set its `.id` incrementally, set its `.period` to the reporting period and set its `.measure` to the number of accidents. If further details available, add them to the observation's `.notes` field.

Publish summary statistics on worker fatalities:

1. Add a `Metric` object to the `.metrics` array, set its `.id` incrementally and set its `.title` to "Worker fatalities".
2. For each reporting period, add an `Observation` object to the metric's `.observations` array, set its `.id` incrementally, set its `.period` to the reporting period and set its `.measure` to the number of fatalities. If further details available, add them to the observation's `.notes` field.
```json
{
  "metrics": [
    {
      "id": "1",
      "title": "Worker accidents",
      "observations": [
        {
          "id": "1",
          "period": {
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "2024-06-30T00:00:00Z"
          },
          "measure": 12,
          "notes": "In H1 2024, most accidents were related to..."
        }
      ]
    },
    {
      "id": "2",
      "title": "Worker fatalities",
      "observations": [
        {
          "id": "1",
          "period": {
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "2024-06-30T00:00:00Z"
          },
          "measure": 0
        }
      ]
    }
  ]
}
```
````

`````


(Social-Health and safety certifications)=

`````{grid} 2

````{grid-item-card} Health and safety certifications
:columns: 4
CoST IDS element
^^^
Disclose labour related certifications issued in relation to project contractors and subcontractors such as ISO 45001 for Health and Safety (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Contracting process level: Publish in `.summary.documents`, with `.documentType` set to 'contractorHealthAndSafetyCertification' and include a short description and/or a link to a document providing details.
```json
{
  "contractingProcesses": [
    {
      "id": "1",
      "summary": {
        "documents": [
          {
            "id": "1",
            "documentType": "contractorHealthAndSafetyCertification",
            "url": "http://example.com/documents/contractorHealthAndSafetyCertification.pdf"
          }
        ]
      }
    }
  ]
}
```
````

`````


(Social-Construction materials testing)=

`````{grid} 2

````{grid-item-card} Construction materials testing
:columns: 4
CoST IDS element
^^^
Disclose materials tests performed during implementation \[document\]. These can include, without limitation, the following:

Foundations
Pavements
Soil
Steel structure
Asphalt
Retaining walls
Concrete
Masonry
Roofs
Compression
Compaction
Thickness
Others (explain)

\[Free text to add not mentioned tests\]

Document
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

Publish a summarry of the material tests:

1. For each material test, add a code from the materialTests codelist to the`.social.healthAndSafety.materialTests.tests` array.
2. Optionally, add a further explanation of the material tests to `.social.healthAndSafety.materialTests.description`.

Publish test results: For each test result, add a document, set `.documentType` to 'materialTestResults' and set `.url` to the URL at which the document is accessible.
```json
{
  "social": {
    "healthAndSafety": {
      "materialTests": {
        "tests": [
          "retainingWalls",
          "roofs"
        ],
        "description": "Tests were conducted of the main retaining wall and of the roof of each structure according to..."
      }
    }
  },
  "documents": [
    {
      "id": "1",
      "documentType": "materialTestResults",
      "url": "http://example.com/materialTestResults.pdf"
    }
  ]
}
```
````

`````


(Social-Building inspections)=

`````{grid} 2

````{grid-item-card} Building inspections
:columns: 4
CoST IDS element
^^^
Disclose building inspections during project implementation (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Publish in `documents`, with `.documentType` set to 'buildingInspectionReport' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "buildingInspectionReport",
      "url": "http://example.com/buildingInspectionReport.pdf"
    }
  ]
}
```
````

`````


(Social-Jobs generated)=

`````{grid} 2

````{grid-item-card} Jobs generated
:columns: 4
CoST IDS element
^^^
Disclose estimated and actual jobs (direct/indirect) during project implementation and estimated and actual jobs during operation (E.g. \[direct: value\] \[indirect: value\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

Publish job creation estimates:

1. Add a `Metric` object to the `forecasts` array and set its `.title` to 'Jobs created'.
2. Add an `observation` object for each job relationship - stage pair and set `.dimensions` accordingly, i.e.

- relationship: direct, stage: implementation
- relationship: indirect, stage: implementation
- relationship: direct, stage: operation
- relationship: indirect, stage: operation

3. Record the estimated number of jobs created for each relationship and stage in the relevant observation's `.measure`.

Publish actual jobs created:

1. Add a `Metric` object to the `metrics` array and set its `.title` to 'Jobs created'.
2. Add an `observation` object for each job relationship - stage pair and set `.dimensions` accordingly, i.e.

- relationship: direct, stage: implementation
- relationship: indirect, stage: implementation
- relationship: direct, stage: operation
- relationship: indirect, stage: operation

3. Record the actual number of jobs created for each relationship and stage in the relevant observation's `.measure`.
```json
{
  "forecasts": [
    {
      "id": "1",
      "title": "Jobs created",
      "observations": [
        {
          "id": "1",
          "measure": 1000,
          "dimensions": {
            "relationship": "direct",
            "stage": "implementation"
          }
        },
        {
          "id": "2",
          "measure": 5000,
          "dimensions": {
            "relationship": "indirect",
            "stage": "implementation"
          }
        },
        {
          "id": "3",
          "measure": 300,
          "dimensions": {
            "relationship": "direct",
            "stage": "operation"
          }
        },
        {
          "id": "4",
          "measure": 2000,
          "dimensions": {
            "relationship": "indirect",
            "stage": "operation"
          }
        }
      ]
    }
  ],
  "metrics": [
    {
      "id": "1",
      "title": "Jobs created",
      "observations": [
        {
          "id": "1",
          "measure": 979,
          "dimensions": {
            "relationship": "direct",
            "stage": "implementation"
          }
        },
        {
          "id": "2",
          "measure": 4120,
          "dimensions": {
            "relationship": "indirect",
            "stage": "implementation"
          }
        },
        {
          "id": "3",
          "measure": 295,
          "dimensions": {
            "relationship": "direct",
            "stage": "operation"
          }
        },
        {
          "id": "4",
          "measure": 1875,
          "dimensions": {
            "relationship": "indirect",
            "stage": "operation"
          }
        }
      ]
    }
  ]
}
```
````

`````

## Institutional


(Institutional-Policy coherence)=

`````{grid} 2

````{grid-item-card} Policy coherence
:columns: 4
CoST IDS element
^^^
Disclose documentation that evidences that the project is part of, or aligned with existing plans and policies, providing further details on the project's policy alignment. Consider alignment with:

SDGs
National plan or strategy
Infrastructure plan or strategy
Sector plan or strategy
Procuring entity plan or strategy
Paris Agreement
Nationally Determined Contributions (NDCs)
National Adaptation Plans
Medium-term fiscal frameworks/targets

\[free text\]
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each plan or policy to which the project is aligned, add a code from the policyAlignment codelist to the `.policyAlignment.policies` array. Add a further explanation of the project's policy alignment to `.policyAlignment.description`.

For each United Nations Sustainable Development Goal to which the project is aligned, add a `Classification` object to the `.additionalClassifications` array, set its `.scheme` to 'sdg', set its `.id` to the goal's number and set its `.description` to the goal's title.

For each United Nations Sustainable Development Goal Target to which the project is aligned, add a `Classification` object to the `.additionalClassifications` array, set its `.scheme` to 'sdgTarget', set its `.id` to the target's number and set its `.description` to the target's title.

If further documentation of the project's policy alignment is available, add a document with `.documentType` set to 'policyAlignment', `url` set to the URL at which the documentation can be accessed.
```json
{
  "additionalClassifications": [
    {
      "scheme": "sdg",
      "id": "6",
      "description": "Ensure availability and sustainable management of water and sanitation for all"
    },
    {
      "scheme": "sdgTarget",
      "id": "6.3",
      "description": "By 2030, improve water quality by reducing pollution, eliminating dumping and minimizing release of hazardous chemicals and materials, halving the proportion of untreated wastewater and substantially increasing recycling and safe reuse globally"
    }
  ],
  "policyAlignment": {
    "policies": [
      "infrastructurePlan"
    ],
    "description": "The project is intended to contribute towards the goals set out in the 2021 Australian Infrastructure Plan."
  },
  "documents": [
    {
      "id": "1",
      "documentType": "policyAlignment",
      "url": "http://example.com/infrastructurePlanAlignment.pdf"
    }
  ]
}
```
````

`````


(Institutional-Freedom of information requests)=

`````{grid} 2

````{grid-item-card} Freedom of information requests
:columns: 4
CoST IDS element
^^^
Disclose Freedom of Information (FoI) requests that have been presented in relation to the project \[E.g. Document\]. Note that FoI requests can also be known as access to information requests.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each freedom of information request, add a document, set `.documentType` to 'foiRequest' and set `.url` to the URL at which the request is available
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "foiRequest",
      "url": "http://example.com/foiRequest-1.pdf"
    }
  ]
}
```
````

`````


(Institutional-Answers to Freedom of information requests)=

`````{grid} 2

````{grid-item-card} Answers to Freedom of information requests
:columns: 4
CoST IDS element
^^^
Disclose the responses provided by authorities to Freedom of Information (FoI) requests related to the project (Eg. \[Document\]). Note that FoI requests may also be known as access to information requests.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

For each freedom of information request response, add a document, set `.documentType` to 'foiRequestResponse' and set `.url` to the URL at which the response is available.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "foiRequest",
      "url": "http://example.com/foiRequest-1.pdf"
    }
  ]
}
```
````

`````


(Institutional-Lobbying transparency)=

`````{grid} 2

````{grid-item-card} Lobbying transparency
:columns: 4
CoST IDS element
^^^
Disclose the occurrence of meetings with interest groups, including the meeting agenda and minutes, the number of the participants, dates and location of these meetings (E.g. Meeting 1 \[date\] \[location\] \[number of participants\] \[Document\], Meeting 2 \[date\] \[location\] \[number of participants\] \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level:

For each meeting:

1. Publish the meeting agenda. Add a document, set its `.documentType` to 'lobbyingMeetingAgenda' and its `.url` to the URL at which the agenda is available.

2. Publish the meeting details. Add a `Meeting` object to the `.lobbyingMeetings` array and set:

- `.id` incrementally
- `.date` to the date of the meeting
- `.address` to the address of the meeting
- `.beneficiary` to the name of the organisation or interest group that ultimately benefits from the lobbying activity

3. Publish the meeting minutes. Add a document, set its `.documentType` to 'lobbyingMeetingMinutes' and its `.url` to the URL at which the meeting minutes are available.
```json
{
  "lobbyingMeetings": [
    {
      "id": "1",
      "date": "2024-01-01T00:00:00Z",
      "address": {
        "streetAddress": "1600 Amphitheatre Pkwy",
        "locality": "Mountain View",
        "region": "CA",
        "postalCode": "94043",
        "countryName": "United States"
      },
      "beneficiary": "Arup Group"
    }
  ],
  "documents": [
    {
      "id": "1",
      "documentType": "lobbyingMeetingAgenda",
      "url": "http://example.com/lobbyingMeetingAgenda.pdf"
    },
    {
      "id": "2",
      "documentType": "lobbyingMeetingMinutes",
      "url": "http://example.com/lobbyingMeetingMinutes.pdf"
    }
  ]
}
```
````

`````


(Institutional-Beneficial ownership)=

`````{grid} 2

````{grid-item-card} Beneficial ownership
:columns: 4
CoST IDS element
^^^
Disclose the beneficial owners of the contractors and suppliers appointed in the project (E.g. \[name, identifier\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
For each beneficial owner:

- Get the `Organization` in `.parties` that represents the contractor or supplier.
- Add a `Person` object to the organization's `.beneficialOwners` array.
- Set the person's:
  - `.id` incrementally
  - `.name` to the beneficial owner's name
  - `.identifier` to the beneficial owner's identifier
```json
{
  "parties": [
    {
      "id": "1",
      "beneficialOwners": [
        {
          "id": "1",
          "name": "Juan Perez",
          "identifier": {
            "scheme": "PRY-IDCARD",
            "id": "12345"
          }
        }
      ]
    }
  ]
}
```
````

`````


(Institutional-Sustainability criteria)=

`````{grid} 2

````{grid-item-card} Sustainability criteria
:columns: 4
CoST IDS element
^^^
Identify the presence of sustainability and non-price attributes in the award criteria.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Contracting process level:

Add a `Sustainability` object to the `.summary.tender.sustainability` array and add 'awardCriteria' to its `.strategies` array.
```json
{
  "contractingProcesses": [
    {
      "id": "1",
      "summary": {
        "tender": {
          "sustainability": [
            {
              "strategies": [
                "awardCritera"
              ]
            }
          ]
        }
      }
    }
  ]
}
```
````

`````


(Institutional-Anti-corruption certifications)=

`````{grid} 2

````{grid-item-card} Anti-corruption certifications
:columns: 4
CoST IDS element
^^^
Disclose anti-corruption certifications of the project, such as ISO 37001 on Anti-Bribery Management Systems Standard (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Publish in documents, with .documentType set to 'antiCorruptionCertification' and include a short description and/or a link to a document providing details.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "antiCorruptionCertification",
      "url": "http://example.com/ISO37001Certification.pdf"
    }
  ]
}
```
````

`````


(Institutional-Independent monitoring)=

`````{grid} 2

````{grid-item-card} Independent monitoring
:columns: 4
CoST IDS element
^^^
Identify the entities acting as independent monitors of the project (E.g. \[free text\])
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Add an entry to `parties` with 'independentMonitor' included in its `.roles`.
```json
{
  "parties": [
    {
      "id": "1",
      "name": "Transparency International New Zealand",
      "roles": [
        "independentMonitor"
      ]
    }
  ]
}
```
````

`````


(Institutional-Performance monitoring)=

`````{grid} 2

````{grid-item-card} Performance monitoring
:columns: 4
CoST IDS element
^^^
Disclose Key Performance Indicators adopted by the project (E.g. \[free text\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level: Publish in `metrics`. For each KPI add a Metric object to the metrics array and set the object's fields according to the schema. Prefix the metric's `.title` with "KPI: "
```json
{
  "metrics": [
    {
      "id": "1",
      "title": "KPI: Capacity utilisation"
    }
  ]
}
```
````

`````


(Institutional-Risk management plans)=

`````{grid} 2

````{grid-item-card} Risk management plans
:columns: 4
CoST IDS element
^^^
Disclose risk management plans prepared for the project (E.g. \[Document\]).
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Publish in documents, with .documentType set to 'riskProvisions' and include a short description and/or a link to a document providing details. If the details are part of a more general document indicate the relevant section of the document using `.pageStart` and `.pageEnd`.
```json
{
  "documents": [
    {
      "id": "1",
      "documentType": "riskProvisions",
      "url": "http://example.com/riskManagementPlan.pdf"
    }
  ]
}
```
````

`````


(Institutional-Sustainable sub-sectors)=

`````{grid} 2

````{grid-item-card} Sustainable sub-sectors
:columns: 4
CoST IDS element
^^^
Identify relevant sub-sectors related to the project scope.
Select from a list (non-exhaustive):

- Renewable energy:
  solar,
  wind,
  hydropower,
  biomass
  geothermal
- Low carbon transport
- Water and wastewater management
- Natural resource management
  flood protection

Free text to add not mentioned sub-sectors
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Add the equivalent code from ProjectSector codelist to the `sector` array.
```json
{
  "sector": [
    "solar"
  ]
}
```
````

`````

