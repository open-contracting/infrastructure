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

## Economic and fiscal

`````{grid} 2

````{grid-item-card} Procurement strategy
:columns: 4
CoST IDS element
^^^
Disclose the procurement strategy risk assessment. This tends to be part of the decision-making strategy and likely includes discussions regarding capabilities, the delivery model and the rationale for the risk allocation decision. (E.g. [Document]).

````


````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
**Project Level:** Publish in documents, with `.documentType` set to 'procurementStrategyRiskAssessment' and include a short description and/or a link to a document providing details.

```json
{
 "documents": [
   {
     "id": "1",
     "documentType": "procurementStrategyRiskAssessment",
     "url": "http://example.com/documents/procurementStrategyRiskAssessment.pdf"
   }
 ]
}
```

````

`````

`````{grid} 2

````{grid-item-card} Life cycle cost
:columns: 4
CoST IDS element
^^^
Disclose the life cycle cost of the project, which is the cost of an asset throughout its life cycle while fulfilling the performance requirements (ISO 15686-5:2017) (E.g. [value]). This tends to be part of the appraisal documents.  In this case, manual work will be required to extract the life cycle cost.

````


````{grid-item-card}
:columns: 8
OC4IDS mapping
^^^
**Project Level:** Add a `CostMeasurement` object to the `costMeasurements` array. Set `.date` to the date the analysis was prepared. If the cost measurement was performed as part of the project appraisal, set `.stage` to ‘preConstruction’. Otherwise, choose an appropriate code from the stage codelist. Map to the cost measurement’s `.lifeCycleCost.cost`. 

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

## Environmental and climate

## Climate finance

## Social

## Institutional
