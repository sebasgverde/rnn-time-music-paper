
# import midi_manager
import os
import midi

# data_dir='/home/sebastian/exampleresearch/data/test_data'
data_dir='../data/midi'
# data_dir='../data/validation/midi'

standard_resoultion = 16
def midi2sequenceVectorWithTime(midifile='test.mid'):
    pattern = midi.read_midifile(midifile)
    sequence = []
    resolution_midi = pattern.resolution
    resolution = resolution_midi * 4 / standard_resoultion
    for track in pattern:
        for evt in track:
            # In this case I'm interested in time, therefore, need the note on
            # event with the final tick
            if isinstance(evt, midi.NoteOnEvent) and evt.tick > 1:
                key_in_dict = int(round(evt.tick / float(resolution)))
                sequence.append([evt.pitch,key_in_dict])

    return sequence

def midi_folder_2_list_of_sequences(data_dir):
    tensor = []
    for midifile in os.listdir(data_dir):
        # print midifile
        tensor.append(midi2sequenceVectorWithTime(data_dir+ '/' +midifile))

    return tensor

tensor = midi_folder_2_list_of_sequences(data_dir)

import pdb; pdb.set_trace()
import pickle
# pickle.dump(tensor,open("train_song_list.p", "wb"))

print ""
