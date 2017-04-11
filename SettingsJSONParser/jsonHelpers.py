# reads population_settings.json and returns a JSON object
import sys
import json
import argparse


def __readDistributionInputJSON(inputJSONFile):
    inputDataString = open(inputJSONFile, "r").read()
    return json.loads(inputDataString)

expectedFields = ["groupsInPopulation","attributes","attributeDistributions","size","pedestrians"]

# performs some simple checks to determine if settings JSON is valid
# (also throws some obvious errors)
def __validateInputJSON(JSON):
    for field in expectedFields:
        if(field not in JSON):
            raise(Exception("JSON file missing required keys"))
    for attribute in JSON["attributes"]:
        for group in list(JSON["groupsInPopulation"].keys()):
            if(attribute not in JSON["attributeDistributions"][group]):
                raise(Exception("A group is missing a preference"))
    return "JSON is valid"


JSONhelpers = [
     __readDistributionInputJSON,
     __validateInputJSON
]
