from errno import EEXIST
import getpass
import matplotlib.pyplot as plt
import numpy as np
from os import makedirs, path



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
def plotBlock(channels, startPosition, endPosition, step, isArtifactValue, message, resultsPath, channelsNames,
              eegChannelNumber, samplingRate):
    samples = 512

    if samplingRate == 128:
        # x = np.arange(0, step, 1)
        x = np.arange(0, samples, 1)
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


        # ax.plot(x, y.T + 600 * np.arange(18, -1, -1))
        # ax.plot(np.zeros((512, 19)) + 600 * np.arange(18, -1, -1), '--', color='gray')

        # ax.set_xticklabels([int(startPosition/128), int((startPosition + step / 4)/128), int((startPosition + step /
        #                                                                   2)/128),
        # int((startPosition + step * 3 / 4)/128), int(endPosition/128)])

        ax.plot(x, y.T + 600 * np.arange(eegChannelNumber - 1, -1, -1))
        ax.plot(np.zeros((samples, eegChannelNumber)) + 600 * np.arange(eegChannelNumber - 1, -1, -1), '--',
                color='gray')
        ax.set_xticks([0, int(samples / 4), int(samples / 2), int(samples * 3 / 4), samples])
        ax.set_xticklabels([int(startPosition / samplingRate), int((startPosition + step / 4) / samplingRate), int((startPosition +
                                                                                                   step /
                                                                                              2) / samplingRate),
                        int((startPosition + step * 3 / 4) / samplingRate), int(endPosition / samplingRate)])
        ax.set_yticks([])

        ax.legend(channelsNames, loc='upper right', bbox_to_anchor=(1.08, 1), borderaxespad=0, labelspacing=1.8, \
                  title='Channels')

        # saving plot into directory
        fig.savefig(resultsPath + '/plot' + block + '.png')

        plt.rcParams.update({'figure.max_open_warning': 0})

        plt.clf()
        plt.close(fig)


    elif samplingRate == 512:
        # x = np.arange(0, step, 1)
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

        ax.plot(x, y.T + 600 * np.arange(eegChannelNumber - 1, -1, -1))
        ax.plot(np.zeros((step, eegChannelNumber)) + 600 * np.arange(eegChannelNumber - 1, -1, -1), '--',
                    color='gray')
        ax.set_xticks([0, int(step / 4), int(step / 2), int(step * 3 / 4), step])
        ax.set_xticklabels(
                [(startPosition / samplingRate / 4), ((startPosition + step / 4) / samplingRate / 4),
                 ((startPosition +
                                                                                                         step /
                                                                                                         2) /
                 samplingRate / 4),
                 ((startPosition + step * 3 / 4) / samplingRate / 4), (endPosition / samplingRate / 4)])
        ax.set_yticks([])

        ax.legend(channelsNames, loc='upper right', bbox_to_anchor=(1.08, 1), borderaxespad=0, labelspacing=1.8, \
                      title='Channels')

        # saving plot into directory
        fig.savefig(resultsPath + '/plot' + block + '.png')

        plt.rcParams.update({'figure.max_open_warning': 0})

        plt.clf()
        plt.close(fig)

    """elif samplingRate == 512:
    # x = np.arange(0, step, 1)
    x = np.arange(0, samples, 1)

    start = 0
    end = samples
    partCounter = int(step / samplingRate)
    for part in range(partCounter):
        y = channels[:, start:end]

        fig = plt.figure(figsize=(17, 12), dpi=100)

        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], facecolor='none')

        block = str(int(startPosition / step + 1))

        ax.set_title("EEG plot: block " + block + " - part " + str(part + 1), fontsize=14)
        ax.set_xlabel("Time of examination [s]")
        ax.set_ylabel("Signal values in all channels")

        if isArtifactValue:
            for spine in ax.spines.values():
                spine.set_edgecolor('red')

            for axis in ['top', 'bottom', 'left', 'right']:
                ax.spines[axis].set_linewidth(4.0)

        plt.figtext(0.47, 0.96, message, fontsize=14, color='red', ha='center')

        ax.plot(x, y.T + 600 * np.arange(eegChannelNumber - 1, -1, -1))
        ax.plot(np.zeros((samples, eegChannelNumber)) + 600 * np.arange(eegChannelNumber - 1, -1, -1), '--',
                color='gray')
        ax.set_xticks([0, int(samples / 4), int(samples / 2), int(samples * 3 / 4), samples])
        ax.set_xticklabels(
            [(startPosition / samplingRate / 4) + part, ((startPosition + step / 4) / samplingRate / 4) + part,
             ((startPosition +
               step /
               2) /
              samplingRate / 4) + part,
             ((startPosition + step * 3 / 4) / samplingRate / 4) + part, (endPosition / samplingRate / 4) + part])
        ax.set_yticks([])

        ax.legend(channelsNames, loc='upper right', bbox_to_anchor=(1.08, 1), borderaxespad=0, labelspacing=1.8, \
                  title='Channels')

        # saving plot into directory
        fig.savefig(resultsPath + '/plot' + block + '_part' + str(part + 1) + '.png')

        plt.rcParams.update({'figure.max_open_warning': 0})

        plt.clf()
        plt.close(fig)

        start += samples
        end += samples"""



    # plt.show()


# function plotting all blocks of data
# needs improvement, takes too much memory and causes memory error when get range(160)
def plotAllBlocks(resultsPath, inputData, isArtifact, message, examinationTime, samplingRate, channelsNames, eegChannelNumber):
    createDirectory(resultsPath)

    blockNumber = len(isArtifact)
    step = int(examinationTime * samplingRate / blockNumber)
    startPosition = 0
    endPosition = startPosition + step

    # in the future for blockNumber, now for 10
    for i in range(blockNumber):
        if eegChannelNumber == 19:
            arr = np.array(inputData[startPosition:endPosition, 1:20])
        elif eegChannelNumber == 20:
            arr = np.array(inputData[startPosition:endPosition, :])
        channels = np.swapaxes(arr, 0, 1)
        isArtifactValue = isArtifact[i]

        if isArtifactValue:
            plotBlock(channels, startPosition, endPosition, step, isArtifactValue, message, resultsPath,
                      channelsNames, eegChannelNumber, samplingRate)

        startPosition += step
        endPosition += step
