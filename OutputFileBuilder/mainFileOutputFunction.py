from SettingsJSONParser.jsonHelpers import JSONhelpers
from OutputFileBuilder.fileConstructionHelpers import outputFileHelpers
from AttributeDataGenerator.generateSyntheticDataForSubgroup import getSubGroupAttributeData

# adds generated population to population.csv


def addRandomizedPopulationToFile(writer, inputJSONFile):
    settings = JSONhelpers[0](inputJSONFile)
    JSONhelpers[1](settings)
    groups, attributes, distributions, size = settings["groupsInPopulation"], settings["attributes"], settings["attributeDistributions"], settings["size"]
    percentpedestrians = settings["pedestrians"]
    outputFileHelpers["addLabelRowToFile"](attributes, writer)
    for group in groups:
        groupSize = int(float(groups[group]) * int(size))
        groupAttributeValues = getSubGroupAttributeData(distributions[group], groupSize)
        outputFileHelpers["addGroupToFile"](group, groupSize, attributes, groupAttributeValues, writer, percentpedestrians)
