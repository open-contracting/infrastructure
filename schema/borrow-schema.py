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

with open(schema_folder + "/schema.json","r") as schemaFile:
    schema = _json_loads(schemaFile.read())

copy_def("Value")
copy_codelist("currency")

copy_def("Period")
schema['definitions']['Period']['description'] = "Key events during a project or contracting process may have a known start date, end date, duration, or maximum extent (the latest date the period can extend to). In some cases, not all of these fields will have known or relevant values."

copy_def("BudgetBreakdown")


copy_def("Organization")
copy_def("OrganizationReference")
copy_codelist("partyRole")

copy_def("Address")
copy_def("ContactPoint")

copy_def("Document")
copy_codelist("documentType")

copy_def("Location")
schema['definitions']['Location']['description'] = "The location where activity related to this project will be delivered, or will take place. A location can be described by either a geometry (point location, line or polygon), or a gazetteer entry, or both."
copy_codelist("geometryType")
copy_codelist("locationGazetteers")


copy_def("Classification")
schema['definitions']['Classification']['properties']['scheme']['description'] = "An classification should be drawn from an existing scheme or list of codes. This field is used to indicate the scheme/codelist from which the classification is drawn."
del(schema['definitions']['Classification']['properties']['scheme']['codelist'])
del(schema['definitions']['Classification']['properties']['scheme']['openCodelist'])

with open(schema_folder + "/schema.json","w") as outFile:
    outFile.write(json.dumps(schema,indent=2))


