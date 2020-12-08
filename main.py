from EEGData import *

EEG = EEGData("C:/Users/Julia/Desktop/Data/PD143.txt")
EEG.performEEPDetection()
EEG.plotAllBlocks()
