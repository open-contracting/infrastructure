# Publishing data in your own language

You can publish the values of free-text fields – like `title`, `description` and `parties/name` – in your own language. You ought to set the `language` field to the language used in these free-text fields. For example:

```json
{
  "id": "1",
  "title": "ตัวอย่างโครงการ",
  "type": "construction",
  "language": "th"
}
```

In order for your data to be interoperable and compatible with OC4IDS tools and methodologies:

* Do not translate codes from codelists. For example, the value of the `type` field needs to be a code from the [ProjectType codelist](../reference/codelists.md#projecttype), like 'construction'. You cannot translate 'construction' to 'การก่อสร้าง':

    ```json
    {
      "id": "incorrect-example-1",
      "type": "การก่อสร้าง",
    }
    ```

* Do not translate field names (object keys). For example, you cannot translate `title` to `ชื่อ`:

    ```json
    {
      "id": "incorrect-example-2",
      "ชื่อ": "ตัวอย่างโครงการ",
    }
    ```

The fields whose values can be translated are listed in the [internationalization lookup table](#internationalization-lookup-table).

## Translating headers in spreadsheets/CSVs

In order to ease access for non-English speakers, instead of using the field *names* as column headers (which are always in English), you can use the field *titles*.

The titles are currently available in English and Spanish. If you would like to translate the titles to your own language, please [contact the OC4IDS Helpdesk](mailto:data@open-contracting.org).

For example, this CSV excerpt uses field titles from the Spanish translation of OC4IDS:

| Identificador o Referencia | Título del Proyecto |
| -------------------------- | ------------------- |
| 1                          | proyecto de ejemplo |

You can use [Flatten Tool](https://flatten-tool.readthedocs.io/en/latest/) to generate files with translated field titles. For example, this command converts the example OC4IDS JSON file to XLSX format, using field titles from the Spanish schema:

```bash
flatten-tool flatten -s https://standard.open-contracting.org/infrastructure/0.9/es/project-schema.json -f xlsx --use-titles --root-id=id --root-list-path=projects example.json
```

## Publishing in multiple languages

To publish data in multiple languages, follow the above guidance and publish a separate [project package](../../reference/package.md) for each language. You need to ensure that the values of `id` fields are consistent across packages, so that users can find the translations of objects.

## Internationalization lookup table

Use the following table to check whether a field can be published in your own language. You can download the table as a {download}`CSV spreadsheet <../_static/i18n.csv>`.

```{csv-table}
:file: ../_static/i18n.csv
:header-rows: 1
```
