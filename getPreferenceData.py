import csv
import subprocess
import sys
from OutputFileBuilder.mainFileOutputFunction import addRandomizedPopulationToFile
import os
import argparse


# generates a population from initial settings


def outputPopulationCSV(inputJSONFile, outputFileName):
    with open(outputFileName, "w+") as outputFile:
        writer = csv.writer(outputFile)
        addRandomizedPopulationToFile(writer, inputJSONFile)

# Code that starts process - checks if user has given correct number of command-line arguments

parser = argparse.ArgumentParser(description='Parse input parameters for outputPopulationsCSV')
parser.add_argument("inputJSON")
parser.add_argument("outputPath")
args = parser.parse_args()

outputPopulationCSV(args.inputJSON.split("=")[1], args.outputPath.split("=")[1])
