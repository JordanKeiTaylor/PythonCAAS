# reads population_settings.json and returns a JSON object
import sys
import json


# prepends a row with labels to the top of the generated population csv
def __addLabelRowToFile(attributes, writer):
    arr = ["Group"]
    arr.extend(attributes)
    arr.append("prefab")
    writer.writerow(arr)


# adds a single row  (defining a single person's attribtues) to population.csv
def __addPersonToFile(groupName, personsAttributes, writer):
    row = [groupName]
    row.extend(personsAttributes)
    writer.writerow(row)


# adds a group to population.csv
def __addGroupToFile(groupName, groupSize, attributeNames, groupAttributeValues, writer, percentpedestrians):
    percentpedestrians = float(percentpedestrians) * .01
    numpedestrians = int(percentpedestrians * groupSize)
    for i in range(groupSize):
        personsAttributes = list(map(lambda name: groupAttributeValues[name][i], attributeNames))
        # append prefab: car or pedestrian
        prefab = "pedestrian" if i < numpedestrians else "car"
        personsAttributes.append(prefab)
        __addPersonToFile(groupName, personsAttributes, writer)


outputFileHelpers = {
    "addLabelRowToFile": __addLabelRowToFile,
    "addPersonToFile": __addPersonToFile,
    "addGroupToFile": __addGroupToFile
}
