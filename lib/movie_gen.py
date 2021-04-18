from moviepy.editor import *


# TODO: いまなっているコードをハイライトする機能を実装する
def create_movie(imagepath, audiopath, outputpath):
  imageclip = ImageClip(imagepath)
  audioclip = AudioFileClip(audiopath)
  finalclip = imageclip.set_audio(audioclip).set_duration(audioclip.duration)

  # 動画を保存
  finalclip.write_videofile(
    outputpath,
    codec='libx264',
    audio_codec='aac',
    audio_bitrate='128k',
    temp_audiofile='/tmp/temp-audio.m4a',
    remove_temp=True,
    fps=30,
    preset='ultrafast'
  )
