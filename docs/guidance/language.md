# Publishing data in your own language

You can publish the value of free-text fields, for example `title`, `description` and `parties/name`, in your own language. You ought to set `language` to the language used in free-text fields in your data.

In order for your data to be interoperable and compatible with OC4IDS tools and methodologies, you cannot:

* Translate codes from OC4IDS's codelists, for example the `type` field needs to be set to a code from the [ProjectType codelist](../reference/codelists/#projecttype), like 'construction', which cannot be translated.
* Translate field names (keys), for example, you cannot translate `title` to `ชื่อ`.

## Examples

The following JSON snippet is valid OC4IDS data. `title` can be published in Thai because it is a free-text field:

```json
{
  "id": "1",
  "title": "ตัวอย่างโครงการ",
  "type": "construction"
}
```

The following JSON snippet is not valid because "การก่อสร้าง" is not a valid code from the [ProjectType codelist](../reference/codelists/#projecttype):

```json
{
  "id": "1",
  "title": "ตัวอย่างโครงการ",
  "type": "การก่อสร้าง"
}
```

The following JSON snippet is not valid because "ชื่อ" and "พิมพ์" are not valid field names in OC4IDS:

```json
{
  "id": "1",
  "ชื่อ": "ตัวอย่างโครงการ",
  "พิมพ์": "construction"
}
```

## Tabular data

In order to ease access for non-English speakers, you can publish a spreadsheet or CSV file with field and code titles from an OC4IDS translation. Currently, OC4IDS is available in English and Spanish. If you would like to translate the schema to your own language, please [contact the OC4IDS Helpdesk](mailto:data@open-contracting.org).

The following CSV except uses field and code titles from the Spanish translation of OC4IDS:

| Identificador o Referencia | Título del Proyecto | Tipo de proyecto |
| -------------------------- | ------------------- | ---------------- |
| 1                          | proyecto de ejemplo | Construcción     |

You can use [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/) to generate a spreadsheet or CSV file with translated field titles; for example, the following command converts the example OC4IDS JSON file to xlsx format using field titles from the Spanish schema:

```bash
flatten-tool flatten -s https://standard.open-contracting.org/infrastructure/0.9/es/_downloads/f53c05d8f3cfd5c65a3b33cdf80c5079/project-schema.json -f xlsx --use-titles --root-id=id --root-list-path=projects example.json
```