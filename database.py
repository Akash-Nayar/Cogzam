from collections import defaultdict
import pickle
def create_or_reset(song_datadb = "song_data.pickle",fingerprintsdb = 'fingerprints.pickle'):
    '''
    Resets or creates given song and fingerprint database
    Parameters:
    ---------------
    song_datadb: str object
    name of pickle file for song data
    
    fingerprintsdb: str object
    name of pickle file for fingerprints
    
    Returns:
    ---------------
    None
    '''
    
    
    unserialized_data  = defaultdict(list)
    with open(fingerprintsdb, 'wb') as handle:
        pickle.dump(unserialized_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    unserialized_song_data  = defaultdict(list)
    with open(song_datadb, 'wb') as handle:
        pickle.dump(unserialized_song_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
def check_contents(song_datadb = "song_data.pickle"):
    '''
    Returns dictionary of songs already in the database
    Parameters:
    ---------------
    song_datadb: str object
    name of pickle file for song data
    
    Returns:
    ---------------
    Print of song data dictionary
    '''
    with open(song_datadb, mode = 'rb') as handle:
        song_data = pickle.load(handle)
    print(song_data)
