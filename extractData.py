# file containing functions extracting necessary data from input file

import numpy as np

def extractSamplingRate(path):
    samplingRate = ""
    file = open(path, "r")
    for i in range(30):
        line = file.readline()
        if "Sampling rate" in line:
            for i in line:
                if i.isdigit():
                    samplingRate += i
            print(samplingRate)


def extractInputData(path):
    inputData = np.loadtxt(path, skiprows=11)
    return inputData
