import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import auxiliaryFunctions as aF
# import artifactDetection as aD
import globalVariables as gV
import dataExtraction as dE
import math

from TMPartifactDetection import *
from TMPgraphPlotting import *

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
    def __init__(self, path):
        data = dE.extractData(path)
        self.inputData = data[0]
        self.examinationTime = data[1]
        self.samplingRate = data[2]
        self.channelsNames = data[3]
        self.eegChannelNumber = data[4]
        self.ecgChannelNumber = data[5]
        self.nyquistFrequency = int(self.samplingRate / 2)
        self.electricFrequency = 50
        self.lambdaFrequency = 0.625
        self.isArtifactOutput = []
        self.message = ""
        self.resultsPath = ""

    def setIsArtifactOutput(self, isArtifactOutput):
        self.isArtifactOutput = isArtifactOutput

    def setMessage(self, message):
        self.message = message

    def setResultsPath(self):
        self.resultsPath = createPath()

    def getInputData(self):
        return self.inputData

    def getExaminationTime(self):
        return self.examinationTime

    def getSamplingRate(self):
        return self.samplingRate

    def getChannelsNames(self):
        return self.channelsNames

    def getEegChannelNumber(self):
        return self.eegChannelNumber

    def getEcgChannelNumber(self):
        return self.ecgChannelNumber

    def getNyquistFrequency(self):
        return self.nyquistFrequency

    def getElectricFrequency(self):
        return self.electricFrequency

    def getLambdaFrequency(self):
        return self.lambdaFrequency

    def getIsArtifactOutput(self):
        return self.isArtifactOutput

    def getMessage(self):
        return self.message

    def getResultsPath(self):
        return self.resultsPath

    def performEEPDetection(self):
        result = performEEPDetection(self.inputData, self.eegChannelNumber, self.examinationTime, self.samplingRate)
        self.setIsArtifactOutput(result[0])
        self.setMessage(result[1])
        return result

    def performECGDetection(self):
        result = performECGDetection(self.inputData, self.examinationTime, self.samplingRate, self.eegChannelNumber)
        self.setIsArtifactOutput(result[0])
        self.setMessage(result[1])
        return result

    def performLFPDetection(self):
        result = performLFPDetection(self.inputData, self.eegChannelNumber, self.examinationTime, self.samplingRate,
                                   self.lambdaFrequency, self.nyquistFrequency, self.electricFrequency)
        self.setIsArtifactOutput(result[0])
        self.setMessage(result[1])
        return result

    def plotAllBlocks(self):
        self.setResultsPath()
        return plotAllBlocks(self.resultsPath, self.inputData, self.isArtifactOutput, self.message,
                             self.examinationTime,
                             self.samplingRate, self.channelsNames, self.eegChannelNumber)





