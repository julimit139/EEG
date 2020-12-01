import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import auxiliaryFunctions as aF
# import artifactDetection as aD
import globalVariables as gV
import dataExtraction as dE
import math

from TMPartifactDetection import *

"""pathAsc = "C:/Users/Julia/Desktop/Data/test.asc"
pathTxt = "C:/Users/Julia/Desktop/Data/PD143.txt"

# dE.readInputFile(path)"""

"""samplingRate = dE.extractExaminationTime(pathAsc)
print(samplingRate)
print(type(samplingRate))

samplingRate = dE.extractSamplingRate(pathTxt)
print(samplingRate)
print(type(samplingRate))"""


class EEGData:
    inputData = []
    examinationTime = 0
    samplingRate = 0
    channelsNames = []
    eegChannelNumber = 0
    ecgChannelNumber = 0
    nyquistFrequency = samplingRate / 2
    electricFrequency = 50
    lambdaFrequency = 0.625

    def __init__(self, path):
        data = dE.extractData(path)
        self.inputData = data[0]
        self.examinationTime = data[1]
        self.samplingRate = data[2]
        self.channelsNames = data[3]
        self.eegChannelNumber = data[4]
        self.ecgChannelNumber = data[5]
        self.nyquistFrequency = int(self.samplingRate / 2)

    def performEEPDetection(self):
        return performEEPDetection(self.inputData, self.eegChannelNumber, self.examinationTime, self.samplingRate)

    def performECGDetection(self):
        return performECGDetection(self.inputData, self.examinationTime, self.samplingRate, self.eegChannelNumber)

    def performLFPDetection(self):
        return performLFPDetection(self.inputData, self.eegChannelNumber, self.examinationTime, self.samplingRate,
                                   self.lambdaFrequency, self.nyquistFrequency, self.electricFrequency)

    def getInputData(self):
        return self.inputData




myEEG = EEGData("C:/Users/Julia/Desktop/Data/test.asc")
print(myEEG.inputData)
print(myEEG.examinationTime)
print(myEEG.samplingRate)
print(myEEG.channelsNames)
print(myEEG.eegChannelNumber)
print(myEEG.ecgChannelNumber)
print(myEEG.nyquistFrequency)

# print(myEEG.performEEPDetection())
# print(myEEG.performECGDetection())
print(myEEG.performLFPDetection())
