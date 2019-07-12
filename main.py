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
    
def path_to_db(filename, window_size, id):

    song_root = Path(r"C:\Users\Akash Nayar\Desktop\Cogzam\Music")
    local_song_path = song_root / f"{filename}"
    samples = functionstart.add_songs(local_song_path)
    spec_test = spectrogram.spec_creator(samples)
    cutoff = background_def.back_val_finder(spec_test)
    peaks = peak_finding_code.local_peaks(spec_test, cutoff, window_size)
    fp = create_val_db.create_database(peaks, id)
    populate_db.populate_db(fp)

    with open('fingerprints.pickle', 'rb') as handle:
        unserialized_data = pickle.load(handle)
    return len(unserialized_data)

def master_tester():
    samples = fs.use_mic()
    spec = spectrogram.spec_creator(samples)
    cutoff = bd.back_val_finder(spec)
    peaks = pfc.local_peaks(spec, cutoff, 20)
    fp = cf.create_fingerprint(peaks)
    return gs.get_song(fp)