# file containing functions for extracting necessary data from input file
import numpy as np


def checkFile(path):
    if path.endswith("asc"):
        file = open(path, "r")
        line = file.readline()
        file.close()
        if line.startswith("\"GALNT ASCII CONVERTED FILE\""):
            return True
        else:
            return False
    elif path.endswith("txt"):
        try:
            file = open(path, "r", encoding="utf-16")
            line = file.readline()
            file.close()
            if line.startswith("%%%%%"):
                return True
            else:
                return False
        except UnicodeError:
            return False
    else:
        return False


def extractData(path):
    if path.endswith("asc"):
        return extractDataAsc(path)
    elif path.endswith("txt"):
        return extractDataTxt(path)


def extractDataAsc(path):
    inputData = np.loadtxt(path, dtype=float, skiprows=11)
    examinationTime = ""
    samplingRate = ""
    channelsNames = []
    eegChannelNumber = 0
    ecgChannelNumber = 0

    file = open(path, "r")
    for i in range(11):
        line = file.readline()
        if "seconds" in line.lower():
            for char in line:
                if char.isdigit():
                    examinationTime += char
        elif "sampling rate" in line.lower():
            for char in line:
                if char.isdigit():
                    samplingRate += char
                elif char == ".":
                    break
        elif "EKG" in line:
            result = line.split("\", \"")
            eegChannelNumber = len(result)
            for i in range(len(result)):
                channelsNames.append(result[i])
                if "EKG-RF" in result[i]:
                    item = result[i]
                    channelsNames.remove(item)
                    ecgChannelNumber += 1
                    eegChannelNumber -= 1
                elif "MK-RF" in result[i]:
                    item = result[i]
                    channelsNames.remove(item)
                    eegChannelNumber -= 1

    file.close()
    return inputData, int(examinationTime), int(samplingRate), channelsNames, eegChannelNumber, ecgChannelNumber


def extractDataTxt(path):
    inputData = []
    examinationTime = ""
    samplingRate = ""
    channelsNames = ["C3", "C4", "Cz", "F3", "F4", "F7", "F8", "Fz", "Fp1", "Fp2", "O1",
                         "O2", "Oz", "P3", "P4", "T5", "T6", "Pz", "T3", "T4"]
    eegChannelNumber = 20
    ecgChannelNumber = 0

    lineNumber = 0
    informLines = 15
    breakLines = 0
    with open(path, "r", encoding="utf=16") as file:
        for line in file:
            lineNumber += 1
            if "--- BREAK IN DATA ---" in line:
                breakLines += 1
    file.close()

    dataLines = lineNumber - informLines - breakLines
    inputData = np.zeros(shape=(dataLines, eegChannelNumber))
    file = open(path, "r", encoding="utf-16")
    for i in range(informLines):
        line = file.readline()
        if "sampling rate" in line.lower():
            for char in line:
                if char.isdigit():
                    samplingRate += char
                elif char == ".":
                    break

    breakCounter = 0
    for row in range(dataLines + breakLines):
        content = file.readline()
        if "--- BREAK IN DATA ---" in content:
            breakCounter += 1
            continue
        else:
            res = content.split()
            for index in range(4):
                res.pop(0)

            for index in range(42):
                res.pop()

            shortCounter = res.count("SHORT")
            for index in range(shortCounter):
                res.remove("SHORT")

            if "AMPSAT" in res:
                for index in range(20):
                    if res[index] == "AMPSAT":
                        res[index] = 0

            if len(res) != 20:
                print("Length varies!")

            inputData[row - breakCounter] = [res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9],
                                 res[10],
                              res[11],
                              res[12], res[13], res[14], res[15], res[16], res[17], res[18], res[19]]

    file.close()
    examinationTime = int(len(inputData) / int(samplingRate))

    return inputData, int(examinationTime), int(samplingRate), channelsNames, eegChannelNumber, ecgChannelNumber
