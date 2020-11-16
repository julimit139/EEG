import statistics
import globalVariables as gV


# function calculating median for calculating thresholds of EEP
def calculateMedian(calcList):
    median = statistics.median(calcList)
    return median


# function calculating standard deviation for calculating thresholds of EEP
def calculateStandardDeviation(calcList):
    standardDeviation = statistics.stdev(calcList)
    return standardDeviation


def calculateFourierTransforms(calcList):
    pass
