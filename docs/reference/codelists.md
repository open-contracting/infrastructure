# Codelist reference

To make data interoperable OC4IDS uses codelists for some fields. There are two kinds of codelist in OC4IDS:

* **Closed codelists** provide mandatory codes, for fields which reference these codelists publishers must only use codes from the list.

* **Open codelists** provide suggested codes, for fields which reference these codelists publishers should use codes from the list but may extend these lists with new codes where the existing codes are insufficient.

```eval_rst
.. admonition:: Extending open codelists
    :class: Tip

    .. markdown::

      If you add codes to an open codelist in your data, create an issue on the [OC4IDS Github](https://github.com/open-contracting/infrastructure) so the codes can be considered for formal inclusion in the codelist.

```

For more information on open and closed codelists, refer to the Open Contracting Data Standard [codelists documentation](http://standard.open-contracting.org/latest/en/schema/codelists/).

## Closed codelists

### ContractingProcessStatus

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/contractingProcessStatus.csv

```

### ContractNature

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/contractNature.csv

```

### Currency

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/currency.csv

```

### GeometryType

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/geometryType.csv

```

### Method

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/method.csv

```

### ProjectStatus

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/projectStatus.csv

```

### ProjectType

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/projectType.csv

```

## Open codelists

### DocumentType

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/documentType.csv

```

### ModificationType

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/modificationType.csv

```

### LocationGazetteers

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/locationGazetteers.csv

```

### PartyRole

```eval_rst

   .. csv-table::
      :header-rows: 1
      :class: codelist-table
      :file: ../../build/current_lang/codelists/partyRole.csv

```

## OCDS codelists

OC4IDS also reuses some codelists from the Open Contracting Data Standard:

* [Release tag](http://standard.open-contracting.org/latest/en/schema/codelists/#release-tag)
* [Organization identifier scheme](http://standard.open-contracting.org/latest/en/schema/codelists/#organization-identifier-scheme)
