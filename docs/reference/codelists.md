# Codelist reference

Some schema fields refer to codelists, to limit and standardize the possible values of the fields, in order to promote data interoperability.

Codelists can either be open or closed. **Closed codelists** are intended to be comprehensive; for example, the [currency](#currency) codelist covers all currencies in the world. **Open codelists** are intended to be representative, but not comprehensive.

Publishers must use the codes in the codelists, unless no code is appropriate. If no code is appropriate and the codelist is **open**, then a publisher may use a new code outside those in the codelist. If no code is appropriate and the codelist is **closed**, then a publisher should instead create an issue in the [OC4IDS GitHub repository](https://github.com/open-contracting/infrastructure/issues).

```eval_rst
.. admonition:: Extending open codelists
    :class: Tip

    .. markdown::

      If you use new codes outside those in an open codelist, please create an issue in the [OC4IDS GitHub repository](https://github.com/open-contracting/infrastructure/issues), so that the codes can be considered for inclusion in the codelist.

```

For more information on open and closed codelists, refer to the Open Contracting Data Standard [codelists documentation](https://standard.open-contracting.org/1.1/en/schema/codelists/).

## OCDS codelists

OC4IDS reuses some codelists from the Open Contracting Data Standard and its extensions:

* [Currency](https://standard.open-contracting.org/1.1/en/schema/codelists/#currency)
* [Geometry type](https://extensions.open-contracting.org/en/extensions/location/master/codelists/#geometryType.csv)
* [Location gazetteers](https://extensions.open-contracting.org/en/extensions/location/master/codelists/#locationGazetteers.csv)
* [Method](https://standard.open-contracting.org/1.1/en/schema/codelists/#method)
* [Organization identifier scheme](https://standard.open-contracting.org/1.1/en/schema/codelists/#organization-identifier-scheme)
* [Release tag](https://standard.open-contracting.org/1.1/en/schema/codelists/#release-tag)

## Closed codelists

### ContractingProcessStatus

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/contractingProcessStatus.csv
```

### ContractNature

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/contractNature.csv
```

### ProjectStatus

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/projectStatus.csv
```

Projects with a `status` of 'completed' may be displayed in a list of archived projects.

### ProjectType

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/projectType.csv
```

## Open codelists

### DocumentType

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/documentType.csv
```

### ModificationType

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/modificationType.csv
```

### PartyRole

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/partyRole.csv
```

### ProjectSector

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/projectSector.csv
```

### RelatedProject

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/relatedProject.csv
```

### RelatedProjectScheme

```eval_rst
.. codelisttable::
   :header-rows: 1
   :file: ../../build/current_lang/codelists/relatedProjectScheme.csv
```
