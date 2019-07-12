import pickle
import collections

def get_song(fingerprint, db_path):
    #Load pickle file with the dictionary files

    pickle_in = open("[PICKLE FILE NAME", "rb")
    database = pickle.load(pickle_in)

    time_offest = 0; #confused about how to use this!!!
    matches = []

    for item in fingerprint:
        time_bin = item[0]
        data = item[1]

        #check if data matches any dictionary values
        if data in database:
            current_values = database[data]
            #here's where i need to add time info
            matches.append(current_values)

    song_matches = [matches[i][0] for i in range(len(matches))] #puts the song ids only into an array
    c = collections.Counter(song_matches)
    top_three = c.most_common(3)

    if abs(top_three[0][1] - top_three[1][1]) > 5 and len(song_matches) > 10:
        return {DICT WITH SONG DATA}[top_three[0][0]]
    else:
        return "no song match found"