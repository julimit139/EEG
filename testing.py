import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import auxiliaryFunctions as aF
import artifactDetection as aD
import globalVariables as gV



inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)
data = np.array(inputData[165120:165632, 1])
res3 = aF.calculateFourierFunction(data)
print(res3)
print(type(res3))


"""
fourierTransform = fft(channel)

absFourierTransform = np.abs(fourierTransform)

powerSpectrum = np.square(absFourierTransform)

frequency = np.linspace(0, gV.samplingRate/2, len(powerSpectrum))

print(sum(powerSpectrum[0:5]))
"""