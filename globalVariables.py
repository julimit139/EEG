# Here are stored global variables describing data being analyzed
# In the future these values will be read from input file directly here
# Header lines in asc file end with spaces


examinationTime = 1294                  # duration of examination (in s)
samplingRate = 128                      # sampling rate used in examination (in Hz)
nyquistFrequency = samplingRate / 2     # Nyquist frequency - half of samplingRate (in Hz)
electricFrequency = 50                  # electric network frequency in Europe (in Hz)
lambdaFrequency = 0.625                 # frequency necessary for detecting LFP artifacts (in Hz)
eegChannelNumber = 20                   # number of EEG channels in examination data
ekgChannelNumber = 1                    # number of EKG channels in examination data

channelNames = ['Fp1-RF', 'Fp2-RF', 'F7-RF', 'F3-RF', 'Fz-RF', 'F4-RF', 'F8-RF', 'T3-RF', 'C3-RF', 'Cz-RF', 'C4-RF',
                'T4-RF', 'T5-RF', 'P3-RF', 'Pz-RF', 'P4-RF', 'T6-RF', 'O1-RF', 'O2-RF']
