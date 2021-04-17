from PIL import Image, ImageDraw, ImageFont
import os, re

def chord_text_to_image(image_text: str, basedir, imagepath) -> None:
  # 背景画像
  image = Image.open(os.path.join(basedir, '/lib/bgimage.png'))
  draw = ImageDraw.Draw(image)

  # テキストが背景画像の幅に収まるようにフォントサイズを調整
  font_size: int = 50
  font = ImageFont.truetype(os.path.join(basedir, '/lib/fonts/Noto_Sans_JP/NotoSansJP-Black.otf'), size=font_size)
  while draw.textsize(image_text, font=font)[0] >= image.size[0] - 100:
    font_size -= 5
    font = ImageFont.truetype(os.path.join(basedir, '/lib/fonts/Noto_Sans_JP/NotoSansJP-Black.otf'), size=font_size)

  # テキストのサイズ
  draw_text_width, draw_text_height = draw.textsize(image_text, font=font)

  # テキスト上下中央寄せで描画
  start_x_point = image.size[0] / 2 - draw_text_width / 2
  start_y_point = image.size[1] / 2 - draw_text_height / 2
  draw.text((start_x_point, start_y_point), image_text, fill=(255,255,255), font=font)

  # 画像を保存
  image.save(imagepath)
