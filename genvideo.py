import ffmpeg

# TODO: Twitter Video用にエンコードを最適化する
def concat_image_and_wav(image, wav):
  image = ffmpeg.input(image)
  wav = ffmpeg.input(wav)
  stream = ffmpeg.output(image, wav, 'output.mp4', vcodec='h264', preset='slow', tune='film', pix_fmt='yuv420p', ac=2, ar=44100, ab='128k', acodec='aac', aprofile='aac_low', brand='mp42', r='29.97', s='500x500', vb='2048k')

  ffmpeg.run(stream)
