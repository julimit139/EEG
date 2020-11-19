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
def calculateFourierSquareModulus(calcList):
    fourier = fft(calcList)
    fourierModulus = np.abs(fourier)
    fourierSquareModulus = np.square(fourierModulus)
    return fourierSquareModulus


# function calculating Fourier based function value (book: formula 6.3) in one channel in one block
def calculateFourierFunction(calcList):
    powerSpectrum = calculateFourierSquareModulus(calcList)
    frequency = np.linspace(0, gV.samplingRate/2, len(powerSpectrum))

    nominatorLimit = np.where(frequency < gV.lambdaFrequency)
    nominator = sum(powerSpectrum[nominatorLimit])

    denominatorLimitFirst = np.where(frequency < gV.nyquistFrequency)
    denominatorLimitSecond = np.where((frequency > (gV.electricFrequency-2)) & (frequency < (gV.electricFrequency+2)))
    denominator = sum(powerSpectrum[denominatorLimitFirst]) - sum(powerSpectrum[denominatorLimitSecond])

    fourierFunction = nominator / denominator

    return fourierFunction

