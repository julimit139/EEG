# file containing functions extracting necessary data from input file

def extractSamplingRate(path):
    samplingRate = ""
    file = open(path, "r")
    for i in range(30):
        line = file.readline()
        if "Sampling rate" in line:
            for i in line:
                if i.isdigit():
                    samplingRate += i
            print(samplingRate)

def extraxtChannelValues(file):
    pass
