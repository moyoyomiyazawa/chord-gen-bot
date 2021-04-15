import datetime, time, os, re, sys
import tweepy
import config
from lib import *


basedir = os.path.dirname(os.path.abspath(__file__))
imagepath = os.path.join(basedir, 'chord_image.png')
audiopath = os.path.join(basedir, 'chord_progression.wav')
outputpath = os.path.join(basedir, 'output.mp4')

# Twitter APIの設定情報
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth ,wait_on_rate_limit = True)

# メンション一覧を取得
mentions = api.mentions_timeline()

# mention_timeが本初子午線の時刻で取得されるため 9時間(32400秒) + 3分
reply_time = 32400 + 180 # 一時的に3分に
now_time = time.time()

# 3分以内のメンションを抽出する
filtered_mentions = [mention for mention in mentions if (now_time - mention.created_at.timestamp()) < reply_time]

# print(filtered_mentions);

# 指定した時間内にメンションがなければ処理を修了する
if filtered_mentions == []:
  sys.exit(0)

for mention in filtered_mentions:
  # 指定時間内のメンションがちゃんと取得できているかデバッグ用
  mention_time = mention.created_at.timestamp()
  now_time = time.time()
  print(datetime.datetime.fromtimestamp(now_time), datetime.datetime.fromtimestamp(mention_time))

  # コード進行テキストがメンション内になければ処理を修了する
  if not is_include_chord_text(mention.text):
    reply = f"@{mention.user.screen_name} コード進行が判定できなかった;;"
    api.update_status(status=reply, in_reply_to_status_id=mention.id, )
    sys.exit(0)

  try:
    # メンションの中のコード進行テキストをパース
    chord_progression_list = parse_chord_text(mention.text)
    # コード進行リストの要素をコードオブジェクトに変換
    chords = convert_to_chord_object(chord_progression_list)
    # コードオブジェクトのリストからwavを生成
    chordwave_gen.generate_wave_from_chord_objects(chords, audiopath, basedir)
    # 画像用にコード進行テキストを整形
    formatted_chord_text = format_chord_text(mention.text)
    # コードテキストから動画用の画像を生成
    image_gen.chord_text_to_image(formatted_chord_text, basedir)
    # 生成したwav、画像を合成しvideoを作成
    movie_gen.create_movie(imagepath, audiopath, outputpath)
    # 作成したvideoをTwitterにアップロードしてmedia_idを取得する
    media_id = video_upload.upload(outputpath)
    time.sleep(5) # アップロードが完了するまで少し待つ
    # リプライを送信
    reply_text = f"@{mention.user.screen_name} できたよ🐼"
    api.update_status(status=reply_text, in_reply_to_status_id=mention.id, media_ids=[media_id])
  except Exception as e:
      print(e)
      reply_text = f"@{mention.user.screen_name} ごめん、なにか問題が発生したみたい…😢"
      api.update_status(status=reply_text, in_reply_to_status_id=mention.id)
  # finally:
  #   os.remove(audiopath)
  #   os.remove(outputpath)
