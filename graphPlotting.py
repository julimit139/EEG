import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from errno import EEXIST
from os import makedirs, path
import getpass
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
def plotBlock(channels):
    x = np.arange(0, 512, 1)
    y = channels

    fig = plt.figure(figsize=(17, 12), dpi=100)

    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='none')

    for spine in ax.spines.values():
        spine.set_edgecolor('red')

    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(4.0)

    ax.plot(x, y.T + 800 * np.arange(18, -1, -1))
    ax.plot(np.zeros((512, 19)) + 800 * np.arange(18, -1, -1), '--', color='gray')

    ax.set_title('EEG plot - part n')
    ax.set_xlabel('Time of examination [s]')
    ax.set_ylabel('Signal values in all channels [Hz]')

    ax.set_xticks([0, 128, 256, 384, 512])
    ax.set_xticklabels([0, 1, 2, 3, 4])

    # ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
    # ax.set_yticklabels(gV.channelNames)

    ax.set_yticks([])

    ax.legend(gV.channelNames, loc='upper right', bbox_to_anchor=(1.08, 1), borderaxespad=0, labelspacing=1.8, \
             title='Channels')

    # fig.canvas.manager.window.showMaximized()

    # fig.savefig('{}/plot1.png'.format(directory))

    #rect = patches.Rectangle((-10, -20), 5000, 800, linewidth=3, edgecolor='r', facecolor='none')
    #ax.add_patch(rect)

    plt.show()


# function plotting all blocks of data
# needs improvement, takes too much memory and causes memory error when get range(160)
def plotAllBlocks(inputData):
    startPosition = 0
    endPosition = 512
    step = 512

    # in the future for all data blocks, now for 20
    for i in range(1):
        arr = np.array(inputData[startPosition:endPosition, 1:20])
        channels = np.swapaxes(arr, 0, 1)
        x = np.arange(0, 512, 1)
        y = channels
        fig = plt.figure(figsize=(17, 12), dpi=100)
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot(x, y.T + 800 * np.arange(18, -1, -1))
        ax.plot(np.zeros((512, 19)) + 800 * np.arange(18, -1, -1), '--', color='gray')

        ax.set_title('EEG plot')
        ax.set_xlabel('Time of examination [s]')
        ax.set_ylabel('Signal graphs in all channels')
        ax.set_xticks([0, 128, 256, 384, 512])
        # ax.set_xticklabels([0, 1, 2, 3, 4])
        ax.set_xticklabels([int(startPosition), int(startPosition + step/4), int(startPosition + step/2),
                            int(startPosition + step*3/4), int(endPosition)])
        ax.set_yticks([])
        ax.legend(gV.channelNames, loc='upper right', bbox_to_anchor=(1.08, 1), borderaxespad=0, labelspacing=1.8, \
                  title='Channels')

        # fig.canvas.manager.window.showMaximized()

        # fig.savefig('{}/plot'+str(i)+'.png'.format(directory))
        # fig.savefig(directory + '/plot' + str(i) + '.png')

        plt.rcParams.update({'figure.max_open_warning': 0})
        plt.show()

        startPosition += step
        endPosition += step
