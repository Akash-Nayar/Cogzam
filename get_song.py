import pickle
import collections

def get_song(fingerprint, song_data_from = "song_data.pickle",fingerprints_from = 'fingerprints.pickle'):


    """
    Returns the most likely song given a fingerprint of frequency and time values

    Parameters
    --------------------------------
    fingerprint: list
        Contains a list of tuples (tb, (f1, f2 time))
        tb - time bin of the peak
        f1/f2 - frequency bins
        time - time bin difference
    md: int
        number of matches different between the top two matches
    mt: int
        minimum number of matches for the top song

    Returns
    --------------------------------
    String
        Either returns the Song and Artist Name or "No Song Found"
    """

    
    # Load pickle file with the dictionary values from database and song values
    pickle_in = open(fingerprints_from, "rb")
    database = pickle.load(pickle_in)
    pickle_in2 = open(song_data_from, "rb")
    song_data = pickle.load(pickle_in2)
    

    #
    matches = []

    m_diff = 5
    m_total = 30

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

    c = collections.Counter(matches)
    top_two = c.most_common(2) # gets tuples with the top three most common based on matches    
    
    # returns either the song data or "No Song Found"
    if (top_two[0][1] > m_total):
        song_title = song_data[top_two[0][0][0]][0]
        song_artist = song_data[top_two[0][0][0]][1]
        return song_title + " - " + song_artist
    else:
        return "No Song Found"
