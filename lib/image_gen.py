from PIL import Image, ImageDraw, ImageFont
import os

# text = """
# |FM7|CM7|FM7|CM7|
# |FM7|CM7|FM7|CM7|
# |FM7|CM7|FM7|CM7|
# |FM7|CM7|FM7|CM7 Gsus4 G Bb|AbM7 Am7 Gsus4 G|
# """

def chord_text_to_image(text, basedir):
  # 背景画像

  image = Image.open(os.path.join(basedir, 'bgimage.png'))
  draw = ImageDraw.Draw(image)

  # テキストが背景画像の幅に収まるようにフォントサイズを調整
  font_size = 50
  font = ImageFont.truetype(os.path.join(basedir, 'fonts/Noto_Sans_JP/NotoSansJP-Black.otf'), size=font_size)
  while draw.textsize(text, font=font)[0] >= image.size[0] - 100:
    font_size -= 5
    font = ImageFont.truetype(os.path.join(basedir, 'fonts/Noto_Sans_JP/NotoSansJP-Black.otf'), size=font_size)

  # テキストのサイズ
  draw_text_width, draw_text_height = draw.textsize(text, font=font)

  # テキスト上下中央寄せで描画
  start_x_point = image.size[0] / 2 - draw_text_width / 2
  start_y_point = image.size[1] / 2 - draw_text_height / 2
  draw.text((start_x_point, start_y_point), text, fill=(255,255,255), font=font)

  # 画像を保存
  image.save(os.path.join(basedir, 'chord_image.png'))
