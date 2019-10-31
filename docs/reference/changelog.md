# Changelog

## [0.9.2] - 2019-10-28

### Schema

#### OC4IDS project schema

* [#157](https://github.com/open-contracting/infrastructure/issues/157) - fix spelling and grammar issues
* [#156](https://github.com/open-contracting/infrastructure/issues/156) - fix the description of `completion/endDateDetails` to refer to the end date of the *project*, not that of the *contract*

## [0.9.1] - 2019-06-17

### Changed

* Add changelog.
* Update ocds-babel to 0.1.0.

### Fixed

* Correct schema URLs in schema files.

## [0.9.0-beta] - 2019-03-19

This changelog entry indicates notable changes since the alpha-2 development release of OC4IDS, it is not intended to be a complete list of changes.

In addition to the specific changes to schema and codelists noted below:

* Various refinements and clarifications were made to schema and codelist descriptions.
* Guidance on mapping values from OCDS was moved from the schema to the IDS and OCDS mapping section of the documentation.
* Documentation was expanded and restructured.

### Packaging

* Add [project package schema](https://standard.open-contracting.org/infrastructure/latest/en/reference/package/). OC4IDS data must be published as part of a project package.

### Schema updates

* `sector` - use projectSector open codelist
* `ContractingProcess` - add required `id` field
* `LinkedRelease` - make `id` required
* `variations` - rename to `modifications`
* `Location` - add required `id` field

### New codelists

* `projectSector` codelist - add codelist for project sector

### Codelist updates

* projectStatus codelist - replace 'construction' with 'implementation'
* variationType codelist - rename to modificationType
* partyRole codelist - add OC4IDS codes mentioned in schema and mapping:
  * funder
  * administrativeEntity
* partyRole codelist - add codes from OCDS partyRole codelist:
  * buyer
  * procuringEntity
  * supplier
  * tenderer
* partyRole codelist - remove PPP-specific codes:
  * bidder
  * qualifiedBidder
  * preferredBidder
  * privateParty
  * leadBank
  * lender
  * equityInvestor
  * consortiaMember
  * interestedParty
  * grantor
  * disqualifiedBidder
  * socialWitness
  * otherWitness
  * notary
* documentType codelist - remove PPP-specific codes:
  * financeAdditionality
  * pppModeRationale
  * riskComparison
  * discountRate
  * equityTransferCaps
  * financeArrangements
  * guaranteeReports
  * grants
  * servicePayments
  * landTransfer
  * assetTransfer
  * revenueShare
  * otherGovernmentSupport
  * tariffMethod
  * tariffReview
  * tariffs
  * tariffIllustration
  * handover
  * financialStatement
* documentType codelist - add codes from OCDS documentType codelist:
  * contractNotice
  * completionCertificate
  * procurementPlan
  * biddingDocuments
  * contractArrangements
  * physicalProgressReport
  * financialProgressReport
  * hearingNotice
  * marketStudies
  * eligibilityCriteria
  * clarifications
  * assetAndLiabilityAssessment
  * winningBid
  * complaints
  * contractAnnexe
  * subContract
  * projectPlan
  * billOfQuantity
  * bidders
  * conflictOfInterest
  * debarments
  * illustration
  * submissionDocuments
  * contractSummary
  * cancellationDetails
