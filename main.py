import numpy as np
import os

# reading edf file
fileName = "C:/Users/Julia/Desktop/EDF/KT53.edf"
file = open(fileName, "rb")
fileSize = os.path.getsize(fileName)
# print(fileSize)
edfList = []
for i in range(30000):
    edfList.append(file.read(1))
    print(edfList[i])
file.close()

arr = np.array(edfList)
print(arr)
file = open("Data/KT53.txt", "wb")
file.write(arr)
file.close()