import numpy as np
import matplotlib.pyplot as plt
import artifactDetection
import thresholdCalculation

# loading asc file into numpy array (ndarray) -> it'll load file given through GUI (later: should change '\' into '/')
inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)
print(inputData)
print("Shape of input: ")
print(inputData.shape)
print(inputData.ndim)

print("\n\n")

# loading data from 1 s from first channel to ndarray (column with index 0 in inputData contains EKG signal)
channel = np.array(inputData[:, 2])
print(channel)
print("Channel shape: ")
print(channel.shape)
print(channel.ndim)


print(artifactDetection.detectEEP(channel))




# signal plotting
# col = np.where(Fp1 < 100, 'red', 'green')
# print("Col shape: ")
# print(col.shape)
"""plt.plot(channel, linewidth=0.2)
plt.xlabel("Number of samples")
plt.ylabel("Potential value")
plt.show()"""
