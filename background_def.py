

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure
import numpy as np


def back_val_finder(S):
    import numpy as np
    """
    Will take in our log(cks)
    and will solve for our determining value "cutoff"
    for what is background
    ---used in peak_finding_code.py

    Parameters:
          S: our spectrogram from spec_creator

    Returns:
          will return a float value of our cutoff
          """
    N = len(S)
    histo, bino = np.histogram(S, bins=(N // 2), density=True)
    bin1 = bino[0]
    bin2 = bino[1]
    binlen = bin2- bin1 #finds bin length
    cumulative_distr = np.cumsum(binlen * histo)
    bin_edges = bino[:-1]

    bin_index_of_cutoff = np.searchsorted(cumulative_distr, 0.77)

    cutoff_log_amplitude = bin_edges[bin_index_of_cutoff]
