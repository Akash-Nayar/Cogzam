def populate_db(fingerprints):

    """
    Populates the database with fingerprints

    Parameters:
    -----------
    fingerprints : dict
        Fingerprints of the peaks of a song
    """

    import pickle
    with open('fingerprints.pickle', 'rb') as handle:
        unserialized_data = pickle.load(handle)
    for key in fingerprints:
        unserialized_data[key].extend(fingerprints[key])
    with open('fingerprints.pickle', 'wb') as handle:
        pickle.dump(unserialized_data, handle, protocol=pickle.HIGHEST_PROTOCOL)