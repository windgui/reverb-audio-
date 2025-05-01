from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import random

# abrir audio
with AudioFile('audiopuro.mp3') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

# config reverb
reverb = Reverb(room_size=0.8, damping=0.1, wet_level=0.3, dry_level=0.7)


board = Pedalboard([reverb])
effected = board(audio, samplerate)

# salvar audio com reverb
random_id = random.randint(100000, 999999)
output_filename = f"audiocomreverb{random_id}.mp3"
with AudioFile(output_filename, 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)
