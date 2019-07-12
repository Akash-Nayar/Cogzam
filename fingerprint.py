from collections import defaultdict

def create_database(peaks, uid):

    """
    Create fingerprints from the peaks of the audio to be stored in a database.

    Parameters:
    -----------
    peaks : List[Tuple[int, int]]
        All the peaks in (f, t) form, where f is frequency and t is time.

    uid : String
        id of the song.

    Returns:
    --------
    Fingerprints in to the database
    """

    fan_out = 15
    db = defaultdict(list)
    for i, p in enumerate(peaks):
        for p2 in peaks[i:i+fan_out]:
            try:
                db[(p[0], p2[0], p2[1]-p[1])].append((uid, p[1]))
            except IndexError:
                break
    return db
