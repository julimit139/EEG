# file containing functions extracting necessary data from input file
import numpy as np


def readInputFile(path):
    if path.endswith("asc"):
        inputFile = open(path, "r")
    elif path.endswith("txt"):
        inputFile = open(path, "r", encoding="utf-16")

    content = inputFile.read()
    inputFile.close()

    txtFile = open("Temporal/inputFile.txt", "w")
    txtFile.write(content)
    txtFile.close()


# function extracting sampling rate value from input file
def extractSamplingRate(path):
    samplingRate = ""
    if path.endswith("asc"):
        file = open(path, "r")
    elif path.endswith("txt"):
        file = open(path, "r", encoding="utf-16")

    for i in range(10):
        line = file.readline()
        if "sampling rate" in line.lower():
            for char in line:
                if char.isdigit():
                    samplingRate += char
                elif char == ".":
                    break

    return int(samplingRate)


def extractExaminationTime(path):
    examinationTime = ""
    if path.endswith("asc"):
        file = open(path, "r")
        for i in range(10):
            line = file.readline()
            if "seconds" in line.lower():
                for char in line:
                    if char.isdigit():
                        examinationTime += char

    elif path.endswith("txt"):
        file = open(path, "r", encoding="utf-16")
        for i in range(10):
            line = file.readline()
            if "original file start/end time" in line.lower():
                for char in line:
                    if char.isdigit() or char == "/" or char == ":":
                        examinationTime += char
                    elif char == ".":
                        break

    return int(examinationTime)


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

