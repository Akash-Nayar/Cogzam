import get_song as gs
import peak_finding_code as pfc
import create_val_db
import background_def as bd
import create_fingerprint as cf
import functionstart as fs
import populate_db as pd
import spectrogram
from pathlib import Path
import pickle
    
def path_to_db(filepath, window_size, song_name, artist_name, song_datadb = "song_data.pickle",fingerprintsdb1 = 'fingerprints.pickle'):

    samples = fs.add_songs(filepath)
    spec_test = spectrogram.spec_creator(samples)
    cutoff = bd.back_val_finder(spec_test)
    peaks = pfc.local_peaks(spec_test, cutoff, window_size)
    pickle_in = open(song_datadb, "rb")
    song_data = pickle.load(pickle_in)
    if song_data.keys():
        n = int(sorted(song_data.keys())[-1])+1
        song_data[n] = (song_name, artist_name)
    else:
        n = 1
        song_data[n] = (song_name, artist_name)
    with open(song_datadb, 'wb') as handle:
        pickle.dump(song_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    fp = create_val_db.create_database(peaks, n)
    pd.populate_db(fp, fingerprintsdb = fingerprintsdb1)


def master_tester(song_datadb1 = "song_data.pickle",fingerprintsdb1 = 'fingerprints.pickle'):
    samples = fs.use_mic()
    spec = spectrogram.spec_creator(samples)
    cutoff = bd.back_val_finder(spec)
    peaks = pfc.local_peaks(spec, cutoff, 20)
    fp = cf.create_fingerprint(peaks)
    return gs.get_song(fp, song_datadb = song_datadb1, fingerprintsdb = fingerprintsdb1)

def manual_input(folder_path, filetype = ".mp3", song_datadb1 = "song_data.pickle", fingerprintsdb1 = 'fingerprints.pickle'):
    """
    Parameters
    ------------
    folder_path: Path object
    Path of music folder which you want to add into the database
    
    filetype: str object
    name of file type which you want to include in the input; includes the dot before file abbreviation (e.g. ".mp3")
    
    Globs all files of given file format
    Allows manual input of song and artist name after prompted with file name
    """
    files = folder_path.glob('*' + filetype)
    for i in files:
        local_song_path = song_root / i
        print(str(local_song_path))
        name = input('Name: ')
        artist = input('Artist: ')
        main.path_to_db(local_song_path, 20, name, artist, song_datadb = song_datadb1, fingerprintsdb = fingerprintsdb1)