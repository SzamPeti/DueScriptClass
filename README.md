# DueScriptClass
This repo was made for a school class. Saved our works through this

# Weather Chatbot

## Telepítés
Telepítsd a szükséges modulokat a következő paranccsal:
```
pip install requests
```

## Használat
Futtasd a weather_bot.py fájlt a következő paranccsal:
```
python weather_bot.py
```
A chatbot óránként értesítéseket küld az aktuális időjárásról.

## Függvények és Modulok
### WeatherBot osztály
+ __init__(self, api_key): A WeatherBot osztály inicializálása egy OpenWeatherMap API kulcs megadásával.
+ get_weather(self): Lekéri az aktuális időjárást az API-tól.
+ send_notification(self, message): Megjeleníti az értesítést egy pop-up ablakban.
+ run(self): A chatbot fő futtatási metódusa, amely folyamatosan lekérdezi az időjárást és küldi az értesítéseket.
