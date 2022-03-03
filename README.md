# vk-spotify-bot

Отображайте прослушиваемые песни в своем статусе ВКонтакте при помощи spotipy и vk_api.

# Скриншоты

![image](https://user-images.githubusercontent.com/87504288/156492469-0a9faf22-e877-4726-b0e4-ea3de30c0d21.png)
![image](https://user-images.githubusercontent.com/87504288/156493429-a19702cc-398a-423b-8346-cfe070eab15f.png)
![image](https://user-images.githubusercontent.com/87504288/156493498-e9660ba9-8c80-49cf-a5bb-41aaa4b5d596.png)
![image](https://user-images.githubusercontent.com/87504288/156493451-6a2c5b31-3e11-4960-b5fb-2f6107834b40.png)


## Установка и настройка

Скачайте библиотеки: 
*pip install spotipy --upgrade* и *pip3 install vk_api*
Авторизуемся: *https://developer.spotify.com/dashboard/login*
Переходим: ![image](https://user-images.githubusercontent.com/87504288/156492891-094ff20e-f39a-4b0e-8547-b0fdf2af6daa.png)
Получаем Client ID и  Client Secret
![image](https://user-images.githubusercontent.com/87504288/156492946-65d2487b-1d5f-4163-9e82-577c65618faa.png)
Заходим в настройки и вставляем http://127.0.0.1:9090 в Redirect URIs
![image](https://user-images.githubusercontent.com/87504288/156493029-f6de3345-9cec-4153-b707-17bf7e5e1afb.png)

Открываем spotify bot.py редактором. Вставляем свои данные от ВКонтакте в соответствующем поле и заменяем Client ID и Client Secret. Рекомендуется заменить переменную *answ* на свой обычный статус, для его отображения во время не прослушивания песен в спотифай.

*Возможно такое, что ВКонтакте будет требовать капчу из-за постоянного запроса статуса и его изменения. Тогда стоит увеличить переменные delay и long_delay, тем самым точнее откалибровав приложение (возможно их можно уменьшить для более точного отображения статуса - все по ситуации, ничто не вечно)*

**03.03.2022 6:59**
