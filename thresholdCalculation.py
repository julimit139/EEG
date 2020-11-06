import numpy as np
import statistics
import math


# functions calculating median and standard deviation for calculating thresholds of EEP
def calculateMedian(calcList):
    median = statistics.median(calcList)
    return median


def calculateStandardDeviation(calcList):
    standardDeviation = statistics.stdev(calcList)
    return standardDeviation


# 1st
# function calculating thresholds for External Electrostatic Potentials - EEP (7.5.1)
"""
Calculates thresholds for External Electrostatic Potentials (EEP) detection function.
Called inside the ``detectEEP`` function. 
Parameters:
    minMaxList : list
        List of tuples containing minimum and maximum signal values from each time block of a channel.
Returns:
    thresholds : tuple 
        Tuple containing minimum and maximum thresholds values for channel on which detection function is called. 
"""


def calculateThresholdsEEP(minMaxList):
    # creating lists to contain normalised min and max values from all blocks
    minList = []
    maxList = []

    # iterating through minMaxList and filling minList and maxList with normalised values
    for (xmin, xmax) in minMaxList:
        xMin = xmin.item()
        xMax = xmax.item()
        if xMin != 0 and xMax != 0:
            xMinNorm = math.log(abs(xMin), 10)
            xMaxNorm = math.log(xMax, 10)
            minList.append(xMinNorm)
            maxList.append(xMaxNorm)

    # calculating median values in minList and maxList
    minMedian = calculateMedian(minList)
    maxMedian = calculateMedian(maxList)

    # calculating standard deviation values in minList and maxList
    minStandardDeviation = calculateStandardDeviation(minList)
    maxStandardDeviation = calculateStandardDeviation(maxList)

    # calculating values of minThreshold and maxThreshold
    minThreshold = minMedian + 6 * minStandardDeviation
    maxThreshold = maxMedian + 6 * maxStandardDeviation

    # creating tuple containing threshold values
    thresholds = (minThreshold, maxThreshold)

    # returning thresholds
    return thresholds


