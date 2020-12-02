import numpy as np
from scipy.fft import fft
import statistics
import globalVariables as gV


"""
Calculates median of data given by ``data``. Necessary for performing ``thresholdCalculation/calculateThresholdsEEP`` 
function.
Parameters:
    data : an iterable
        Fragment of EEG examination data stored in an iterable (e.g. a list).
Returns:
    median : float
        Floating point median value.     
"""


def calculateMedian(data):
    median = statistics.median(data)
    return float(median)


"""
Calculates sample standard deviation of data given by ``data``. Necessary for performing 
``thresholdCalculation/calculateThresholdsEEP`` function.
Parameters:
    data : an iterable
        Fragment of EEG examination data stored in an iterable (e.g. a list).
Returns:
    standardDeviation : float
        Floating point standardDeviation value.     
"""


def calculateStandardDeviation(data):
    standardDeviation = statistics.stdev(data)
    return standardDeviation


"""
Calculates discrete Fourier transforms of data given by ``data``, it's absolute value and then it's square value. 
Necessary for performing ``calculateFourierFunction`` function.
Parameters:
    data : ndarray
        Fragment of one channel of EEG examination data.
Returns:
    fourierSquareModulus : ndarray
        Numpy ndarray containing calculated values.     
"""


def calculateFourierSquareModulus(data):
    fourier = fft(data)
    fourierModulus = np.abs(fourier)
    fourierSquareModulus = np.square(fourierModulus)
    return fourierSquareModulus


"""
Calculates value of Fourier-based function on data given by ``data``. Necessary for performing 
``artifactDetection/detectLFP`` function.
Parameters:
    data : ndarray
        Fragment of one channel of EEG examination data.
Returns:
    fourierFunction : float
        Floating point fourierFunction value.     
"""


def calculateFourierFunction(data):
    # ndarray containing calculated power spectrum of given data
    powerSpectrum = calculateFourierSquareModulus(data)

    # calculating frequency values from 0 to half of sampling rate
    # number of frequency values is equal to length of powerSpectrum
    frequency = np.linspace(0, gV.samplingRate/2, len(powerSpectrum))

    # extracting indexes of frequency ndarray where a condition is met
    nominatorLimit = np.where(frequency < gV.lambdaFrequency)

    # calculating sum of powerSpectrum elements with extracted indexes
    nominator = sum(powerSpectrum[nominatorLimit])

    # extracting indexes of frequency ndarray where conditions are met
    denominatorLimitFirst = np.where(frequency < gV.nyquistFrequency)
    denominatorLimitSecond = np.where((frequency > (gV.electricFrequency-2)) & (frequency < (gV.electricFrequency+2)))

    # calculating difference of sums of powerSpectrum elements with extracted indexes
    denominator = sum(powerSpectrum[denominatorLimitFirst]) - sum(powerSpectrum[denominatorLimitSecond])

    # calculating Fourier-based function value
    if nominator == 0:
        fourierFunction = nominator
    else:
        fourierFunction = nominator / denominator


    # returning Fourier-based function value
    return fourierFunction


def sortList(item):
    return len(item)
