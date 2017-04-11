import csv
import numpy as np


def __getInputData(path):
    with open(path, "rt") as csvfile:
        inputdata = []
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            row[0] = float(row[0])
            inputdata.append(row)
    return np.array(inputdata)
