def populate_db(fingerprints):

    """
    Populates the database with fingerprints

    Parameters:
    -----------
    fingerprints : dict
        Fingerprints of the peaks of a song
    """

    import pickle
    for key in fingerprints:
        unserialized_data[key].extend(fingerprints[key])
    with open('fingerprints.pickle', 'wb') as handle:
        pickle.dump(unserialized_data, handle, protocol=pickle.HIGHEST_PROTOCOL)