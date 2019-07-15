def populate_db(fingerprints, fingerprintsdb = 'fingerprints.pickle'):

    """
    Populates the database with fingerprints

    Parameters:
    -----------
    fingerprints : dict
        Fingerprints of the peaks of a song
    """

    import pickle

    from collections import defaultdict
    with open(fingerprintsdb, 'rb') as handle:
        unserialized_data = pickle.load(handle)
    #unserialized_data  = defaultdict(list)
    for key in fingerprints:
        unserialized_data[key].extend(fingerprints[key])
    with open(fingerprintsdb, 'wb') as handle:
        pickle.dump(unserialized_data, handle, protocol=pickle.HIGHEST_PROTOCOL)