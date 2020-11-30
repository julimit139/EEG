from errno import EEXIST
import getpass
import matplotlib.pyplot as plt
import numpy as np
from os import makedirs, path
import globalVariables as gV


# function creating path to directory for storing program's results (plots)
# might add creating paths on macOS and Linux
def createPath():
    user = getpass.getuser()
    path = "C:/Users/" + user + "/Desktop/Results/"
    return path


# function creating a directory for storing program's results (plots)
def createDirectory(myPath):
    try:
        makedirs(myPath)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(myPath):
            pass
        else:
            raise


# function plotting block of data
def plotBlock(channels, startPosition, endPosition, step, isArtifactValue, message, directory):
    x = np.arange(0, step, 1)
    y = channels

    fig = plt.figure(figsize=(17, 12), dpi=100)

    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='none')

    block = str(int(startPosition / step + 1))
    ax.set_title("EEG plot: block " + block, fontsize=14)
    ax.set_xlabel("Time of examination [s]")
    ax.set_ylabel("Signal values in all channels")

    if isArtifactValue:
        for spine in ax.spines.values():
            spine.set_edgecolor('red')

        for axis in ['top', 'bottom', 'left', 'right']:
            ax.spines[axis].set_linewidth(4.0)

    plt.figtext(0.47, 0.96, message, fontsize=14, color='red', ha='center')

    ax.plot(x, y.T + 600 * np.arange(18, -1, -1))
    ax.plot(np.zeros((512, 19)) + 600 * np.arange(18, -1, -1), '--', color='gray')

    ax.set_xticks([0, int(step / 4), int(step / 2), int(step * 3 / 4), step])
    ax.set_xticklabels([int(startPosition/128), int((startPosition + step / 4)/128), int((startPosition + step /
                                                                                          2)/128),
                int((startPosition + step * 3 / 4)/128), int(endPosition/128)])

    ax.set_yticks([])

    ax.legend(gV.channelNames, loc='upper right', bbox_to_anchor=(1.08, 1), borderaxespad=0, labelspacing=1.8, \
                title='Channels')

    # showing plot in maximized window
    """fig.canvas.manager.window.showMaximized()"""

    # saving plot into directory
    fig.savefig(directory + '/plot' + block + '.png')

    plt.rcParams.update({'figure.max_open_warning': 0})

    # plt.cla()

    # plt.show()


# function plotting all blocks of data
# needs improvement, takes too much memory and causes memory error when get range(160)
def plotAllBlocks(inputData, isArtifact, message):
    # directory = createPath()
    # createDirectory(directory)

    directory = "../Temporal/Results/"

    blockNumber = len(isArtifact)
    step = int(gV.examinationTime * gV.samplingRate / blockNumber)
    startPosition = 0
    endPosition = startPosition + step

    # in the future for blockNumber, now for 10
    for i in range(blockNumber):
        arr = np.array(inputData[startPosition:endPosition, 1:20])
        channels = np.swapaxes(arr, 0, 1)
        isArtifactValue = isArtifact[i]

        if isArtifactValue:
            plotBlock(channels, startPosition, endPosition, step, isArtifactValue, message, directory)

        startPosition += step
        endPosition += step
