from lib import parse_chord_text

def test_1行のコード進行テキストがパースできる():
  s = '|FM9|CM9| @chordpanda'
  assert parse_chord_text(s) == ['FM9', 'CM9']

def test_改行を含むコード進行テキストがパースできる():
  s = """
  |FM9|CM9|Em7|Am7|
  |FM9|CM9|Em7|Am7|
  @chordpanda
  """
  assert parse_chord_text(s) == ['FM9', 'CM9', 'Em7', 'Am7', 'FM9', 'CM9', 'Em7', 'Am7']

def test_コードが1つだけのコード進行テキストがパースできる():
  s = '|FM9| @chordpanda'
  assert parse_chord_text(s) == ['FM9']

def test_1つの区切りの中に複数のコードがある場合もパースできる():
  s = """|FM9|E7 E7/G#|Am9|Gm7 Gm7/C|
  @chordpanda
  """
  assert parse_chord_text(s) == ['FM9', ['E7', 'E7/G#'], 'Am9', ['Gm7', 'Gm7/C']]

def test_区切り文字がない場合もパースできる():
  s = '@chordpanda C F G C'
  assert parse_chord_text(s) == [['C', 'F', 'G', 'C']]

def test_頭と末尾の区切り文字がなくてもパースできる():
  s = '@chordpanda C|F|G|C'
  assert parse_chord_text(s) == ['C', 'F', 'G', 'C']

def test_文章の間にコード進行があってもパースできる():
  s = 'この曲のFM9→E7の次にAm7→C7に行くとこ良いよね～'
  assert parse_chord_text(s) == ['FM9', 'E7', 'Am7', 'C7']

# TODO: これの解決が難しい... 一旦後回しにする
# def test_コードが含まない文章は空配列となる():
#   s = """
#   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
#   """
#   assert parse_chord_text(s) == []
