import numpy as np
import matplotlib.pyplot as plt
import artifactDetection
import thresholdCalculation

# loading asc file into numpy array - ndarray
ascArray = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)
print(ascArray)
print("Shape of ascArray: ")
print(ascArray.shape)

print("\n\n")

# loading data from 1 s (128 samples) from channel Fp1 to ndarray
Fp1 = np.array(ascArray[0:165632, 1])
print(Fp1.shape)


print(artifactDetection.detectEEP(Fp1))







"""
# signal plotting
plt.plot(Fp1, linewidth=0.2)
plt.xlabel("Number of samples (number of seconds = number of samples / 128)")
plt.ylabel("Potential value")
plt.show()
"""