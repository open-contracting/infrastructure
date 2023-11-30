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


(economic-and-fiscal-procurement-strategy)=

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


(economic-and-fiscal-life-cycle-cost)=

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
**Project Level:** Add a `CostMeasurement` object to the `costMeasurements` array. Set `.date` to the date the analysis was prepared. Map to the cost measurement's `.lifeCycleCost.cost`.
```json
{
  "costMeasurements": [
    {
      "id": "1",
      "date": "2014-05-01T00:00:00Z",
      "lifeCycleCost": {
        "cost": {
          "amount": 10000000,
          "currency": "USD"
        }
      }
    }
  ]
}
```
````

`````


(economic-and-fiscal-life-cycle-cost-calculation-methodology)=

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


(economic-and-fiscal-funding-source-for-preparation-implementation-and-operation)=

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
Project level:

1. Get the `BudgetBreakdowns` object in the `budget.budgetBreakdowns` array that represents the budget breakdown by stage. If none exists yet:

- Add a `BudgetBreakdowns` object to the `budget.budgetBreakdowns` array.

2. Set it's `.id` incrementally and it's `.description` to "Breakdown by stage".

3. Get the `BudgetBreakdown` object in the budget breakdowns object for each of the 3 stages. If none exists yet:

- Add 3 `BudgetBreakdown` objects to the `budget.budgetBreakdowns.budgetBreakdown` array. For each object:
- Set the `.id` incrementally.
- Set the `.description` to the stage name - "Preparation", "Implementation" or "Operation". If the funding source is not known for a stage note append "funding/budget source not specified" to the `.description`.

4. For each stage, get the `Organization` object in `.parties` that represents the party providing the funding for the stage named in `.description`. If none exists yet, [add an organization](../common.md#add-an-organization) and add 'funder' to its `.roles`.

- Set the budget breakdown's `.sourceParty` to the `.id` and `.name` of the organization.
```json
{
  "budget": {
    "budgetBreakdowns": [
      {
        "id": "1",
        "description": "Breakdown by stage",
        "budgetBreakdown": [
          {
            "id": "1",
            "description": "Preparation",
            "sourceParty": {
              "id": "1",
              "name": "Agency for Agricultural Development of Morocco"
            }
          },
          {
            "id": "2",
            "description": "Implementation",
            "sourceParty": {
              "id": "1",
              "name": "Agency for Agricultural Development of Morocco"
            }
          },
          {
            "id": "3",
            "description": "Operation funding/budget source not specified"
          }
        ]
      }
    ]
  },
  "parties": [
    {
      "id": "1",
      "name": "Agency for Agricultural Development of Morocco",
      "roles": [
        "funder"
      ]
    }
  ]
}
```
````

`````


(economic-and-fiscal-budget-for-preparation-implementation-and-operation)=

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
Project level:

1. Get the `BudgetBreakdowns` object in the `budget.budgetBreakdowns` array that represents the budget breakdown by stage. If none exists yet:

- Add a `BudgetBreakdowns` object to the `budget.budgetBreakdowns` array.

2. Set it's `.id` incrementally and it's `.description` to "Breakdown by stage".

3. Get the `BudgetBreakdown` object in the budget breakdowns object for each of the 3 stages. If none exists yet:

- Add 3 `BudgetBreakdown` objects to the `budget.budgetBreakdowns.budgetBreakdown` array. For each object:
- Set the `.id` incrementally.
- Set the `.description` to the stage name - "Preparation", "Implementation" or "Operation". If the funding source is not known for a stage note append "funding/budget amount not allocated" to the `.description`.

4. For each stage, map the amount and currency to the budget breakdown's `.amount`
```json
{
  "budget": {
    "budgetBreakdowns": [
      {
        "id": "1",
        "description": "Breakdown by stage",
        "budgetBreakdown": [
          {
            "id": "1",
            "description": "Preparation",
            "amount": {
              "amount": 350000,
              "currency": "USD"
            }
          },
          {
            "id": "2",
            "description": "Implementation",
            "amount": {
              "amount": 300000,
              "currency": "USD"
            }
          },
          {
            "id": "3",
            "description": "Operation funding/budget amount not allocated"
          }
        ]
      }
    ]
  }
}
```
````

`````


(economic-and-fiscal-cost-benefit-analysis)=

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


(economic-and-fiscal-value-for-money)=

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


(economic-and-fiscal-budget-projections)=

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
Project level:

1. Add a `BudgetBreakdowns` object to the `budget.budgetBreakdowns` array.

2. Set it's `.id` incrementally and it's `.description` to "Breakdown by year of implementation".

3. For each year of implementation, add a `BudgetBreakdown` object to the `budget.budgetBreakdowns.budgetBreakdown` array. For each object:

- Set the `.id` incrementally.
- Set the `.description` to the year of implementation.

4. For each year, map the amount and currency to the budget breakdown's `.amount`
```json
{
  "budget": {
    "budgetBreakdowns": [
      {
        "id": "1",
        "description": "Breakdown by year of implementation",
        "budgetBreakdown": [
          {
            "id": "1",
            "description": "2024",
            "amount": {
              "amount": 350000,
              "currency": "USD"
            }
          },
          {
            "id": "2",
            "description": "2025",
            "amount": {
              "amount": 300000,
              "currency": "USD"
            }
          }
        ]
      }
    ]
  }
}
```
````

`````


(economic-and-fiscal-budget-shortfall)=

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


(environment-and-climate-environmental-impact-category)=

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

If an environmental impact assessment was conducted:

- Set `.environment.hasImpactAssessment` to `true`.
- Add a `Classification` object to the `.environment.impactCategories` array, set its `.scheme` to "ifc-environmental-social" and set its `.id` to the letter for the category into which the project falls.

If an environmental impact assessment was not conducted, set `environmental.hasImpactAssessment` to `false`.
```json
{
  "environment": {
    "hasImpactAssessment": true,
    "impactCategories": [
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


(environment-and-climate-environmental-measures)=

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


(environment-and-climate-environmental-exceptions)=

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


(environment-and-climate-protected-area)=

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


(environment-and-climate-conservation-measures)=

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


(environment-and-climate-climate-and-disaster-risk-assessment)=

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


(environment-and-climate-climate-measures)=

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


(environment-and-climate-forecast-of-greenhouse-gas-emissions)=

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


(environment-and-climate-environmental-certifications)=

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


(environment-and-climate-decommissioning-plans)=

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


(environment-and-climate-decommissioning-cost-forecast)=

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

1. Add a `CostMeasurement` object to the `.costMeasurements` array and set its:

- `.id` incrementally
- `.date` to the date that the forecast was prepared.

2. Add a `CostGroup` object to the cost measurement's `.costGroups` array, set its `.id` incrementally and set its `.category` to 'endOfLife'
3. Add a `Cost` object to the cost group's `.costs` array, set its `.id` incrementally and map to its `.value`.
```json
{
  "costMeasurements": [
    {
      "id": "1",
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


(climate-finance-climate-objective)=

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
Project level: Add the relevant codes from the environmentalGoal codelist to the `environment.goals` array
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


(climate-finance-financial-instrument)=

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
1. Get the `Finance` object in `.budget.finance` or `.contractingProcesses.summary.finance` that represents the financing arrangement. If none exists yet, [add a financing arrangement](../common.md#add-a-financing-arrangement).
2. Set the the financing arrangement's properties according to the instrument type:

Instrument type | `.assetClass` | `.type`
-- | -- | --
loan | 'debt' | 'loan'
grant | | 'grant'
equity | 'equity' | 'shares.listed' or 'shares.unlisted'
guarantee | | 'guarantee'

3. If the instrument is a concessional loan, set `.concessional` to `true`.
4. If the instrument is a non-concessional loan, set `.concessional` to `false`.
5. If the instrument is results-based, set `.resultsBased` to `true`.
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "assetClass": [
          "debt"
        ],
        "type": "loan",
        "concessional": false,
        "resultsBased": true
      }
    ]
  }
}
```
````

`````


(climate-finance-climate-transformation)=

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


(climate-finance-climate-finance-decision-maker)=

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
Project level: [Add an organization](../common.md#add-an-organization) for the decision maker and add 'climateFinanceFocalPoint' to its `.roles` array.
```json
{
  "parties": [
    {
      "id": "1",
      "name": "Presidential Climate Commission",
      "roles": [
        "climateFinanceFocalPoint"
      ]
    }
  ]
}
```
````

`````


(climate-finance-nationally-determined-contributions-ndc)=

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


(climate-finance-paris-agreement)=

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
````

`````


(climate-finance-beneficiaries)=

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
See [number of beneficiaries (social module)](social-number-of-beneficiaries)
````

`````


(climate-finance-amount-of-investment)=

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
1. Get the `Finance` object in `.budget.finance` or `.contractingProcesses.summary.finance` that represents the financing arrangement. If none exists yet, [add a financing arrangement](../common.md#add-a-financing-arrangement).
2. Map to the financing arrangement's `.value`.
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "value": {
          "amount": 3000000,
          "currency": "EUR"
        }
      }
    ]
  }
}
```
````

`````


(climate-finance-funding-source)=

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
1. Get the `Finance` object in `.budget.finance` or `.contractingProcesses.summary.finance` that represents the financing arrangement. If none exists yet, [add a financing arrangement](../common.md#add-a-financing-arrangement).
2. Map to the financing arrangement's `.source`.
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "source": "Green Climate Fund"
      }
    ]
  }
}
```
````

`````


(climate-finance-green-climate-fund-accredited-entity)=

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
1. Get the `Finance` object in `.budget.finance` or `.contractingProcesses.summary.finance` that represents the financing arrangement. If none exists yet, [add a financing arrangement](../common.md#add-a-financing-arrangement).
2. Get the `Organization` object in `.parties` that represents the party providing the finance. If none exists yet, [add an organization](../common.md#add-an-organization) and add 'funder' to its `.roles`.
3. Set the financing arrangement's `.financingParty` to the `.id` and `.name` of the organization.
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "financingParty": {
          "id": "1",
          "name": "Agency for Agricultural Development of Morocco"
        }
      }
    ]
  },
  "parties": [
    {
      "id": "1",
      "name": "Agency for Agricultural Development of Morocco",
      "roles": [
        "funder"
      ]
    }
  ]
}
```
````

`````


(climate-finance-accredited-entity-type)=

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
1. Get the `Organization` object in `parties` that represents the accredited entity. If none exists yet, [add an organization](../common.md#add-an-organization) and add 'funder' to its `.roles`.
2. Add a `Classification` object to the organization's `.classifications` array, set its `.scheme` to 'costIdsLegalType' and map the organization's legal type ('private', 'public' or 'non-government') to its `.id`.
3. Add a `Classification` object to the organization's `.classifications` array, set its `.scheme` to 'costIdsAdministrativeLevel' and map the organization's administrative level ('international', 'regional', 'national' or 'sub-national') to its `.id`.
```json
{
  "parties": [
    {
      "id": "1",
      "name": "Development Bank of South Africa",
      "roles": [
        "funder"
      ],
      "classifications": [
        {
          "id": "public",
          "scheme": "costIdsLegalType"
        },
        {
          "id": "national",
          "scheme": "costIdsAdministrativeLevel"
        }
      ]
    }
  ]
}
```

````

`````


(climate-finance-project-preparation-costs)=

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
See [Budget for preparation, implementation and operation (economic and fiscal module)](economic-and-fiscal-budget-for-preparation-implementation-and-operation).
````

`````


(climate-finance-project-preparation-period)=

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
Project level: Map to `preparationPeriod`.
```json
{
  "preparationPeriod": {
    "startDate": "2016-07-01T00:00:00Z",
    "endDate": "2016-12-31T00:00:00Z"
  }
}
```
````

`````


(climate-finance-project-approval-period)=

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
Project level:

For each date:

- Add a `Milestone` to the `milestones` array and set its:
  - `.id` incrementally
  - `.type` to 'financing'
  - `.status` to 'met'
- For the submission date, set the milestone's `.title` to "Climate finance submission" and its `.dateMet` to the date of the submission
- For the approval date, set the milestone's `.title` to "Climate finance approval" and its `.dateMet` to the date of the approval.
```json
{
  "milestones": [
    {
      "id": "1",
      "title": "Climate finance submission",
      "type": "financing",
      "dateMet": "2023-06-01T00:00:00Z",
      "status": "met"
    }
  ]
}
```
````

`````


(climate-finance-ratio-of-co-finance)=

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
The OC4IDS data model provides the information needed to calculate co-finance ratios by modelling a project's individual financing arrangements. For more information, see the mappings for [amount of investment](climate-finance-amount-of-investment), [funding source](climate-finance-funding-source), [Green Climate Fund Accredited Entity](climate-finance-green-climate-fund-accredited-entity) and [Accredited Entity Type](climate-finance-accredited-entity-type).
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "source": "Green Climate Fund",
        "value": {
          "amount": 3000000,
          "currency": "USD"
        }
      },
      {
        "id": "2",
        "source": "GEF Trust Fund",
        "value": {
          "amount": 150000,
          "currency": "USD"
        }
      }
    ]
  }
}
```
````

`````


(climate-finance-terms-of-climate-finance)=

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
1. Get the `Finance` object in `.budget.finance` or `.contractingProcesses.summary.finance` that represents the financing arrangement. If none exists yet, [add a financing arrangement](../common.md#add-a-financing-arrangement).
2. Map the terms to the financing arrangement's properties:

- Maturity: `.period`
- Grace period: Map the period over which payments will be made to `.paymentPeriod`. The grace period is the difference between `.period` and `.paymentPeriod`.
- Annual principal repayment years: `.description`
- Interest: `.interestRate`
- Service fee: `.description`
- Commitment fee: `.description`
```json
{
  "budget": {
    "finance": [
      {
        "id": "1",
        "period": {
          "startDate": "2024-01-01T00:00:00Z",
          "endDate": "2043-12-31T00:00:00Z"
        },
        "paymentPeriod": {
          "startDate": "2029-01-01T00:00:00Z",
          "endDate": "2043-12-31T00:00:00Z"
        },
        "interestRate": {
          "margin": 0.0075
        },
        "description": "Annual principal repayment years 11-20 (% of initial principal): 6.7%. Service fee (per annum): 0.50%. Commitment fee (per annum): Up to 0.75%."
      }
    ]
  }
}
```

````

`````


(climate-finance-carbon-efficiency)=

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
Map to `environment.abatementCost`. If supporting documentation is available, [add a project document](../common.md#add-a-project-document) and set `.documentType` to 'abatementCostMethodology'.
```json
{
  "environment": {
    "abatementCost": {
      "amount": 12.29,
      "currency": "USD"
    }
  },
  "documents": [
    {
      "id": "1",
      "documentType": "abatementCostMethodology",
      "url": "http://example.com/abatementCostMethodology.pdf"
    }
  ]
}
```
````

`````


(climate-finance-non-climate-co-benefits)=

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
Project level: For each co-benefit, add a `Benefit` object to the `benefits` array, map the option from the list to its `.title` and map the explanation to its `.description`.
```json
{
  "benefits": [
    {
      "title": "environmental",
      "description": "The new water management plant will mean less water is removed from the delta meaning more is left in place for use by the local biome."
    }
  ]
}
```
````

`````


(climate-finance-public-consultation-meetings)=

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
See [public consultation meetings (social module)](social-public-consultation-meetings).
````

`````


(climate-finance-disbursement-records)=

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


(climate-finance-type-of-project-monitoring)=

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
Project level: Add the relevant codes from the climateOversightTypes codelist to the `environment.climateOversightTypes` array
```json
{
  "environment": {
    "climateOversightTypes": [
      "internal"
    ]
  }
}
```
````

`````


(climate-finance-performance-monitoring)=

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


(climate-finance-reporting-period)=

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


(climate-finance-oversight-reports)=

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

````

`````


(climate-finance-independent-monitoring)=

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
See [independent monitoring (institutional module)](institutional-independent-monitoring).
````

`````


(climate-finance-independent-evaluation)=

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


(climate-finance-impact-measurement)=

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


(climate-finance-carbon-footprint)=

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


(climate-finance-infrastructure-assets-to-be-decommissioned)=

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
For each set of decommissioned assets in a specified location, create a new OC4IDS project and:

1. Set `.type` to 'decommissioning'

2. Set `.title` to the name of the asset

3. Add a `RelatedProject` object to the `.relatedProjects` array and set its:

- `.id` and `.title` to the `.id` and `.title` of the OC4IDS project for the replacement of the asset
- `.scheme` to 'oc4ids'
- `.relationship` to 'replacement'
```json
{
  "id": "oc4ids-bu3kcz-123456789",
  "title": "Otahuhu B Power Station",
  "type": "decommissioning",
  "relatedProjects": [
    {
      "id": "oc4ids-bu3kcz-987654321",
      "scheme": "oc4ids",
      "title": "Otahuhu C Power Station",
      "relationship": "replacement"
    }
  ]
}
```
````

`````


(climate-finance-decommission-period)=

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
Map to `decommissioningPeriod`.
```json
{
  "decommissioningPeriod": {
    "startDate": "2040-07-01T00:00:00Z",
    "endDate": "2041-06-30T00:00:00Z"
  }
}
```
````

`````


(climate-finance-decommission-plan)=

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
````

`````


(climate-finance-carbon-decommission-savings)=

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


(climate-finance-decommission-mitigation-plan)=

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


(social-number-of-beneficiaries)=

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
Project level:

1. Add a `Benefit` object to the `benefits` array.
2. Add a `Beneficiary` object to the benefit's `.beneficiaries` array, set its `.description` to "Direct beneficiaries" and set its `.numberOfPeople` to the number of direct beneficiaries.
3. Add a `Beneficiary` object to the benefit's `.beneficiaries` array, set its `.description` to "Indirect beneficiaries" and set its `.numberOfPeople` to the number of indirect beneficiaries.
```json
{
  "benefits": [
    {
      "beneficiaries": [
        {
          "description": "Direct beneficiaries",
          "numberOfPeople": 1000
        },
        {
          "description": "Indirect beneficiaries",
          "numberOfPeople": 2000
        }
      ]
    }
  ]
}
```
````

`````


(social-inclusive-design-and-implementation)=

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


(social-indigenous-land)=

`````{grid} 2

````{grid-item-card} Indigenous land
:columns: 4
CoST IDS element
^^^
Identify whether the project is located or cut through indigenous land. Use the information at the [LandMark - Global Platform of Indigenous and Community Lands](https://www.landmarkmap.org/) on both databases Indigenous Lands Acknowledged by Government and Not Acknowledged by Government (customary tenure or with formal land claim submitted) to disclose the information.
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project level:

If the project is located in or cuts through indigenous land:

1. Set `.social.inIndigenousLand` to `true`
2. Add a `Location` object to the `.locations` array, set its `.id` incrementally and set its description to "Indigenous land: <Name> (<Category>)" substituting <Name>  and <Category> for the name and land category from the Landmark database.

If the project is not located in or cutting through indigenous land, set `.social.inIndigenousLand` to `false`.
```json
{
  "social": {
    "inIndigenousLand": true
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


(social-public-consultation-meetings)=

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

1. Publish the meeting invite. [Add a project document](../common.md#add-a-project-document) and set its `.documentType` to 'consultationMeetingInvitation'.

2. Publish the meeting details. Add a `Meeting` object to the `.social.consultationMeetings` array and set:

- `.id` incrementally
- `.date` to the date of the meeting
- `.address` to the address of the meeting
- `.numberOfparticipants` to the number of people that participated in the meeting

3. Publish the meeting minutes. [Add a project document](../common.md#add-a-project-document), set its `.documentType` to 'minutes.consultationMeeting'.
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
        "numberOfParticipants": 12
      }
    ]
  },
  "documents": [
    {
      "id": "1",
      "documentType": "consultationMeetingInvitation",
      "url": "http://example.com/consultationMeetingInvitation.pdf"
    },
    {
      "id": "2",
      "documentType": "minutes.consultationMeeting",
      "url": "http://example.com/consultationMeetingMinutes.pdf"
    }
  ]
}
```
````

`````


(social-land-compensation-budget)=

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


(social-labour-obligations)=

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

1. For each labor obligation in the contract, add a code from the [laborObligations](../../reference/codelists.md#laborobligations) codelist to the`.summary.social.laborObligations.obligations` array.
2. Optionally, add a further explanation of the labor obligations to `.summary.social.laborObligations.description`.

Publish the bidding documents that specify labor obligations: [Add a contracting process document](../common.md#add-a-contracting-process-document) and set its `.documentType` to 'biddingDocuments'.

Publish the signed contract that includes labor obligations:  [Add a contracting process document](../common.md#add-a-contracting-process-document) and set its `.documentType` to 'contractSigned'.
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
              "paidOvertime"
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


(social-labour-budget)=

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
Contracting process level: Map to `.summary.social.laborBudget`.
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


(social-workers-accidents)=

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


(social-health-and-safety-certifications)=

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


(social-construction-materials-testing)=

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

Publish a summary of the material tests:

1. For each material test, add a code from the [constructionMaterial](../../reference/codelists.md#constructionmaterial) codelist to the`.social.healthAndSafety.materialTests.tests` array.
2. Add any further explanation of the tests to `.social.healthAndSafety.materialTests.description` including the international or national standards the tests conform to.

Publish test results: For each test result, [Add a project document](../common.md#add-a-project-document) and set `.documentType` to 'materialTestResults'.
```json
{
  "social": {
    "healthAndSafety": {
      "materialTests": {
        "tests": [
          "metal",
          "masonry"
        ],
        "description": "Tests were conducted of the steel frame and masonry of each structure according to ASTM International standards..."
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


(social-building-inspections)=

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


(social-jobs-generated)=

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


(institutional-policy-coherence)=

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


(institutional-freedom-of-information-requests)=

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


(institutional-answers-to-freedom-of-information-requests)=

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


(institutional-lobbying-transparency)=

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

1. Publish the meeting details:
2. Add a `Meeting` object to the `.lobbyingMeetings` array and set:
   \- `.id` incrementally
   \- `.date` to the date of the meeting
   \- `.address` to the address of the meeting
   \- `.numberOfParticipants` to the number of people present at the meeting
   \- `.publicOffice.name` to the name of the person representing the public office present at the meeting
   \- `.publicOffice.jobTitle` to the job title of the person representing the public office present at the meeting
3. Get the `Organization` in `.parties` that represents the public office. If none exists yet, [add an organization](../common.md#add-an-organization).
4. Set the meeting's `.publicOffice.organization` to the `.id` and `.name` of the organization.
5. Publish the meeting minutes. [Add a project document](../common.md#add-a-project-document) and set its `.documentType` to 'minutes.lobbyingMeeting'.
```json
{
  "lobbyingMeetings": [
    {
      "id": "1",
      "date": "2024-01-01T00:00:00Z",
      "address": {
        "streetAddress": "1600 Amphitheatre Pkwy",
        "locality": "London",
        "region": "London",
        "postalCode": "WC1 8HG",
        "countryName": "United Kingdom"
      },
      "numberOfParticipants": 4,
      "publicOffice": {
        "person": {
          "name": "Brett Gliddon"
        },
        "organization": {
          "name": "Motorways UK",
          "id": "GB-GOR-XX1234"
        },
        "jobTitle": "Group General Manager Transport Services"
      }
    }
  ],
  "documents": [
    {
      "id": "2",
      "documentType": "minutes.lobbyingMeeting",
      "url": "http://example.com/lobbyingMeetingMinutes.pdf"
    }
  ]
}
```
````

`````


(institutional-beneficial-ownership)=

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


(institutional-sustainability-criteria)=

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

Add a `Sustainability` object to the `summary.tender.sustainability` array and add 'awardCriteria' to its `.strategies` array.
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
                "awardCriteria"
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


(institutional-anti-corruption-certifications)=

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


(institutional-independent-monitoring)=

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
Project level: [Add an organization](../common.md#add-an-organization) for the independent monitor and add 'independentMonitor' to its `.roles` array.
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


(institutional-performance-monitoring)=

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


(institutional-risk-management-plans)=

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


(institutional-sustainable-sub-sectors)=

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
- Natural resource management:
  flood protection

Free text to add not mentioned sub-sectors
````

````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
Project Level: Map to `sector`, using the \[ProjectSector codelist\]((../../reference/codelists.md#projectsector).
```json
{
  "sector": [
    "solar"
  ]
}
```
````

`````

