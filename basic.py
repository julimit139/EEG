import numpy as np
import mne

# loading asc file into numpy array (ndarray)
ascArr = np.loadtxt("test.asc", skiprows=11)
print(ascArr)

"""
# loading edf+ file into raw data
file = "C:/Users/Julia/Desktop/EDF/test.edf"
data = mne.io.read_raw_edf(file)
raw_data = data.get_data()
info = data.info
channels = data.ch_names
"""