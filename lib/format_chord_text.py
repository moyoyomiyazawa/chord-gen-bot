import re
from lib import is_include_chord_text


# コード進行テキストを含む文字列から余計なものを取り除いて、整形する
def format_chord_text(chord_text: str) -> str:
  print(chord_text)
  # 行で分割する
  rows = chord_text.splitlines()

  # コードを含まない行を除外する
  chord_text_rows = [row for row in rows if is_include_chord_text(row)]

  formatted_chord_text = ''
  for row in chord_text_rows:
    # 小節線で分割する
    pattern = re.compile(r'[ABCDEFG](?:[\dABCDEFGMm#♭b\-\+△\/\(\), ]|add|omit|sus|dim|aug|on)*')
    split_by_barline = re.findall(pattern, row)

    r = '|'.join(split_by_barline)
    formatted_chord_text += f'|{r}|\n'

  print(formatted_chord_text)
  return formatted_chord_text.strip()
