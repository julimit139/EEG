# file containing functions extracting necessary data from input file
import datetime as dt
import numpy as np
import re
from datetime import datetime


# function uploading input file and saving it's content into Temporal directory
def uploadInputFile(path):
    if path.endswith("asc"):
        inputFile = open(path, "r")
        content = inputFile.read()
        inputFile.close()

        ascFile = open("Temporal/ascFile.txt", "w", encoding="utf-8")
        ascFile.write(content)
        ascFile.close()

    elif path.endswith("txt"):
        inputFile = open(path, "r", encoding="utf-16")
        content = inputFile.read()
        inputFile.close()

        txtFile = open("Temporal/txtFile.txt", "w", encoding="utf-8")
        txtFile.write(content)
        txtFile.close()


# function extracting sampling rate value from input file
def extractSamplingRate(path):
    samplingRate = ""
    file = open(path, "r", encoding="utf-8")

    for i in range(10):
        line = file.readline()
        if "sampling rate" in line.lower():
            for char in line:
                if char.isdigit():
                    samplingRate += char
                elif char == ".":
                    break
            break
    file.close()
    return int(samplingRate)


def extractChannelsNumber(path):
    eegChannelNumber = 0
    ecgChannelNumber = 0
    if "ascFile" in path:
        file = open(path, "r", encoding="utf-8")
        for i in range(15):
            line = file.readline()
            if "EKG" in line:
                result = line.split("\", \"")
                eegChannelNumber = len(result)
                for i in range(len(result)):
                    if "EKG-RF" in result[i]:
                        ecgChannelNumber += 1
                        eegChannelNumber -= 1
                    elif "MK-RF" in result[i]:
                        eegChannelNumber -= 1
                break

    elif "txtFile" in path:
        eegChannelNumber = 23
        ecgChannelNumber = 0

    return eegChannelNumber, ecgChannelNumber


def extractEEGChannelsNames(path):
    channelsNames = []
    if "ascFile" in path:
        file = open(path, "r", encoding="utf-8")
        for i in range(15):
            line = file.readline()
            if "EKG" in line:
                result = line.split("\", \"")
                for i in range(len(result)):
                    channelsNames.append(result[i])
                    if "EKG-RF" in result[i]:
                        item = result[i]
                        channelsNames.remove(item)
                    elif "MK-RF" in result[i]:
                        item = result[i]
                        channelsNames.remove(item)
                break

    elif "txtFile" in path:
        channelsNames = ["C3", "C4", "Cz", "F3", "F4", "F7", "F8", "Fz", "Fp1", "Fp2", "Fps", "A1/M1", "A2/M2", "O1",
                         "O2", "Oz", "P3", "P4", "T5", "T6", "Pz", "T3", "T4"]

    return channelsNames


def extractExaminationTime(path):
    examinationTime = ""
    file = open(path, "r", encoding="utf-8")
    if "ascFile" in path:
        for i in range(10):
            line = file.readline()
            if "seconds" in line.lower():
                for char in line:
                    if char.isdigit():
                        examinationTime += char
                break

    elif "txtFile" in path:
        for i in range(10):
            line = file.readline()
            if "original file start/end time" in line.lower():
                pattern = "(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(20[0-9][0-9])\s(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[" \
          "0-9]|3[0-9]|4[0-9]|5[0-9]):(0[0-9]|1[0-9]|2[" \
          "0-9]|3[0-9]|4[0-9]|5[0-9])\t\t(0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(20[0-9][0-9])\s(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[" \
          "0-9]|3[0-9]|4[0-9]|5[0-9]):(0[0-9]|1[0-9]|2[" \
          "0-9]|3[0-9]|4[0-9]|5[0-9])"
                result = re.search(pattern, line)
                res = result.group()
                start = res[:19]
                end = res[21:]
                startDatetime = datetime.strptime(start, "%m/%d/%Y %H:%M:%S")
                endDatetime = datetime.strptime(end, "%m/%d/%Y %H:%M:%S")
                timeDif = endDatetime - startDatetime
                examinationTime = timeDif.total_seconds()
                break
    return int(examinationTime)


# function extracting all channels value from input file (asc of txt)
def extractInputData(path):
    if "ascFile" in path:
        inputData = np.loadtxt(path, dtype=float, skiprows=11)
    elif "txtFile" in path:
        inputData = np.loadtxt(path, dtype=str, skiprows=15, max_rows=5)
        invalidColumns = np.where(inputData == "SHORT", inputData)
        print(invalidColumns)
    return inputData




