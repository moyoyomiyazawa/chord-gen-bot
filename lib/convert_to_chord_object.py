from pychord import Chord

# コード進行テキスト配列の要素をコードオブジェクトに変換
def convert_to_chord_object(chord_progression_list: list) -> list:
    chords = []
    for one_bar in chord_progression_list:
        if type(one_bar) is list:
            chords.append([Chord(c) for c in one_bar])
        else:
            chords.append(Chord(one_bar))
    return chords
