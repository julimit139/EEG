import math
import numpy as np
from scipy import stats
import auxiliaryFunctions as aF
import globalVariables as gV
import thresholdCalculation as tC


# function detecting External Electrostatic Potentials - EEP (Potencjały zewnętrzne elektrostatyczne - 6.3.1)
# performed for whole examination time in one channel
"""
Detects External Electrostatic Potentials (EEP) in channel given by ``channel``.
Parameters:
    channel : ndarray
        EEG channel - one of all EEG channels occurring in EEG examination data.
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block.    
    blockNumber : int
        Int value informing about number of blocks in a channel data.
"""


def detectEEP(channel):
    # creating empty list for storing tuples containing minimum and maximum channel data values for each time block
    minMaxList = []

    # channel data is divided into many blocks where each block is 4 s long
    blockDuration = 4

    # number of blocks (integer, fractional parts are ignored)
    blockNumber = int(gV.examinationTime / blockDuration)

    # step with which a block of channel data will be extracted
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they are incremented in the for loop
    startPosition = 0
    endPosition = startPosition + step

    # finding minimum and maximum channel data values in each block and filling minMaxList with them
    for block in range(blockNumber):
        xMin = min(channel[startPosition:endPosition])
        xMax = max(channel[startPosition:endPosition])
        minMaxList.append((xMin, xMax))
        startPosition += step
        endPosition += step

    # getting thresholds values for processed channel from function which calculates them
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

    # returning list informing about artifact occurrences and int value informing about number of blocks
    return isArtifact, blockNumber


# performed for whole examination time and all channels
"""
Performs detection function ``detectEEP`` on whole EEG examination data given by ``inputData``.
Parameters:
    inputData : ndarray
        EEG examination data (all channels).
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block of EEG examination data.    
"""


def performEEPDetection(inputData):
    message = "An artifact reflected by the external electrostatic potential occurrence has been detected in this " \
              "block"

    # creating empty list for storing information about artifact occurrence in each block of EEG data
    isArtifactOutput = []

    # performing EEP detection function in every channel and changing isArtifactOutput content respectively
    for channelNumber in range(gV.eegChannelNumber):
        channel = np.array(inputData[:, channelNumber + 1])
        isArtifact = detectEEP(channel)[0]
        blockNumber = detectEEP(channel)[1]

        # filling isArtifactOutput with isArtifact content when iterating outer for loop for the first time
        if channelNumber == 0:
            isArtifactOutput = isArtifact

        # respectively changing or leaving as is the isArtifactOutput content when iterating outer for loop for second
        # and more times
        if channelNumber != 0:
            for block in range(blockNumber):
                if isArtifact[block]:
                    if isArtifactOutput[block] != isArtifact[block]:
                        isArtifactOutput[block] = isArtifact[block]

    # returning list informing about artifact occurrence in each block
    return isArtifactOutput, message


# **********************************************************************************************************************


# function detecting potentials derived from ECG (Potencjały związane z czynnością elektryczną serca - 6.2.3)
# performed for one block in all channels
"""
Detects potentials derived from ECG in data block given by ``dataBlock``.
Parameters:
    dataBlock : ndarray
        Part of EEG examination data of one time block and all examination data channels (ECG and EEG).
Returns:
    maxCoefficient : float
        Maximum value in list of coefficients in a block.
"""


def detectECG(dataBlock):
    # creating empty list fot storing correlation coefficient values for a block time and all channels
    coefficients = []

    # ndarray containing ECG signal values
    channelECG = np.array(dataBlock[:, 0])

    # calculating value of correlation coefficient of the signal in channel with ECG signal for all channels
    for channelNumber in range(gV.eegChannelNumber):
        channel = np.array(dataBlock[:, channelNumber + 1])
        coefficient = stats.pearsonr(channelECG, channel)
        coefficients.append(coefficient[0])

    # maximum value in list of correlation coefficients in a time block
    maxCoefficient = max(coefficients)

    # returning maximum correlation coefficient
    return maxCoefficient


"""
Performs detection function ``detectECG`` on whole EEG examination data given by ``inputData``.
Parameters:
    inputData : ndarray
        EEG examination data (all channels).
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block of EEG examination data.    
"""


def performECGDetection(inputData):
    # creating empty list for storing information about artifact occurrence in each block of EEG data
    isArtifactOutput = []

    # input data is divided into many blocks where each block is 4s long
    blockDuration = 4

    # number of blocks (integer, fractional parts are ignored)
    blockNumber = int(gV.examinationTime / blockDuration)

    # step with which a block of input data will be extracted
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they are incremented in the for loop
    startPosition = 0
    endPosition = startPosition + step

    # getting threshold value from function which calculates it
    threshold = tC.calculateThresholdECG()

    # finding correlation coefficient maximum value in each block and all channels
    # and checking if an artifact occurs in a block
    for block in range(blockNumber):
        dataBlock = np.array(inputData[startPosition:endPosition, :])
        maxCoefficient = detectECG(dataBlock)
        if maxCoefficient > threshold:
            isArtifactOutput.append(True)
        else:
            isArtifactOutput.append(False)
        startPosition += step
        endPosition += step

    # returning list informing about artifact occurrence in each block
    return isArtifactOutput


# *********************************************************************************************************************


# function detecting low-frequency potentials (Potencjały niskoczęstotliwościowe - 6.1.1)
# performed for whole examination time in one channel
"""
Detects low-frequency potentials (LFP) in channel given by ``channel``.
Parameters:
    channel : ndarray
        EEG channel - one of all EEG channels occurring in EEG examination data.
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block.    
    blockNumber : int
        Int value informing about number of blocks in a channel data.
"""


def detectLFP(channel):
    # creating empty list for storing Fourier based function values for each time block
    fourierList = []

    # channel data is divided into many blocks where each block is 4 s long
    blockDuration = 4

    # number of blocks (integer, fractional parts are ignored)
    blockNumber = int(gV.examinationTime / blockDuration)

    # step with which a block of channel data will be extracted
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they are incremented in the for loop
    startPosition = 0
    endPosition = startPosition + step

    # finding Fourier-based function values in each block and filling fourierList with them
    for block in range(blockNumber):
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

    # returning list informing about artifact occurrences and int value informing about number of blocks
    return isArtifact, blockNumber


# performed for whole examination time and all channels
"""
Performs detection function ``detectLFP`` on whole EEG examination data given by ``inputData``.
Parameters:
    inputData : ndarray
        EEG examination data (all channels).
Returns:
    isArtifact : list 
        List of boolean values informing about artifact occurrence in each block of EEG examination data.    
"""


def performLFPDetection(inputData):
    # creating empty list for storing information about artifact occurrence in each block of EEG data
    isArtifactOutput = []

    # performing EEP detection function in every channel and changing isArtifactOutput content respectively
    for channelNumber in range(gV.eegChannelNumber):
        channel = np.array(inputData[:, channelNumber + 1])
        isArtifact = detectLFP(channel)[0]
        blockNumber = detectLFP(channel)[1]

        # filling isArtifactOutput with isArtifact content when iterating outer for loop for the first time
        if channelNumber == 0:
            isArtifactOutput = isArtifact

        # respectively changing or leaving as is the isArtifactOutput content when iterating outer for loop for second
        # and more times
        if channelNumber != 0:
            for block in range(blockNumber):
                if isArtifact[block]:
                    if isArtifactOutput[block] != isArtifact[block]:
                        isArtifactOutput[block] = isArtifact[block]

    # returning list informing about artifact occurrence in each block
    return isArtifactOutput
