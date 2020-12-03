import numpy
from numpy import genfromtxt
import artifactDetection as aD
import graphPlotting as gP
import dataExtraction as dE
import globalVariables as gV
from EEGData import *

# cols = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 34, 35)

# inputData = numpy.loadtxt(fname="C:/Users/Julia/Desktop/Data/test.asc", dtype=float, skiprows=11)

# print(inputData)

# inputData = genfromtxt(fname="C:/Users/Julia/Desktop/Data/PD143.txt", encoding="utf-16")

"""lineNumber = 0
informLines = 15
breakLines = 0
with open("C:/Users/Julia/Desktop/Data/PD143.txt", "r", encoding="utf=16") as file:
    for line in file:
        lineNumber += 1
        if "--- BREAK IN DATA ---" in line:
            breakLines += 1
file.close()


dataLines = lineNumber - informLines - breakLines
print("lineNumber: " + str(lineNumber))
print("informLines: " + str(informLines))
print("breakLines: " + str(breakLines))
print("dataLines: " + str(dataLines))



file = open("C:/Users/Julia/Desktop/Data/PD143.txt", "r", encoding="utf=16")
for i in range(informLines):
    garbage = file.readline()


inputData = numpy.zeros(shape=(dataLines, 20))
listCounter = 0

for row in range(dataLines):
    content = file.readline()
    if "--- BREAK IN DATA ---" in content:
        print("--- BREAK IN DATA ---")
        continue

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

    inputData[row] = [res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9], res[10], res[11],
                      res[12], res[13], res[14], res[15], res[16], res[17], res[18], res[19]]

print(inputData)
print(inputData.shape)

file.close()"""

myEEG = EEGData("C:/Users/Julia/Desktop/Data/PD143.txt")
inputData = myEEG.getInputData()
print(inputData)
print(myEEG.getSamplingRate())
print(myEEG.getExaminationTime())
print(myEEG.getChannelsNames())
print(myEEG.getEegChannelNumber())
print(myEEG.getEcgChannelNumber())

myEEG.performEEPDetection()
myEEG.plotAllBlocks()
