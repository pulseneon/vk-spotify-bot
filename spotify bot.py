import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
import vk_api

login = 'Ваш логин ВКонтакте' 
passw = 'Ваш пароль ВКонтакте'

Client_id = 'Ваш Client ID'
Client_secret = 'Ваш Client Secret'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_id,
                                                client_secret=Client_secret,
                                                redirect_uri="http://127.0.0.1:9090",
                                                scope="user-read-playback-state"))
vk_session = vk_api.VkApi(login, passw)
vk_session.auth()
vk = vk_session.get_api()

answ = "🎧 Сейчас не слушает музыку в Spotify." # Можно заменить на свой статус, который отображается, когда ничего не слушаете
send_text = "🎧 Слушает в Spotify: " # Можно заменить на ваш текст + песня
delay = 25 # Задержка между проверками 25 секунд
long_delay = 60 #Длинная задержка (минута)

print("[" + time.ctime() + "] Script work")
while True:
  try:
    results = sp.current_playback()
    try:
      track = results['item']['artists'][0]['name'] + " — " +  results['item']['name']
      sendtext = send_text + track
      getstatus = vk.status.get()
      mystatus = getstatus['text']
      if mystatus == sendtext:
        print("[" + time.ctime() + "] Status already set")
      else:
        vk.status.set(text=sendtext)
        print("[" + time.ctime() + "] New status set")
      time.sleep(delay)
    except Exception as e:
      getstatus = vk.status.get()
      mystatus = getstatus['text']
      if mystatus == answ:
        print("[" + time.ctime() + "] None status already set")
      else:
        vk.status.set(text=answ)
        print("[" + time.ctime() + "] New none status already set")
      time.sleep(long_delay)
  except Exception as e:
    print("[" + time.ctime() + "] Ошибка входа. Код ошибки: ")
    print(e)
