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
    
def path_to_db(filename, window_size, song_name, artist_name):

    samples = functionstart.add_songs(filename)
    spec_test = spectrogram.spec_creator(samples)
    cutoff = background_def.back_val_finder(spec_test)
    peaks = peak_finding_code.local_peaks(spec_test, cutoff, window_size)
    pickle_in = open("song_data.pickle", "rb")
    song_data = pickle.load(pickle_in)
    n = str(int(sorted(song_data.keys())[-1])+1)
    song_data[n] = (song_name, artist_name)
    fp = create_val_db.create_database(peaks, n)
    populate_db.populate_db(fp)


def master_tester():
    samples = fs.use_mic()
    spec = spectrogram.spec_creator(samples)
    cutoff = bd.back_val_finder(spec)
    peaks = pfc.local_peaks(spec, cutoff, 20)
    fp = cf.create_fingerprint(peaks)
    return gs.get_song(fp, 5, 20)