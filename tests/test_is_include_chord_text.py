from lib import is_include_chord_text

def test_コード進行テキストを含むか判別できる():
  s = """\
|BM7|EM7|
@chordpanda
"""
  assert is_include_chord_text(s) == True

def test_区切り文字がなくてもコード進行テキストを含むか判別できる():
  s = """\
BM7 EM7
@chordpanda
"""
  assert is_include_chord_text(s) == True

def test_コード進行テキストが含まない場合を判別できる():
  s = """\
こんにちは！元気ですか？
What's up?
@chordpanda
"""
  assert is_include_chord_text(s) == False
