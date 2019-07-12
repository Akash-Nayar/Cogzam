from pathlib import Path
import numpy as np
def use_mic():
    from pathlib import Path
    '''
    Records audio for 10 seconds using the microphone and checks against song data in database to identify song
    
    Parameters
    ------------
    None
    
    Returns
    ------------
    song_info: Tuple('string','string')
    Strings containing Name of Song and Name of Artist
    '''
    from microphone import record_audio
    frames, sampling_rate = record_audio(10)
    listen_audio = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    return listen_audio
    
def test(song_path):
    from pathlib import Path
    '''
    Checks audio file against existing song database to identify song
    Parameters
    ------------
    song_path: Path object
    File Path of test song
    
    Returns
    ------------
    song_info: Tuple('string','string')
    Strings containing Name of Song and Name of Artist
    
    '''
    
    
    import numpy as np
    import librosa
    samples, fs = librosa.load(str(song_path), sr=44100, mono=True)
    samples*=2**15
    return samples
    

def add_songs(song_path, name = None, artist = None):
    from pathlib import Path
    '''
    Inputs song path of audio file, as well as optional keyword arguments for strings which name the song and the artist
    Generates data from the audio file, then manipulates data to generate keys
    Assigns keys to song and adds to databases containing fingerprints for song ids and song ids for song info
    Parameters
    ------------
    song_path: Path object
    File Path of test song
    
    name: string
    name of song
    
    artist: string
    name of artist
    
    
    Returns
    ------------
    None
    
    '''

    import numpy as np
    import librosa
    samples, fs = librosa.load(str(song_path), sr=44100, mono=True)
    samples*=2**15
    return samples
    
song_root = Path(r"C:\Users\Akash Nayar\Desktop\Cogzam\Music")
local_song_path = song_root / r"Eminem - Beautiful (Official Music Video).mp3"
test(local_song_path)