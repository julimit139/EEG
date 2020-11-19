import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fft
import auxiliaryFunctions as aF
import artifactDetection as aD
import globalVariables as gV


inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)
channel = np.array(inputData[:, 1])

for channelNumber in range(gV.eegChannelNumber):
    channel = np.array(inputData[:, channelNumber+1])
    result = aD.detectLFP(channel)
    print("Channel number: " + str(channelNumber+1))
    print(len(result))
    try:
        print(result.index(True))
    except ValueError:
        print("True is not in list")



"""
fourierTransform = fft(channel)

absFourierTransform = np.abs(fourierTransform)

powerSpectrum = np.square(absFourierTransform)

frequency = np.linspace(0, gV.samplingRate/2, len(powerSpectrum))

print(sum(powerSpectrum[0:5]))
"""