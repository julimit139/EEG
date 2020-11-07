import numpy as np
import matplotlib.pyplot as plt
import artifactDetection as aD
import globalVariables as gV


# loading asc file into numpy array (ndarray) -> it'll load file given through GUI (later: should change '\' into '/')
inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)
print(inputData)
print("Shape of input: ")
print(inputData.shape)
print(inputData.ndim)

print("\n\n")

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


print(aD.performDetection(aD.detectEEP, inputData))





# signal plotting
# col = np.where(Fp1 < 100, 'red', 'green')
# print("Col shape: ")
# print(col.shape)
"""plt.plot(channel, linewidth=0.2)
plt.xlabel("Number of samples")
plt.ylabel("Potential value")
plt.show()"""
