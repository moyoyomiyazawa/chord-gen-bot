import time
import os
import re
import tweepy
import config
import genchord
import videoupload
import image_gen
import movie_gen


CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth ,wait_on_rate_limit = True)

status = api.mentions_timeline()

DIR = os.path.dirname(os.path.abspath(__file__))
imagepath = os.path.join(DIR, 'chord_image.png')
audiopath = os.path.join(DIR, 'chord_progression.wav')
outputpath = os.path.join(DIR, 'output.mp4')


for mention in status:
  mention_time = mention.created_at.timestamp()
  now_time = time.time()

  # mention_timeが本初子午線の時刻で取得されるため 9時間(32400秒) + 1分
  reply_time = 32400 + 60

  # 10分以内に来たリプライを10分ごとに返す
  if now_time - mention_time < reply_time:
    if re.search('\|.*\|', mention.text):
      try:
        # コード進行からwavを生成
        genchord.generate_chord_from_text(mention.text, audiopath)

        # コードテキストから動画用の画像を生成
        video_image_text = ''
        rows = re.findall('\|(.*)\|', mention.text)

        for row in rows:
          video_image_text += f'|{row}|\n'
        print(video_image_text)
        image_gen.chord_text_to_image(video_image_text)

        # video を作成
        movie_gen.create_movie(imagepath, audiopath, outputpath)

        reply_text = f"@{mention.user.screen_name}"
        media_id = videoupload.upload(outputpath)
        time.sleep(5)

        # リプライを送信
        api.update_status(status=reply_text, in_reply_to_status_id=mention.id, media_ids=[media_id])
      except Exception as e:
          print(e)
      # finally:
      #   os.remove(audiopath)
      #   os.remove(outputpath)
