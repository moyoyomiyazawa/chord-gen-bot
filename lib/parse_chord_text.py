import re
import constants

# コード進行テキストをパースして配列にして返す
def parse_chord_text(chord_text: str) -> list:
    # 小節の区切りで分割する
    pattern = re.compile(constants.CHORD_PATTERN)
    split_by_barline = [bar.strip() for bar in re.findall(pattern, chord_text)]

    # 同一小節内の区切りで分割する
    chord_progression_list = [bar if not re.search(r'\s+', bar) else re.split(r'\s+', bar) for bar in split_by_barline]
    print('chord_progression_list:', chord_progression_list)

    return chord_progression_list
