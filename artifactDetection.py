import numpy as np
import math
from scipy import stats
import globalVariables as gV
import thresholdCalculation as tC
import auxiliaryFunctions as aF


# 0th
# function performing any detection function in all channels
# performed for whole examination time and all channels
"""
Performs detection function given by ``detectionFunction`` on all channels given by ``inputData``.
Parameters:
    detectionFunction : function
        Detection function which has to be performed on given data.
    inputData : ndarray
        All channels of EEG data.
Returns:
    output : list 
        List of lists of boolean values informing about artifact occurrence in each block of every channel.    
"""


def performDetection(detectionFunction, inputData):
    # creating empty list to contain information about artifact occurrence in each block of every channel
    output = []

    # performing detection function in every channel and appending it's result to output list
    for channelNumber in range(gV.eegChannelNumber):
        channel = np.array(inputData[:, channelNumber + 1])
        output.append(detectionFunction(channel))

    # returning list of lists
    return output


# 1st
# function detecting External Electrostatic Potentials - EEP (Potencjały zewnętrzne elektrostatyczne - 6.3.1)
# performed for whole examination time in one channel
"""
Detects External Electrostatic Potentials (EEP) in channel given by ``channel``.
Parameters:
    channel : ndarray
        EEG channel - one of all EEG channels occurring in examination.
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block.    
"""


def detectEEP(channel):
    # list of tuples containing min and max values for each time block
    minMaxList = []

    # signal is divided into many blocks where each block is 4s long
    blockDuration = 4
    # number of blocks (integer, fractional parts are ignored)
    blockNumber = int(gV.examinationTime / blockDuration)
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they are incremented in the for loop
    startPosition = 0
    endPosition = startPosition + step

    # finding  min and max signal values in each block and filling minMaxList with them
    for i in range(blockNumber):
        xMin = min(channel[startPosition:endPosition])
        xMax = max(channel[startPosition:endPosition])
        minMaxList.append((xMin, xMax))
        startPosition += step
        endPosition += step

    # getting thresholds values from function which calculates them
    thresholds = tC.calculateThresholdsEEP(minMaxList)
    minThreshold = thresholds[0]
    maxThreshold = thresholds[1]

    # creating and filling list with boolean values informing about artifact occurrence in each block
    isArtifact = []
    for (xmin, xmax) in minMaxList:
        xMin = xmin.item()
        xMax = xmax.item()
        if xMin != 0 and xMax != 0:
            if math.log(abs(xMin), 10) > minThreshold or math.log(abs(xMax), 10) > maxThreshold:
                isArtifact.append(True)
            else:
                isArtifact.append(False)
        elif xMin == 0 or xMax == 0:
            if xMin > minThreshold or xMax > maxThreshold:
                isArtifact.append(True)
            else:
                isArtifact.append(False)

    # returning list informing about artifact occurrences
    return isArtifact


# 2nd
# function detecting potentials derived from ECG (Potencjały związane z czynnością elektryczną serca (pochodzące od EKG) - 6.2.3)
# performed for one time block in all channels
"""
Detects potentials derived from ECG in data block given by ``dataBlock``.
Parameters:
    dataBlock : ndarray
        Fragment of inputData of one time block duration and all channels (ECG and EEG).
Returns:
    maxCoefficient : float
        Maximum value in list of coefficients in a time block.
"""


def detectECG(dataBlock):
    # list containing correlation coefficient values for a block time and all channels
    coefficients = []

    # array containing ECG values
    channelECG = np.array(dataBlock[:, 0])

    # calculating correlation coefficient values for all channels
    for channelNumber in range(gV.eegChannelNumber):
        channel = np.array(dataBlock[:, channelNumber + 1])
        coefficient = stats.pearsonr(channelECG, channel)
        coefficients.append(coefficient[0])

    # maximum value in list of coefficients in a time block
    maxCoefficient = max(coefficients)
    return maxCoefficient


# function performing detection function
"""
Performs detection function given by ``detectionFunction`` on whole examination data given by ``inputData``.
Parameters:
    detectionFunction : function
        Detection function which has to be performed on given data.
    inputData : ndarray
        All channels of EEG data.
Returns:
    output : list 
        List of boolean values informing about artifact occurrence in each time block.    
"""


def performECGDetection(detectionFunction, inputData):
    # signal is divided into many blocks where each block is 4s long
    blockDuration = 4
    # number of blocks (integer, fractional parts are ignored)
    blockNumber = int(gV.examinationTime / blockDuration)
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they are incremented in the for loop
    startPosition = 0
    endPosition = startPosition + step

    # getting threshold value from function which calculates it
    threshold = tC.calculateThresholdECG()

    # creating list to contain boolean values informing about artifact occurrence in each block
    isArtifact = []

    # finding correlation coefficient maximum value in each block and all channels
    # and checking if an artifact occurs in a block
    for i in range(blockNumber):
        dataBlock = np.array(inputData[startPosition:endPosition, :])
        maxCoefficient = detectECG(dataBlock)
        if maxCoefficient > threshold:
            isArtifact.append(True)
        else:
            isArtifact.append(False)
        startPosition += step
        endPosition += step

    # returning list informing about artifact occurrences
    return isArtifact


# 3rd
# function detecting low-frequency potentials (Potencjały niskoczęstotliwościowe - 6.1.1)
#       performed for one time block in all channels
"""
Detects low-frequency potentials (LFP) in channel given by ``channel``.
Parameters:
    channel : ndarray
        EEG channel - one of all EEG channels occurring in examination.
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block.    
"""


def detectLFP(channel):
    # list containing Fourier function values for each time block
    fourierList = []

    # signal is divided into many blocks where each block is 4s long
    blockDuration = 4
    # number of blocks (integer, fractional parts are ignored)
    blockNumber = int(gV.examinationTime / blockDuration)
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they are incremented in the for loop
    startPosition = 0
    endPosition = startPosition + step

    # finding Fourier function values in each block and filling fourierList with them
    for i in range(blockNumber):
        fourierValue = aF.calculateFourierFunction(channel[startPosition:endPosition])
        fourierList.append(fourierValue)
        startPosition += step
        endPosition += step

    # getting threshold value from function which calculates it
    threshold = tC.calculateThresholdLFP(fourierList)

    # creating and filling list with boolean values informing about artifact occurrence in each block
    isArtifact = []
    for fourierValue in fourierList:
        if fourierValue > threshold:
            isArtifact.append(True)
        else:
            isArtifact.append(False)

    # returning list informing about artifact occurrences
    return isArtifact

