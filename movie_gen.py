from moviepy.editor import *


def create_movie(imagepath, audiopath):
  imageclip = ImageClip(imagepath)
  audioclip = AudioFileClip(audiopath)
  finalclip = imageclip.set_audio(audioclip).set_duration(audioclip.duration)

  # 動画を保存
  finalclip.write_videofile(
    'output.mp4',
    codec='libx264',
    audio_codec='aac',
    audio_bitrate='128k',
    temp_audiofile='temp-audio.m4a',
    remove_temp=True,
    fps=30,
    preset='ultrafast'
  )

