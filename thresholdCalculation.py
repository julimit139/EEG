import numpy as np
import statistics
import math

# functions calculating median and standard deviation for calculating thresholds of EEP
def calculateMedian(array):
    median = statistics.median(array)
    return median


def calculateStandardDeviation(array):
    standardDeviation = statistics.stdev(array)
    return standardDeviation


# 1st
# function calculating thresholds for External Electrostatic Potentials - EEP (7.5.1)
def calculateThresholdsEEP(minmaxArray):
    minArray = []
    maxArray = []
    for tup in range(len(minmaxArray)):
        xmin, xmax = tup
        xminNorm = math.log(abs(xmin), 10)
        xmaxNorm = math.log((xmax, 10))
        minArray.append(xminNorm)
        maxArray.append(xmaxNorm)

    minMedian = calculateMedian(minArray)
    maxMedian = calculateMedian(maxArray)

    minStandardDeviation = calculateStandardDeviation(minArray)
    maxStandardDeviation = calculateStandardDeviation(maxArray)

    minThreshold = minMedian + 6 * minStandardDeviation
