"""borrow-schema.py.

This script takes the full PPP extension schema as a basis (as this includes
most of the elements we need in OC for Infrastructure, and copies definitions
across into the Infrastructure Project Transparency Schema, making
modifications to titles or descriptions where required.

The goal of this is to make it easier to see where changes might be needed in
future to keep Infrastructure Project Transparency Standard aligned with OCDS
object definitions.
"""

import json
from collections import OrderedDict

import requests


base_url = "http://standard.open-contracting.org/profiles/ppp/latest/en/_static/patched/"
schema_folder = "project-level"

def _json_loads(data):
    """
    Loads JSON data, preserving order.
    """
    return json.loads(data, object_pairs_hook=OrderedDict)

def copy_def(definition):
    schema['definitions'][definition] = pppSchema['definitions'][definition]

def copy_codelist(codelist):
    with open(schema_folder + '/codelists/' + codelist + '.csv',"w+") as writeCodelist:
        writeCodelist.write(requests.get(base_url + "codelists/"+codelist+".csv").text)


pppSchema = _json_loads(requests.get(base_url + "release-schema.json").text)

with open(schema_folder + "/project-schema.json","r") as schemaFile:
    schema = _json_loads(schemaFile.read())

copy_def("Identifier")

copy_def("Value")
copy_codelist("currency")

copy_def("Period")
schema['definitions']['Period']['description'] = "Key events during a project or contracting process may have a known start date, end date, duration, or maximum extent (the latest date the period can extend to). In some cases, not all of these fields will have known or relevant values."

copy_def("BudgetBreakdown")


## We need organisations, but not shareholder or beneficial ownership information.
copy_def("Organization")
copy_def("OrganizationReference")
copy_codelist("partyRole")
del(schema['definitions']['Organization']['properties']['shareholders'])
del(schema['definitions']['Organization']['properties']['beneficialOwnership'])
del(schema['definitions']['Organization']['properties']['details'])
schema['definitions']['Organization']['properties']['roles']['description'] = str(schema['definitions']['Organization']['properties']['roles']['description']).replace("contracting process","project")


copy_def("Address")
copy_def("ContactPoint")
schema['definitions']['ContactPoint']['properties']['name']['description'] = str(schema['definitions']['ContactPoint']['properties']['name']['description']).replace("contracting process","project")


copy_def("Document")
schema['definitions']['Document']['properties']['description']['description'] = "Where a link to a full document is provided, the description should provide a 1 - 3 paragraph summary of the information the document contains, and the `pageStart` field should be used to make sure readers can find the correct section of the document containing more information. Where there is no linked document available, the description field may contain all the information required by the current `documentType`. \n\nLine breaks in text (represented in JSON using `\\n\\n`) must be respected by systems displaying this information, and systems may also support basic HTML tags (H1-H6, B, I, U, strong, A and optionally IMG) or [markdown syntax](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for formatting. "
schema['definitions']['Document']['properties']['url']['description'] = "This should be a direct link to the document or web page where the information described by the current documentType exists."
copy_codelist("documentType")


copy_def("Location")
schema['definitions']['Location']['description'] = "The location where activity related to this project will be delivered, or will take place. A location may be described using a geometry (point location, line or polygon), a gazetteer entry, an address, or a combination of these."
schema['definitions']['Location']['properties']['address'] = {
          "title": "Address",
          "description": "A physical address where works will take place.",
          "$ref": "#/definitions/Address"
        }
copy_codelist("geometryType")
copy_codelist("locationGazetteers")


copy_def("Classification")
schema['definitions']['Classification']['properties']['scheme']['description'] = "An classification should be drawn from an existing scheme or list of codes. This field is used to indicate the scheme/codelist from which the classification is drawn."
del(schema['definitions']['Classification']['properties']['scheme']['codelist'])
del(schema['definitions']['Classification']['properties']['scheme']['openCodelist'])
del(schema['definitions']['Classification']['properties']['uri'])

with open(schema_folder + "/project-schema.json","w") as outFile:
    outFile.write(json.dumps(schema,indent=2))
