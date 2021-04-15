from lib import flatten

def test_flatten():
  l = [['F', 'G'], ['C', 'Am7'], 'Em7']
  assert flatten(l) == ['F', 'G', 'C', 'Am7', 'Em7']
