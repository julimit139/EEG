import numpy as np
import globalVariables as gV

# Because every detection function is performed for every eeg channel in examination file,
# these functions are written for whole examination time and one channel.
# There will be one general function dedicated for performing these detection functions for every channel (->looping).

#0th
def performDetectionFunction(function):
    for iteration in range(gV.eegChannelNumber):
        function()


# 1st
# function detecting External Electrostatic Potentials - EEP (Potencjały Zewnętrzne Elektrostatyczne - 6.3.1)
# performed for whole examination time in one channel
"""
Detects External Electrostatic Potentials (EEP) in channel given by ``array``.
Parameters:
    array : np.ndarray
        One of EEG channels used in examination.
Returns:
    minmaxArray : list 
        List of tuples containing min and max signal values from each time block of given channel.    
"""
def detectEEP(array):
    # result array of tuples containing min and max values for each block
    minmaxArray = []

    # signal is divided into many blocks where each block is 4s long
    blockDuration = 4
    blockNumber = int(gV.examinationTime / blockDuration)  # number of blocks (integer, fractional parts are ignored)
    step = blockDuration * gV.samplingRate

    # indexes at which a block starts and ends (here: the first block); they'll be incremented in the loop
    startPosition = 0
    endPosition = startPosition + step
    for i in range(blockNumber):
        xmin = min(array[startPosition:endPosition])
        xmax = max(array[startPosition:endPosition])
        minmaxArray.append((xmin, xmax))
        startPosition += step
        endPosition += step
    return minmaxArray

















    result = (xmin, xmax)
    return result