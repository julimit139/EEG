# Here are stored global variables describing data being analyzed
# In the future these values will be read from input file directly here
# Header lines in asc file end with spaces

"""inputFile = open("C:/Users/Julia/Desktop/Data/test.asc", "r")
for i in range(20):
    line = inputFile.readline()

    if "Seconds" in line:
        examinationTime = ""
        for i in line:
            if i.isdigit():
                examinationTime += i
        print(examinationTime)

    if "Sampling rate" in line:
        samplingRate = ""
        for i in line:
            if i.isdigit():
                samplingRate += i
        print(samplingRate)

    if "EKG" in line:
        pass
"""


examinationTime = 1294                  # duration of examination (in s)
samplingRate = 128                      # sampling rate used in examination (in Hz)
nyquistFrequency = samplingRate / 2     # Nyquist frequency - half of samplingRate (in Hz)
electricFrequency = 50                  # electric network frequency in Europe (in Hz)
lambdaFrequency = 0.625                 # frequency necessary for detecting LFP artifacts (in Hz)
eegChannelNumber = 20                   # number of EEG channels in examination data
ekgChannelNumber = 1                    # number of EKG channels in examination data
