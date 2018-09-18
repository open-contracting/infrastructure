

```eval_rst
.. csv-table:: Mapping
   :header-rows: 1

  CoST IDS Element,Guidance note 9 definition,Maps to,Notes
  Project owner,Name of the sponsoring Government department,Project Level: Add a [party]($/Parties) with 'owner' included in its `.roles`.,
  Sector,"Develop a list of sectors relevant to country e.g. housing, transport, energy, water etc.","Project Level: Publish as `sector`, with additional sectors in `additionalClassifications`.",DISCUSSION ON CODELIST
  Subsector,"Develop a subset for each sector e.g. Transport could be subdivided into national highway, local road, railway, port, airport etc.",,DISCUSSION ON CODELIST
  Project name,Specify the project name,Project Level: Publish as `title`,
  Project Location,Briefly specify location of the project,"Project Level: Publish using the `location` fields as an address, geometry (point/line/polygon) or gazetter entry.",
  Purpose,Specify the socio economic purpose of the project,,DISCUSSION QUESTION???
  Project description,Concise description and details of the project,Project Level: Publish in `description`,
  Project Scope (main output),"Main outputs from the project that are being taken forward into construction (type, quantity, unit)","Project Level: Publish as a [document]($/Document), with `.type` set to 'scope' and include a short description and/or a link to a document providing details.",
  Environmental impact,"Briefly describe the environmental impacts and mitigation measures for this project e.g. impacts on flora, fauna & woodlands, areas of natural beauty, carbon emissions etc. and mitigation measures e.g. pollution control, low carbon solutions, sustainable timber etc.","Project Level: Publish as a [document]($/Document), with `.type` set to 'environmentalImpact' and include a short description and/or a link to a document providing details.",
  Land and settlement impact,"State the amount of land and property that was acquired for the project e.g. 25km2 land, and related impacts e.g. archaeological issues (moved saxon burial site), local/indigenous settlements (relocated 5 indigenous villages of 500 villagers each), impacts on local businesses e.g. (30 business properties purchased).","Project Level: Publish as a [document]($/Document), with `.type` set to 'landAndSettlementImpact' and include a short description and/or a link to a document providing details.",
  Contact details,Postal and electronic address of the Project Owner,Project Level: Include `.address` and `.contactPoint` information for the Party with the 'owner' `.role`. ,
  Funding sources,Name the funding organisation(s)/sources of funding,"Project Level: Include each of the funding organisations as a [party]($/Parties) with 'funder' as a `.role`. When information on the amount provided by each funder is available, use `budget/budgetBreakdown` to provide details.",
  Project Budget,"Specify the projected costs/allocated budget for the project (currency and amount). The budget includes land / property acquisition, environmental mitigation measures, H&S provisions, client, consultant & contractor costs, VAT etc.",Project Level: Publish as `budget/amount`.,
  Project budget approval date,Date project budget was authorised,Projet Level: Publish as `budget/approvalDate` and include additional document with `.type` of 'budgetApproval' if required,
  Project status (current),"The current stage of the project. Select from identification, preparation, construction or completed",Project Level: Publish as `status`.,
  Project completion) cost,"State projected or actual completion cost
  (currency and amount)",Project Level: Publish as `completion/finalValue`,
  Completion date,State projected or actual completion date,Project Level: Publish as `completion/endDate`,
  Project Scope at completion (projected),"Indicate projected or actual scope of project. Aim is to show if the completed project scope differs from the original project scope. Specify main outputs (type, quantity, unit)",ProjectLevel: Publish free text as `completion/finalScopeDetails` and/or include document with `.type` of `scope` and dates and descriptions that show this is final scope at completion.,
  Reasons for project changes,"Summary of primary reasons for any changes in scope, time and cost","Project Level: Publish using `completion/endDateDetails`, `completion/finalValueDetails` and `completion/finalScopeDetails`.",
```