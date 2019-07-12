from collections import defaultdict

def create_datatbase(peaks):

    """
    Create fingerprints from the peaks of the audio to compare against the database

    Parameters:
    -----------
    peaks : List[Tuple[int, int]]
        All the peaks in (f, t) form, where f is frequency and t is time.

    Returns:
    --------
    List
        list of tuples [tn, (f1, f2, time)]
        tn - time bin in audio sample
        f1/f2 - frequency bins
        time - time difference
    """
    fingerprint = []

    fan_out = 15
    for i, p in enumerate(peaks):
        for p2 in peaks[i:i+fan_out]:
            try:
                fingerprint.append(p[0], p2[0], p2[1]-p[1])
            except IndexError:
                break

    return fingerprint