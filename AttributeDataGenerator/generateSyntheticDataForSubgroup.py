from AttributeDataGenerator.readCSVDataToArray import __getInputData
from AttributeDataGenerator.drawRandomSample import __sampleData
import json


def getSubGroupAttributeData(attributesJSON, groupSize):
        attributesData = {}
        for attribute in attributesJSON:
                distributionFile = attributesJSON[attribute]
                data = __getInputData(distributionFile)
                syntheticData = __sampleData(data, groupSize).flatten().tolist()
                attributesData[attribute] = syntheticData
        return attributesData
