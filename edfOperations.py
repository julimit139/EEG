import numpy as np
import os

# reading edf file
fileName = "C:/Users/Julia/Desktop/Data/KT53.edf"
file = open(fileName, "rb")
fileSize = os.path.getsize(fileName)
# print(fileSize)
edfList = []
for i in range(30000):
    edfList.append(file.read(2))
    print(edfList[i])
file.close()

# arr = np.array(edfList)
arr = str(edfList)
print(len(arr))
file = open("KT53.txt", "wb")
file.write(arr.encode(encoding="ASCII", errors="ignore"))
file.close()
# arr.tofile("KT53.txt")