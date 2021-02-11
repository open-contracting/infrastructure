# Changelog

## [X.X.X] - YYYY-MM-DD

### Documentation

* [#217](https://github.com/open-contracting/infrastructure/issues/217) - remove repeated 'OCDS:' in mapping documentation
* [#268](https://github.com/open-contracting/infrastructure/issues/268), [#269](https://github.com/open-contracting/infrastructure/issues/269) replace 'finalAudit' with 'technicalAuditReport' and 'financialAuditReport' in mapping

### Schema

* [#277](https://github.com/open-contracting/infrastructure/issues/277) - add `forecasts` and `metrics` which can be used to publish implementation progress reports
* [#282](https://github.com/open-contracting/infrastructure/pull/282) - update fields shared with OCDS for PPPs 1.0.0-beta2 and OCDS 1.1.4.

### Codelists

* [#282](https://github.com/open-contracting/infrastructure/pull/282) - update codes shared with OCDS for PPPs 1.0.0-beta2 and OCDS 1.1.4.
* [#264](https://github.com/open-contracting/infrastructure/issues/264) - add a field and class for natural persons.

#### documentType codelist

Changed:

* [#261](https://github.com/open-contracting/infrastructure/issues/261) Update description of 'feasibilityStudy' code to include "project"
* [#267](https://github.com/open-contracting/infrastructure/issues/267) Update description of 'completionCertificate' code to include "project"

Added:

* [#263](https://github.com/open-contracting/infrastructure/issues/263) 'resettlementPlan'
* [#265](https://github.com/open-contracting/infrastructure/issues/265) 'financialAgreement'
* [#266](https://github.com/open-contracting/infrastructure/issues/266) 'budgetAmendmentApproval'
* [#268](https://github.com/open-contracting/infrastructure/issues/268) 'technicalAuditReport'
* [#269](https://github.com/open-contracting/infrastructure/issues/269) 'financialAuditReport'
* [#272](https://github.com/open-contracting/infrastructure/issues/272) 'qualityAssuranceReport'
* [#274](https://github.com/open-contracting/infrastructure/issues/274) 'incorporationCertificate'
* [#275](https://github.com/open-contracting/infrastructure/issues/275) 'contractAmendment'
* [#270](https://github.com/open-contracting/infrastructure/issues/270) 'designReport'

Removed:

* [#268](https://github.com/open-contracting/infrastructure/issues/268) 'finalAudit'

## [0.9.2] - 2020-06-29

### Documentation

* [#96](https://github.com/open-contracting/infrastructure/issues/96) - add guidance on providing project identifiers in OCDS data.
* [#120](https://github.com/open-contracting/infrastructure/issues/120) - add list of registered project identifier prefixes to documentation
* [#124](https://github.com/open-contracting/infrastructure/issues/124) - clarify guidance on project identifier prefixes.
* [#131](https://github.com/open-contracting/infrastructure/issues/131) - replace 'owner' with 'publicAuthority' in mapping.
* [#133](https://github.com/open-contracting/infrastructure/issues/133) - improve clarity of 'what is a project' in getting started section
* [#136](https://github.com/open-contracting/infrastructure/issues/136) - add project identifier prefix to example file.
* [#143](https://github.com/open-contracting/infrastructure/issues/143) - update worked example page to describe project package, use non-normative keywords, and edit for clarity.
* [#143](https://github.com/open-contracting/infrastructure/issues/143) - add data user guide page.
* [#145](https://github.com/open-contracting/infrastructure/issues/145) - re-order codelist reference page, refer to OCDS and extension documentation for codelists that are shared
* [#146](https://github.com/open-contracting/infrastructure/issues/146) - add 'publicAuthority' role to example file.
* [#218](https://github.com/open-contracting/infrastructure/pull/218) - add link to CoST guidance note on OGP commitments
* [#211](https://github.com/open-contracting/infrastructure/issues/211) - update description of 'publicAuthority' role

### Schema

#### Project package schema

* [#143](https://github.com/open-contracting/infrastructure/issues/143) - update URL in `publicationPolicy` description to reference the data user guide page.
* [#182](https://github.com/open-contracting/infrastructure/issues/182) - update validation properties to enforce minimum length on required string fields and minimum properties on required objects.

#### OC4IDS project schema

* [#127](https://github.com/open-contracting/infrastructure/issues/127) - remove the requirement that linked OCDS releases must be provided in release packages containing only one release. Remove recommendation that OCDS releases are cached from schema and add guidance on caching releases from unreliable sources to implementation guidance
* [#132](https://github.com/open-contracting/infrastructure/issues/132) - add a publicAuthority organization reference field  
* [#139](https://github.com/open-contracting/infrastructure/issues/139) - update properties of fields in common with OCDS to version [1.1.4](https://standard.open-contracting.org/1.1/en/schema/changelog/#id1)
* [#140](https://github.com/open-contracting/infrastructure/issues/140) - update the description of `project/period` to clarify that this field should be used to provide the planned start and end dates during the preparation phase, for comparison with the actual completion date for the project.
* [#141](https://github.com/open-contracting/infrastructure/issues/141) - clarify that `contractingProcesses/summary/description` is for the contract's *initial* scope of work
* [#141](https://github.com/open-contracting/infrastructure/issues/141) - remove incorrect guidance about other fields from `contractingProcesses/summary/modifications`
* [#153](https://github.com/open-contracting/infrastructure/issues/153) - add project/relatedProjects array
* [#154](https://github.com/open-contracting/infrastructure/issues/154) - add `.requestDate` field to `project/budget` to record the date of the budget request for the project
* [#156](https://github.com/open-contracting/infrastructure/issues/156) - fix the description of `completion/endDateDetails` to refer to the end date of the *project*, not that of the *contract*
* [#157](https://github.com/open-contracting/infrastructure/issues/157) - fix spelling and grammar issues
* [#158](https://github.com/open-contracting/infrastructure/issues/158) - make `contractingProcesses/releases/tag` an array, not a string (bugfix)
* [#160](https://github.com/open-contracting/infrastructure/issues/160) - describe the components of `project/id`, and link to guidance
* [#161](https://github.com/open-contracting/infrastructure/issues/161) - removed `contractingProcesses/summary/ocid` because it duplicates `contractingProcesses/id`
* [#182](https://github.com/open-contracting/infrastructure/issues/182) - update validation properties to enforce unique items in arrays and minimum length on required string fields.

### Codelists

* [#139](https://github.com/open-contracting/infrastructure/issues/139) - update codelists in common with OCDS to version [1.1.4](https://standard.open-contracting.org/1.1/en/schema/changelog/#id1)
* [#152](https://github.com/open-contracting/infrastructure/issues/152) - add 'expansion' code to projectType codelist.

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
