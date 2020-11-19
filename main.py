import numpy as np
import matplotlib.pyplot as plt
import artifactDetection as aD
import globalVariables as gV
import auxiliaryFunctions as aF
import dataExtraction as eD
import graphPlotting as gP


# loading asc file into numpy array (ndarray) -> it'll load file given through GUI (later: should change '\' into '/')
inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)
# print(inputData)
# print("Shape of input: ")
# print(inputData.shape)
# print(inputData.ndim)

channel = np.array(inputData[165504:165632, 1])
print(channel)
print(aF.calculateSquareModulus(channel))
# print(aF.calculateFourier(channel))


print(aD.performDetection(aD.detectEEP, inputData))

channelNames = eD.extractChannelNames("C:/Users/Julia/Desktop/Data/test.asc")

arr = np.array(inputData[165120:165632, 1:20])
channels = np.swapaxes(arr, 0, 1)
print(channels)
print(channels.shape)


"""
x = np.arange(0, 512, 1)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
y = np.array(inputData[165120:165632, 1])
ax.plot(x, y)
ax.set_xlabel('Time of examination [s]')
ax.set_title('EEG')
ax.set_xticks([0, 128, 256, 384, 512])
ax.set_xticklabels([0, 1, 2, 3, 4])
ax.set_yticks([-100, 0, 100])
plt.show()
"""

# creating results directory from its path
resultsDirectory = gP.createPath()
gP.createDirectory(resultsDirectory)

# gP.plotBlock(channels, resultsDirectory)
gP.plotAllBlocks(inputData, resultsDirectory)






# loading data from 1 s from first channel to ndarray (column with index 0 in inputData contains EKG signal)

"""for channelNumber in range(gV.eegChannelNumber):
    if channelNumber == 2:
        continue
    if channelNumber == 14:
        continue
    channel = np.array(inputData[:, channelNumber + 1])
    print("Channel number: ", channelNumber + 1)
    print("Channel: ", channel)
    print("Channel shape and dimensions: ", channel.shape, channel.ndim)
    print(aD.detectEEP(channel))"""


# print(aD.performDetection(aD.detectEEP, inputData))

# output = aD.performECGDetection(aD.detectECG, inputData)
# print(output)
# print(len(output))

# signal plotting
# col = np.where(Fp1 < 100, 'red', 'green')
# print("Col shape: ")
# print(col.shape)
"""plt.plot(channel, linewidth=0.2)
plt.xlabel("Number of samples")
plt.ylabel("Potential value")
plt.show()"""













