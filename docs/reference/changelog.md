# Changelog

## [0.9.2] - 2019-10-25

### Documentation
* Update example file [#146](https://github.com/open-contracting/infrastructure/pull/159/commits/cf162cf2e24f3c0cd4489b9a7ff2089c0e11dd3f) - add 'publicAuthority' role and [#136](https://github.com/open-contracting/infrastructure/pull/159/commits/3b58a49139a72b56e469a8eefa2e688ce68b17fd) -   project identifier prefix.
* Update worked example pages including [#143](https://github.com/open-contracting/infrastructure/pull/159/commits/a199f94982ab720446e668591c8af485f62e33d8) - adding project package, metadata.
* Added guidance for data users page [#143](https://github.com/open-contracting/infrastructure/pull/159/commits/52f955600c5ecde5cb57f3a4a2ebaf73457c86c7).
* Replaced owner with publicAuthority in mapping   [#131](https://github.com/open-contracting/infrastructure/pull/159/commits/30d1e5dddcb328ea4f3092f3ff789a87a6c6ecdc).

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
