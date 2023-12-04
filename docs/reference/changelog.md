# Changelog

## [0.9.4] - YYYY-MM-DD

### Documentation

* [#344](https://github.com/open-contracting/infrastructure/pull/344) - add implementation models guidance.
* [#343](https://github.com/open-contracting/infrastructure/pull/343) - add Flatten Tool command to implementation guidance.
* [#328](https://github.com/open-contracting/infrastructure/issues/328) - fix reference tables so that "Required" column is correct for arrays (e.g. LinkedRelease.tag  is now correctly marked as "Required")
* [#355](https://github.com/open-contracting/infrastructure/pull/355) - use correct normative and non-normative keywords in documentation.
* [#362](https://github.com/open-contracting/infrastructure/pull/362) - add guidance on publishing in your own language.
* [#371](https://github.com/open-contracting/infrastructure/pull/371) - add link to field level mapping template tutorial.
* [#370](https://github.com/open-contracting/infrastructure/pull/370) - improve schema reference documentation and integrate worked example.
* [#389](https://github.com/open-contracting/infrastructure/pull/389) - emphasize publishing data throughout a project's lifecycle.
* [#422](https://github.com/open-contracting/infrastructure/pull/422), [#425](https://github.com/open-contracting/infrastructure/pull/425) - add CoST IDS sustainability modules to mapping documentation.

### Schema

* [#355](https://github.com/open-contracting/infrastructure/pull/355) - use correct normative and non-normative keywords in schema descriptions.
* [#361](https://github.com/open-contracting/infrastructure/pull/361) - clarify project budget description.
* [#365](https://github.com/open-contracting/infrastructure/pull/365) [#386](https://github.com/open-contracting/infrastructure/pull/386) - add description field to budget.
* [#368](https://github.com/open-contracting/infrastructure/pull/368) - clarify contracting processes id description.
* [#378](https://github.com/open-contracting/infrastructure/pull/378) - clarify semantics of `additionalClassifications`.
* [#450](https://github.com/open-contracting/infrastructure/pull/450) - deprecate `budget.budgetBreakdown` in favor of `budget.budgetBreakdowns`.

* Add fields:
  * [#367](https://github.com/open-contracting/infrastructure/pull/367) - `BudgetBreakdown.approvalDate`
  * [#390](https://github.com/open-contracting/infrastructure/pull/390) - `identifiers`
  * [#427](https://github.com/open-contracting/infrastructure/pull/427) - `parties.beneficialOwners`
  * [#426](https://github.com/open-contracting/infrastructure/pull/426) - `transactions`
  * [#426](https://github.com/open-contracting/infrastructure/pull/426), [#456](https://github.com/open-contracting/infrastructure/pull/456) - `milestones`
  * [#438](https://github.com/open-contracting/infrastructure/pull/438) - `benefits`
  * [#379](https://github.com/open-contracting/infrastructure/pull/379) - `contractingProcesses.summary.tender.datePublished`
  * [#426](https://github.com/open-contracting/infrastructure/pull/426) - `contractingProcesses.summary.milestones`
  * [#433](https://github.com/open-contracting/infrastructure/pull/433) - `contractingProcesses.summary.social`
  * [#432](https://github.com/open-contracting/infrastructure/pull/432):
    * `identificationPeriod`
    * `preparationPeriod`
    * `implementationPeriod`
    * `completionPeriod`
    * `maintenancePeriod`
    * `decommissioningPeriod`
  * [#431](https://github.com/open-contracting/infrastructure/pull/431) - `environment.goals`
  * [#447](https://github.com/open-contracting/infrastructure/pull/447) - `environment.conservationMeasures`
  * [#444](https://github.com/open-contracting/infrastructure/pull/444) - `budget.finance` and `contractingProcesses.summary.finance`
  * [#443](https://github.com/open-contracting/infrastructure/pull/443) - `costMeasurements`
  * [#445](https://github.com/open-contracting/infrastructure/pull/445) - `parties.details.classifications`
  * [#441](https://github.com/open-contracting/infrastructure/pull/441) - `environment.hasImpactAssessment`
  * [#441](https://github.com/open-contracting/infrastructure/pull/441) - `environment.impactCategories`
  * [#442](https://github.com/open-contracting/infrastructure/pull/442) - `environment.abatementCost`
  * [#434](https://github.com/open-contracting/infrastructure/pull/434) - `contractingProcesses.summary.tender.sustainability`
  * [#428](https://github.com/open-contracting/infrastructure/pull/428) - `lobbyingMeetings`
  * [#428](https://github.com/open-contracting/infrastructure/pull/428) - `social.consultationMeetings`
  * [#448](https://github.com/open-contracting/infrastructure/pull/448) - `social.inIndigenousLand`
  * [#448](https://github.com/open-contracting/infrastructure/pull/448) - `social.landCompensationBudget`
  * [#449](https://github.com/open-contracting/infrastructure/pull/449) - `social.healthAndSafety.materialTests`
  * [#455](https://github.com/open-contracting/infrastructure/pull/455) - `environment.inProtectedArea`
  * [#451](https://github.com/open-contracting/infrastructure/pull/451) - `environment.climateOversightTypes`
  * [#457](https://github.com/open-contracting/infrastructure/pull/457) - `environment.climateMeasures`

### Codelists

* [#355](https://github.com/open-contracting/infrastructure/pull/355) - use correct normative and non-normative keywords codelist descriptions.
* [#377](https://github.com/open-contracting/infrastructure/pull/377) - clarify business logic in contractingProcessStatus codelist.
* Add codelists:
  * [#369](https://github.com/open-contracting/infrastructure/pull/369) - classificationScheme
  * [#427](https://github.com/open-contracting/infrastructure/pull/427) - country
  * [#426](https://github.com/open-contracting/infrastructure/pull/426) - milestoneType
  * [#426](https://github.com/open-contracting/infrastructure/pull/426) - milestoneStatus
  * [#426](https://github.com/open-contracting/infrastructure/pull/426) - milestoneCode
  * [#433](https://github.com/open-contracting/infrastructure/pull/433) - laborObligations
  * [#434](https://github.com/open-contracting/infrastructure/pull/434) - sustainabilityStrategy
  * [#431](https://github.com/open-contracting/infrastructure/pull/431) - environmentalGoal
  * [#447](https://github.com/open-contracting/infrastructure/pull/447) - conservationMeasure
  * [#437](https://github.com/open-contracting/infrastructure/pull/437) - policyAlignment
  * [#449](https://github.com/open-contracting/infrastructure/pull/449) - constructionMaterial
  * [#451](https://github.com/open-contracting/infrastructure/pull/451) - climateOversightTypes
  * [#457](https://github.com/open-contracting/infrastructure/pull/457) - climateMeasures
* Add codes:
  * partyRole:
    * [#429](https://github.com/open-contracting/infrastructure/pull/429) - 'climateFinanceFocalPoint'
    * [#439](https://github.com/open-contracting/infrastructure/pull/439) - 'independentMonitor'
  * [#440](https://github.com/open-contracting/infrastructure/pull/440) - projectType: 'decommissioning'
  * [#432](https://github.com/open-contracting/infrastructure/pull/432) - projectStatus:
    * 'maintenance'
    * 'decommissioning'
    * 'decommissioned'
  * [#446](https://github.com/open-contracting/infrastructure/pull/446) - documentType:
    * 'procurementStrategyRiskAssessment'
    * 'lifeCycleCostMethodology'
    * 'costBenefitAnalysis'
    * 'environmentalExemption'
    * 'climateAndDisasterRiskAssessment'
    * 'climateTransformation'
    * 'decommissioningPlans'
    * 'impactMethodology'
    * 'inclusiveDesign'
    * 'inclusiveImplementation'
    * 'supplierEnvironmentalCertification'
    * 'supplierHealthAndSafetyCertification'
    * 'antiCorruptionCertification'
    * 'oversightReport'
    * 'informationRequest'
    * 'informationRequestResponse'
    * 'buildingInspectionReport'
    * 'ghgEmissionsForecast'
    * 'ghgEmissionsReduction'
    * 'ghgEmissions'
  * [#435](https://github.com/open-contracting/infrastructure/pull/435) - projectSector:
    * 'energy.solar'
    * 'energy.wind'
    * 'energy.hydropower'
    * 'energy.biomass'
    * 'energy.geothermal'
    * 'transport.lowCarbon'
    * 'naturalResources'
    * 'naturalResources.floodProtection'
  * [#455](https://github.com/open-contracting/infrastructure/pull/455) - locationGazetteers: 'WDPA'
  * documentType:
    * [#449](https://github.com/open-contracting/infrastructure/pull/449) - 'materialTestResults'
    * [#457](https://github.com/open-contracting/infrastructure/pull/457) - 'climateMeasures'
* [#432](https://github.com/open-contracting/infrastructure/pull/432) - Deprecate 'completed' in favor of 'maintenance' in the projectStatus codelist


### Other

* [#374](https://github.com/open-contracting/infrastructure/pull/374) - add pull request template.
* [#380](https://github.com/open-contracting/infrastructure/pull/380) - update links to OC4IDS Kit.

## [0.9.3] - 2021-10-07

### Documentation

* [#210](https://github.com/open-contracting/infrastructure/issues/210):
  * update the 'Mapping from OCDS' column to reflect the logic used in [convert-to-oc4ids](https://ocdskit.readthedocs.io/en/latest/cli/ocds.html#convert-to-oc4ids).
  * remove references to the PPP profile, reference individual extensions instead.
  * update project identification mapping for sector.
  * replace reference to Budget and projects extension with Projects extension.
  * remove reference to 'publicAuthority' code from OCDS mapping.
* [#216](https://github.com/open-contracting/infrastructure/issues/216) - update CoST IDS & OCDS mapping documentation to separate the OC4IDS to CoST IDS mapping and the OCDS to OC4IDS mapping.
* [#217](https://github.com/open-contracting/infrastructure/issues/217) - remove repeated 'OCDS:' in mapping documentation.
* [#220](https://github.com/open-contracting/infrastructure/issues/220) - add reactive disclosure elements to CoST IDS & OCDS mapping documentation.
* [#246](https://github.com/open-contracting/infrastructure/issues/246) - correct link and wording to Project extension in project identifiers guidance.
* [#268](https://github.com/open-contracting/infrastructure/issues/268), [#269](https://github.com/open-contracting/infrastructure/issues/269) replace 'finalAudit' with 'technicalAuditReport' and 'financialAuditReport' in mapping.
* [#278](https://github.com/open-contracting/infrastructure/issues/278) - add reactive disclosures to worked example.
* [#304](https://github.com/open-contracting/infrastructure/issues/304) - update blank OC4IDS file with schema changes, and add project package.
* [#316](https://github.com/open-contracting/infrastructure/issues/316) - update wording around worked example file, add link to blank.json.
* [#260](https://github.com/open-contracting/infrastructure/pull/260) - improve the clarity of the Getting Started documentation.
* [#329](https://github.com/open-contracting/infrastructure/pull/329) - fix incorrect references to `document.type` in the CoST IDS & OCDS mapping.
* [#339](https://github.com/open-contracting/infrastructure/pull/339) - update link to CoST IDS on mapping page.
* [#382](https://github.com/open-contracting/infrastructure/pull/382) - update email addresses for support.

### Schema

* [#277](https://github.com/open-contracting/infrastructure/issues/277) - add `forecasts` and `metrics`, which can be used to publish implementation progress reports.
* [#317](https://github.com/open-contracting/infrastructure/pull/317) - update fields shared with OCDS for PPPs 1.0.0-beta3 and OCDS 1.1.5.
* [#264](https://github.com/open-contracting/infrastructure/issues/264) - add a field and class for natural persons.
* [#273](https://github.com/open-contracting/infrastructure/issues/273) - add `contractingProcesses/summary/transactions`, which can be used to publish disbursement records.
* [#284](https://github.com/open-contracting/infrastructure/issues/284) - restore `classification/uri` field.
* [#223](https://github.com/open-contracting/infrastructure/issues/223) - add stricter validation rules to catch empty arrays, objects and strings.

### Codelists

* [#317](https://github.com/open-contracting/infrastructure/pull/317) - update codes shared with OCDS for PPPs 1.0.0-beta3 and OCDS 1.1.5.

#### documentType codelist

Changed:

* [#261](https://github.com/open-contracting/infrastructure/issues/261) Update description of 'feasibilityStudy' code to include "project".
* [#267](https://github.com/open-contracting/infrastructure/issues/267) Update description of 'completionCertificate' code to include "project".

Added:

* [#262](https://github.com/open-contracting/infrastructure/issues/262) 'socialImpact'
* [#263](https://github.com/open-contracting/infrastructure/issues/263) 'resettlementPlan'
* [#265](https://github.com/open-contracting/infrastructure/issues/265) 'financialAgreement'
* [#266](https://github.com/open-contracting/infrastructure/issues/266) 'budgetAmendmentApproval'
* [#268](https://github.com/open-contracting/infrastructure/issues/268) 'technicalAuditReport'
* [#269](https://github.com/open-contracting/infrastructure/issues/269) 'financialAuditReport'
* [#271](https://github.com/open-contracting/infrastructure/issues/271) 'escalationApproval'
* [#272](https://github.com/open-contracting/infrastructure/issues/272) 'qualityAssuranceReport'
* [#274](https://github.com/open-contracting/infrastructure/issues/274) 'incorporationCertificate'
* [#275](https://github.com/open-contracting/infrastructure/issues/275) 'contractAmendment'
* [#270](https://github.com/open-contracting/infrastructure/issues/270) 'designReport'
* [#273](https://github.com/open-contracting/infrastructure/issues/273) 'paymentCertificate'

Removed:

* [#269](https://github.com/open-contracting/infrastructure/issues/269) 'finalAudit' (use 'technicalAuditReport' or 'financialAuditReport')
* [#321](https://github.com/open-contracting/infrastructure/issues/269) 'contractSchedule' (use 'contractAnnexe')

## [0.9.2] - 2020-06-29

### Documentation

* [#96](https://github.com/open-contracting/infrastructure/issues/96) - add guidance on providing project identifiers in OCDS data.
* [#120](https://github.com/open-contracting/infrastructure/issues/120) - add list of registered project identifier prefixes to documentation.
* [#124](https://github.com/open-contracting/infrastructure/issues/124) - clarify guidance on project identifier prefixes.
* [#131](https://github.com/open-contracting/infrastructure/issues/131) - replace 'owner' with 'publicAuthority' in mapping.
* [#133](https://github.com/open-contracting/infrastructure/issues/133) - improve clarity of 'what is a project' in getting started section.
* [#136](https://github.com/open-contracting/infrastructure/issues/136) - add project identifier prefix to example file.
* [#143](https://github.com/open-contracting/infrastructure/issues/143) - update worked example page to describe project package, use non-normative keywords, and edit for clarity.
* [#143](https://github.com/open-contracting/infrastructure/issues/143) - add data user guide page.
* [#145](https://github.com/open-contracting/infrastructure/issues/145) - re-order codelist reference page, refer to OCDS and extension documentation for codelists that are shared.
* [#146](https://github.com/open-contracting/infrastructure/issues/146) - add 'publicAuthority' role to example file.
* [#218](https://github.com/open-contracting/infrastructure/pull/218) - add link to CoST guidance note on OGP commitments.
* [#211](https://github.com/open-contracting/infrastructure/issues/211) - update description of 'publicAuthority' role.

### Schema

#### Project package schema

* [#143](https://github.com/open-contracting/infrastructure/issues/143) - update URL in `publicationPolicy` description to reference the data user guide page.
* [#182](https://github.com/open-contracting/infrastructure/issues/182) - update validation properties to enforce minimum length on required string fields and minimum properties on required objects.

#### OC4IDS project schema

* [#127](https://github.com/open-contracting/infrastructure/issues/127) - remove the requirement that linked OCDS releases must be provided in release packages containing only one release. Remove recommendation that OCDS releases are cached from schema and add guidance on caching releases from unreliable sources to implementation guidance.
* [#132](https://github.com/open-contracting/infrastructure/issues/132) - add a publicAuthority organization reference field.
* [#139](https://github.com/open-contracting/infrastructure/issues/139) - update properties of fields in common with OCDS to version [1.1.4](https://standard.open-contracting.org/1.1/en/schema/changelog/#id1).
* [#140](https://github.com/open-contracting/infrastructure/issues/140) - update the description of `project/period` to clarify that this field should be used to provide the planned start and end dates during the preparation phase, for comparison with the actual completion date for the project.
* [#141](https://github.com/open-contracting/infrastructure/issues/141) - clarify that `contractingProcesses/summary/description` is for the contract's *initial* scope of work.
* [#141](https://github.com/open-contracting/infrastructure/issues/141) - remove incorrect guidance about other fields from `contractingProcesses/summary/modifications`.
* [#153](https://github.com/open-contracting/infrastructure/issues/153) - add project/relatedProjects array.
* [#154](https://github.com/open-contracting/infrastructure/issues/154) - add `.requestDate` field to `project/budget` to record the date of the budget request for the project.
* [#156](https://github.com/open-contracting/infrastructure/issues/156) - fix the description of `completion/endDateDetails` to refer to the end date of the *project*, not that of the *contract*.
* [#157](https://github.com/open-contracting/infrastructure/issues/157) - fix spelling and grammar issues.
* [#158](https://github.com/open-contracting/infrastructure/issues/158) - make `contractingProcesses/releases/tag` an array, not a string (bugfix).
* [#160](https://github.com/open-contracting/infrastructure/issues/160) - describe the components of `project/id`, and link to guidance.
* [#161](https://github.com/open-contracting/infrastructure/issues/161) - removed `contractingProcesses/summary/ocid` because it duplicates `contractingProcesses/id`.
* [#182](https://github.com/open-contracting/infrastructure/issues/182) - update validation properties to enforce unique items in arrays and minimum length on required string fields.

### Codelists

* [#139](https://github.com/open-contracting/infrastructure/issues/139) - update codelists in common with OCDS to version [1.1.4](https://standard.open-contracting.org/1.1/en/schema/changelog/#id1).
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

* `sector` - use projectSector open codelist.
* `ContractingProcess` - add required `id` field.
* `LinkedRelease` - make `id` required.
* `variations` - rename to `modifications`.
* `Location` - add required `id` field.

### New codelists

* `projectSector` codelist - add codelist for project sector.

### Codelist updates

* projectStatus codelist - replace 'construction' with 'implementation'.
* variationType codelist - rename to modificationType.
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
