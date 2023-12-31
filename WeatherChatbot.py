import requests
import time
import tkinter as tk
from tkinter import messagebox


class WeatherBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.weather_url = "http://api.openweathermap.org/data/2.5/weather"
        self.city = "Dunaújváros"  # Város neve, amelyre kérjük az időjárásinformációt

    def get_weather(self):
        params = {
            'q': self.city,
            'appid': self.api_key,
            'units': 'metric'  # Mértékegység Celsiusban
        }
        response = requests.get(self.weather_url, params=params)
        data = response.json()

        if response.status_code == 200:
            city_name = data['name']
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            wind_speed = round(data['wind']['speed'] * 3.6, 2)
            return (f"{city_name}\nIdőjárás: {weather_description}\nHőmérséklet: {temperature}°C\nHőérzet: {feels_like}°C\n"
                    f"Szélsebesség: {wind_speed} km/h")
        else:
            return "Nem sikerült lekérdezni az időjárást."

    def send_notification(self, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Időjárás Értesítés", message)
        root.destroy()

    def run(self):
        while True:
            weather_info = self.get_weather()
            self.send_notification(weather_info)
            time.sleep(3600)  # Várakozás 1 óra, majd újra lekérdezés (ms-ben számol)


if __name__ == "__main__":
    api_key = "2be00f64519f029d1f190b1e6364c817"

    weather_bot = WeatherBot(api_key)
    weather_bot.run()
