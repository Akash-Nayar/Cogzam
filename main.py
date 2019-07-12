import create_db
import fingerprint
import functionstart
import peak_finding_code
import spectrogram
import background_def
from pathlib import Path
import pickle
    
def path_to_db(filename, window_size, id):

    song_root = Path(r"C:\Users\Akash Nayar\Desktop\Cogzam\Music")
    local_song_path = song_root / f"{filename}"
    samples = functionstart.add_songs(local_song_path)
    spec_test = spectrogram.spec_creator(samples)
    cutoff = background_def.back_val_finder(spec_test)
    peaks = peak_finding_code.local_peaks(spec_test, cutoff, window_size)
    fp = fingerprint.create_database(peaks, id)
    create_db.populate_db(fp)

    with open('fingerprints.pickle', 'rb') as handle:
        unserialized_data = pickle.load(handle)
    return len(unserialized_data)