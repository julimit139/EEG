import numpy as np
import math
import globalVariables as gV
import thresholdCalculation as tC

# These functions are written for whole examination time and one channel.
# Because every detection function is performed for every EEG channel in examination file,
# there will be one general function dedicated for performing detection functions for every channel (->looping).


# 0th

def performWholeDetection(detectionFunction, inputData):
    for channelNumber in range(gV.eegChannelNumber):
        channel = np.array(inputData[:, channelNumber + 1])
        detectionFunction(channel)


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
            if math.log(abs(xMin), 10) > minThreshold or math.log(xMax, 10) > maxThreshold:
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
