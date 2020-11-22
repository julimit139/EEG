import numpy as np
import artifactDetection as aD
import graphPlotting as gP


inputData = np.loadtxt("C:/Users/Julia/Desktop/Data/test.asc", skiprows=11)

result = aD.performEEPDetection(inputData)
isArtifact = result[0]
message = result[1]

gP.plotAllBlocks(inputData, isArtifact, message)













