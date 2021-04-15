import re

# コード進行テキストを含むかどうかを判定する
def is_include_chord_text(chord_text: str) -> bool:
  return bool(re.search(r'[ABCDEFG](?:[\dABCDEFGMm#♭b\-\+△\/\(\),]|add|omit|sus|dim|aug|on)*', chord_text))
