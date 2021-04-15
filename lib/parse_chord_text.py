import re

# コード進行テキストをパースして配列にして返す
def parse_chord_text(chord_text: str) -> list:
    # 小節の区切りで分割する
    pattern = re.compile(r'[ABCDEFG](?:[\dABCDEFGMm#♭b\-\+△\/\(\), ]|add|omit|sus|dim|aug|on)*')
    split_by_barline = [bar.strip() for bar in re.findall(pattern, chord_text)]
    print(split_by_barline)

    # 同一小節内の区切りで分割する
    chord_progression_list = [bar if not re.search(r'\s+', bar) else re.split(r'\s+', bar) for bar in split_by_barline]
    print(chord_progression_list)

    return chord_progression_list
