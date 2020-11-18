# file containing functions extracting necessary data from input file
import numpy as np


# function extracting sampling rate value from input file
def extractSamplingRate(path):
    samplingRate = ""
    file = open(path, "r")
    if path.endswith("asc"):
        for i in range(10):
            line = file.readline()
            if "Sampling rate" in line:
                for i in line:
                    if i.isdigit():
                        samplingRate += i
    elif path.endswith("txt"):
        for i in range(30):
            line = file.readline()
            if line.find("Sampling Rate") != -1:
                if i.isdigit():
                    samplingRate += 1
    print(samplingRate)
    return samplingRate


# function extracting all channels value from input file (asc of txt)
def extractInputData(path):
    if path.endswith("asc"):
        print("asc")
        inputData = np.loadtxt(path, skiprows=11)
    elif path.endswith("txt"):
        print("txt")
    return inputData


def extractChannelNames(path):
    channelNames = []
    file = open(path, "r")
    if path.endswith("asc"):
        for i in range(15):
            line = file.readline()
            if "EKG" in line:
                result = line.split("\", \"")
                for i in range(len(result)):
                    if i == 0:
                        channelNames.append(result[i].lstrip(" \""))
                    elif i == (len(result)-1):
                        channelNames.append(result[i].rstrip("\"\n"))
                    else:
                        channelNames.append(result[i])
                channelNames.pop(0)
                channelNames.pop()
                print(channelNames)
    return channelNames

