import numpy as np
import math
import globalVariables as gV
import thresholdCalculation as tC


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
# function detecting External Electrostatic Potentials - EEP (Potencjały Zewnętrzne Elektrostatyczne - 6.3.1)
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
