# Project Identifiers

## Objectives

This report sets out to address:

* To what extent do CoST Countries already have robust sources of project
identification? What are the opportunities and challenges for robust country level project identification?
* What are the opportunities and challenges for the creation of a global identifier system for infrastructure projects?
* What modifications are needed to OCDS, and to country systems, in order to record contract -> project linkages?

## Introduction

CoST define an infrastructure project as *"the delivery of a set of infrastructure assets in a specified location, generally under a single managing entity (project owner) and budget authority’"* ([CoST, 2013]((http://www.constructiontransparency.org/documentdownload.axd?documentresourceid=31))).

Over its lifetime, a project may go by many different names, and although led by a single managing entity, may involve multiple stakeholders, contractors and agencies. 

> EXAMPLE: Smart Motorways Programme, SMP, SMP M1, SMP M1 JCT 5, Smart Motorways Programme M1 Junction 5  <ToDO: Replace with a real example of multiple ways same project has been named>. 

A unique project identifier is a string that unambiguously identifies a specific project. If stable unique project identifiers are available and widely used within data systems then it may become easier to:

* Identify all the contracts relating to a particular infrastructure project;
* Bring together project and contract level data from different sources;
* Develop a definitive list of active infrastructure projects

In the absence of unique project identifiers: 

* Linking project level and contract level information is a complex, costly and error-prone activity;
* Our understanding of infrastructure project activity is likely to be incomplete and patchy. 

> <TODO> DIAGRAM of linking projects and contracts without project ids, and with project ids

This short paper explores the need for project identifiers, current identifier availability and creation practices, options for the future creation and use of identifiers in OCDS data, and data modelling considerations for OCDS. 

## Key concepts: identifiers and registers

> TODO: Check example and ideally use one with name and identifier and multiple languages. (Ukraine?)

"Smart Motorways Programme" is a **name**. It might be written in different ways at different times (for example, when translated in a country with more than one official language, or when abbreviated to SMP). 

"PRJ08-572062" is an **identifier**. It can only be written in one way. It may belong to an identification scheme that sets out the connection between the identifier and the thing it identifies (e.g. a project). 

Identifiers may be **semantic**, where the letters and numbers that make up the identifier have meaning (for example, in 'PRJ08-572062' PRJ may stand for 'project' and '08' for the year the project started), or identifiers may be **arbitrary** (sometimes called dumb identifiers), where the letters and numbers that make up the identifier carries no meaning. 

A **unique identifier** (UID) identifies a single instance of an entity in the world (e.g. a single project).  

Identifiers may be accompanied by a **register** which stores meta-data about each identifier: linking the identifier to the things it identifies. 

Registers may be **primary** (when they are *the* authoritative source of identification, such as a register of companies), or **secondary** (such as a list of companies involved in construction projects compiled by a particular government agency). 

> For further reading on Identifiers see TODO - ADD BOOK
>
> For further reading on Registers, see https://theodi.org/article/registers-and-collaboration-making-lists-we-can-trust-report/

## Understanding the need

This section explores the need for project identifiers. As our [demonstrator has shown](ADD LINK HERE), it is possible, with manual searching, to identify  contracts that relate to a given infrastructure project. However, in the absence of consistently used unique project identifiers, this process is time-consuming and costly, with a high chance of false positives (contracts being associated with an infrastructure project they do not relate to) and false negatives (contracts related to an infrastructure project being missed). 

### What do we need to identify? 

Identification involves taking an opinionated view of the world and of what matters. For example, the Open Contracting Data Standard introduced the idea of identifying a **contracting process** as opposed to identifying individual tender and award notices - and as a result has made it easier to pull together related information from different stages of the contracting cycle. 

To support use of OCDS in relation to Infrastructure, we are seeking identifiers for **infrastructure projects**. CoST define an infrastructure project as *"the delivery of a set of infrastructure assets in a specified location, generally under a single managing entity (project owner) and budget authority’"* ([CoST, 2013]((http://www.constructiontransparency.org/documentdownload.axd?documentresourceid=31))). An infrastructure project may involve many different contracting processes. 

The clear delineation of an infrastructure project, and the link between projects and contracts is not without challenges. For example, at the 'identification' and 'preparation' stages of a project (as per the CoST Disclosure Note 6) decisions may be taken around a programme of work involving a number of different infrastructure assets, to be delivered in multiple locations. It may only be at the implementation stage that discrete projects emerge: and the scope of projects may also change over time. 

> TODO: DIGRAMS

### How would identifiers support the use of the Open Contracting Data Standard for infrastructure construction transparency?

>> TODO

## Existing practice

### Methodology 

We undertook desk research to look at existing practices of infrastructure project identification and project registries, looking at:

* A sample of CoST member countries: Afghanistan, Tanzania, Costa Rica, Honduras and Ukraine;
* The United Kingdom, based on published OCDS data through the Contracts Finder platform;
* Industry approaches to project identification;
* Academic literature on infrastructure and construction project identification;
* Related project identification processes. 

### Findings from country research

TODO: EDIT 

* I didn't find a really good example of assigning and using project identifiers;
* One good system found in California to generate a ten digit number for project identifiers. Well documented and clear system.
* No evidence of anyone else trying to run an initiative on assigning project identifiers;
* Most countries didn't have a good, complete list of projects;
* Countries might have list of projects managed by one agency, but not across agencies;
* UK has good list of big programmes/projects - but without identifiers 
* Postcode looked like used as an Identifier in Australia. Physical nature of infrastructure gives this advantage. 
* Putting all the data on a map is a common theme in sites we looked at. 
* Budget numbers used as only identifier for a project, or budget number was present in information about a project.
* There are commercial databases out there, but without identifiers.
* Spotted a disparate set of identifiers when searching Contracts Finder with some patterns of information in titles - e.g. Acronymns and numbers. Authorities and agencies come up with their own identifiers.

### Findings from industry practice


### Findings from related initiatives


### Discussion



## OCDS project linkages

What existing fields do we have in OCDS?

What options do we have?




**Do we need an identifier field?**

* Things can be a in titles and descriptions - and discovered?
* ID field is important for **validation**. 








Reflections: 

* Difficult to be certain that you are looking for something. Without identifiers we get both **false positives, and false negatives**. Places a lot of costs on data cleaning. 

**What constitutes a project?**

* Project in major project list?
* Project in national budget?
* Project as single contract for constructing something, and immediately related contracts for planning and designing, checking and assessing construction.
* What do CoST define as a project?

* There might be a significant distinction between programmes and projects (though a programme is called a project in the budget)


**Do we need an identifier field?**

* Things can be a in titles and descriptions - and discovered?
* ID field is important for **validation**. 

**Do we need identifiers?**

* We get 'structured descriptions' in some of the data, but not identifiers. 
* What is wrong with these 'structured descriptions'?

**Do we need global identifiers?**

* There is potential for clash with road numbers etc. 

**What would a central registration system address?**





GEODATA!!


## References

CoST, 2013, [CoST Guidance Note 6: Designing and Disclosure Process](http://www.constructiontransparency.org/documentdownload.axd?documentresourceid=31).