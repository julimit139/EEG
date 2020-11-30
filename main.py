import numpy as np
import artifactDetection as aD
import graphPlotting as gP


inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)

result = aD.performEEPDetection(inputData)
# result = aD.performECGDetection(inputData)
# result = aD.performLFPDetection(inputData)

isArtifact = result[0]
message = result[1]
artifactNumber = isArtifact.count(True)
print(artifactNumber)

isArtifactArray = np.array(isArtifact)
print(np.where(isArtifactArray == True))

gP.plotAllBlocks(inputData, isArtifact, message)













