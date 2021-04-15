from lib import format_chord_text


def test_コード進行以外の文字を含むテキストを整形できる():
  s = """\
|FM9|CM9|
|FM9|CM9 FM9   |C  @chordpanda よろしく！
"""
  assert format_chord_text(s) == """\
|FM9|CM9|
|FM9|CM9 FM9   |C  |"""


def test_正常系():
  s = """\
|FM9|CM9|
|FM9|CM9 FM9|C|
@chordpanda
"""
  assert format_chord_text(s) == """\
|FM9|CM9|
|FM9|CM9 FM9|C|"""


def test_異常系():
  s = 'F G C C @chordpanda'
  assert format_chord_text(s) == '|F G C C |'


def test_コードの間に空白がある場合():
  s = '| FM9 CM9 | Am7 Dm7 | @chordpanda'
  assert format_chord_text(s) == '| FM9 CM9 | Am7 Dm7 |'

def test_コードの間に空白がある場合():
  s = 'この曲のFM9→E7の次にAm7→C7に行くとこ良いよね～'
  assert format_chord_text(s) == '|FM9|E7|Am7|C7|'
