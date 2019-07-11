def create_fingerprint(peaks, uid):

    """
    Create fingerprints from the peaks of the audio to be stored in a database.

    Parameters:
    -----------
    peaks : List[Tuple[int, int]]
        All the peaks in (f, t) form, where f is frequency and t is time.

    id : String
        id of the song.

    Returns:
    --------
    Fingerprints in to the database
    """

    fan_out = 15
    db = {}
    for i, p in enumerate(peaks):
        for j, p2 in enumerate(peaks[:i+fan_out], i):
            try:
                db[(p[0], j[0], j[1]-p[1])] = (uid, p[1])
            except IndexError:
                break
    print(str(db))
    return db
