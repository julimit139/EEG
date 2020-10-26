import numpy as np
import matplotlib.pyplot as plt


# loading asc file into numpy array - ndarray
ascArray = np.loadtxt("Data/test.asc", skiprows=11)
print(ascArray)
print("Shape of ascArray: ")
print(ascArray.shape)

print("\n\n")

# loading data from 1 s (128 samples) from channel Fp1 to ndarray
Fp1 = np.array(ascArray[:128, 1])
print(Fp1.shape)

# signal plotting
plt.plot(Fp1)
plt.show()