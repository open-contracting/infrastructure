**Related issues**
*Add links to related issues here. Use [keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword) if you want an issue to be automatically closed when the PR is merged.*

**Description**
*If the changes in the PR are not sufficiently explained by the related issues and commit messages, add a description here.*

**Merge checklist**
- [ ] [Log your changes](https://ocds-standard-development-handbook.readthedocs.io/en/latest/standard/contributing.html#logging-changes)

If there are changes to `project-schema.json` or `project-package-schema.json`:

- [ ] Update the examples:
  - [ ] `docs/examples/example.json`
  - [ ] `docs/examples/blank.json`
- [ ] Run `./manage.py pre-commit` to update `docs/_static/i8n.csv`

If you added a new definition to the schema, update `docs/reference/schema.md`:

- [ ] Add an entry to the components section
- [ ] Update the `:collapse:` parameter of the `jsonschema` directive for any schemas or sub-schemas that reference the new definition 

If you added a new codelist:

  - [ ] Add an entry to `docs/reference/codelists.md`