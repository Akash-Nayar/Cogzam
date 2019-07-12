import pickle
import collections


def get_song(fingerprint):

    """
    Returns the most likely song given a fingerprint of frequency and time values

    Parameters
    --------------------------------
    fingerprint: list
        Contains a list of tuples (tb, (f1, f2 time))
        tb - time bin of the peak
        f1/f2 - frequency bins
        time - time bin difference

    Returns
    --------------------------------
    String
        Either returns the Song and Artist Name or "No Song Found"
    """

    # Load pickle file with the dictionary values from database and song values
    pickle_in = open("fingerprints.pickle", "rb")
    database = pickle.load(pickle_in)

    pickle_in = open("songs.pickle", "rb")
    song_data = pickle.load(pickle_in)

    #
    matches = []
    c = collections.Counter(matches)

    # Iterate through the values within the fingerprint
    for finger in fingerprint:
        time_bin = finger[0] # integer: indicates the time bin
        data = finger[1] # tuple: contains two frequencies, time difference

        # check if data matches any dictionary values
        if data in database:
            temp_matches = database[data]
            for match in temp_matches:
                offset = time_bin -  match[1]
                matches.append((match[0], offset))

    top_three = c.most_common(3)

    if abs(top_three[0][1] - top_three[1][1]) > 5 and top_three[0][1] > 5:
        song_title = song_data[top_three[0][0]][0]
        song_artist = song_data[top_three[0][0]][1]
        return song_title + " - " + song_artist
    else:
        return "No Song Found"
