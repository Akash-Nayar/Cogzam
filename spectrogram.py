import numpy as np
import matplotlib.mlab as mlab

def spec_creator(sample):
    """
    This function will take in a np.ndarray and compute out a spectogram
    Parameters:
    x: np.ndarray of audio file
    :return:
    array of frequency vs time
    """
    sampling_rate = 44100  # sampling rate in Hz

    S, freqs, times = mlab.specgram(sample, NFFT=4096, Fs=sampling_rate,
                                    window=mlab.window_hanning,
                                    noverlap=int(4096 / 2))
    S = np.clip(S, a_min = 10e-20, a_max = None)
    S = np.log(S)
    return S

