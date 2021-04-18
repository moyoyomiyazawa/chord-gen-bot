import time, os, sys
import tweepy
from lib import *


# Twitter APIの設定情報
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth ,wait_on_rate_limit = True)


def generate_video_from_mention_tweet(mention: dict, basedir):
  imagepath = '/tmp/chord_image.png'
  audiopath = '/tmp/chord_progression.wav'
  outputpath = '/tmp/output.mp4'

  # コード進行テキストがメンション内になければ処理を修了する
  if not is_include_chord_text(mention.get('text')):
    print('メンション内にコード進行テキストがなかったよ')
    return None

  try:
    # メンションの中のコード進行テキストをパース
    chord_progression_list = parse_chord_text(mention.get('text'))
    # コード進行リストの要素をコードオブジェクトに変換
    chords = convert_to_chord_object(chord_progression_list)
    # コードオブジェクトのリストからwavを生成
    chordwave_gen.generate_wave_from_chord_objects(chords, audiopath)
    # 画像用にコード進行テキストを整形
    formatted_chord_text = format_chord_text(mention.get('text'))
    # コードテキストから動画用の画像を生成
    image_gen.chord_text_to_image(formatted_chord_text, basedir, imagepath)
    # 生成したwav、画像を合成しvideoを作成
    movie_gen.create_movie(imagepath, audiopath, outputpath)
    # 作成したvideoをTwitterにアップロードしてmedia_idを取得する
    media_id = video_upload.upload(outputpath)
    time.sleep(5) # アップロードが完了するまで少し待つ
    # リプライを送信
    reply_text = f"@{mention.get('user').get('screen_name')} できたよ🐼"
    api.update_status(status=reply_text, in_reply_to_status_id=mention.get('id'), media_ids=[media_id])
    print('リプライ完了！')
  except Exception as e:
      print(e)
      reply_text = f"@{mention.get('user').get('screen_name')} ごめん、なにか問題が発生したみたい…😢"
      api.update_status(status=reply_text, in_reply_to_status_id=mention.get('id'))
