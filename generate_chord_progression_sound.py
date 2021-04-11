import os
import re

from pychord import Chord, ChordProgression
from synthesizer import Synthesizer, Waveform, Writer

DIR = os.path.dirname(os.path.abspath(__file__))


def parse_chord_text(chord_text):
    rows = re.findall('\|(.*)\|', chord_text)
    splitted_rows = [re.split('\s*\|\s*', row.strip()) for row in rows]
    print('splitted_rows', splitted_rows)

    chord_progression_list = []
    for row in splitted_rows:
        for bar in row:
            if ' ' in bar:
                chord_progression_list.append(re.split('\s+', bar))
            else:
                chord_progression_list.append(bar)
    return chord_progression_list

def convert_to_chord(chord_progression_list):
    chords = []
    for one_bar in chord_progression_list:
        if type(one_bar) is list:
            chords.append([Chord(c) for c in one_bar])
        else:
            chords.append(Chord(one_bar))
    return chords


def main():
    writer = Writer()
    with open('./chord_progression.txt') as f:
        s = f.read()
        chord_progression_list = parse_chord_text(s)
        chords = convert_to_chord(chord_progression_list)

        synthesizer = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=1.0, use_osc2=False)

        chord_waves = [];
        note_length = 2
        for chord in chords:
            if type(chord) is list:
                for c in chord:
                    notes = c.components_with_pitch(root_pitch=3)
                    chord_waves.append(synthesizer.generate_chord(notes, note_length/len(chord)))
            else:
                notes = chord.components_with_pitch(root_pitch=3)
                chord_waves.append(synthesizer.generate_chord(notes, note_length))
        writer.write_waves(os.path.join(DIR, "chord_progression.wav"), *chord_waves)


if __name__ == '__main__':
    main()
