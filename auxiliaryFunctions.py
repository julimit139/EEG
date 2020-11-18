import statistics
import numpy as np
from scipy.fft import fft
import scipy.integrate as integrate
import globalVariables as gV


# function calculating median for calculating thresholds of EEP
def calculateMedian(calcList):
    median = statistics.median(calcList)
    return median


# function calculating standard deviation for calculating thresholds of EEP
def calculateStandardDeviation(calcList):
    standardDeviation = statistics.stdev(calcList)
    return standardDeviation


# function calculating square modulus of a Fourier Transform array
def calculateSquareModulus(calcList):
    inputData = fft(calcList)
    result = np.abs(inputData)
    result **= 2
    return result


def callAnything(calcList):
    return calcList


def calculateFourier(calcList):
    # squareModulus = calculateSquareModulus(calcList)
    # numerator = integrate.quad(calculateSquareModulus(calcList), 0, gV.lambdaFrequency)
    # denominator = integrate.quad(calculateSquareModulus(calcList), 0, gV.nyquistFrequency) - integrate.quad(calculateSquareModulus(calcList), gV.electricFrequency-2, gV.electricFrequency+2)
    # numerator = integrate.quad(func=callAnything, a=0, b=gV.lambdaFrequency, args=calcList)[0]
    # denominator = integrate.quad(func=callAnything, a=0, b=gV.nyquistFrequency, args=calcList)[0] - integrate.quad(func=callAnything, a=gV.electricFrequency - 2, b=gV.electricFrequency + 2, args=calcList)[0]
    numerator = integrate.simps(calculateSquareModulus(calcList))
    denominator = integrate.simps(calculateSquareModulus(calcList)) - integrate.simps(
        calculateSquareModulus(calcList))
    result = float(numerator / denominator)
    return result
