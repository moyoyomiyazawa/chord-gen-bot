import os
from synthesizer import Synthesizer, Waveform, Writer
from typing import List

# コードオブジェクトの配列からwavを生成する
def generate_wave_from_chord_objects(chords: List[object], filepath: str,) -> None:
    synthesizer = Synthesizer(osc1_waveform=Waveform.triangle, osc1_volume=1.0, use_osc2=False)

    note_length: int = 2
    root_pitch: int = 3
    chord_waves: list = [];
    for chord in chords:
        if type(chord) is list:
            for c in chord:
                notes: list = c.components_with_pitch(root_pitch=root_pitch)
                chord_waves.append(synthesizer.generate_chord(notes, note_length/len(chord)))
        else:
            notes: list = chord.components_with_pitch(root_pitch=root_pitch)
            chord_waves.append(synthesizer.generate_chord(notes, note_length))
    writer = Writer()
    writer.write_waves(filepath, *chord_waves)
