import tkinter as tk
from tkinter import messagebox
import requests

# Student: Çağatay İpek
# Project: Weather Dashboard
# Tool Used: Cursor

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vibe Weather Dashboard")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Title
        self.title_label = tk.Label(root, text="Weather App", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # City Entry
        self.city_entry = tk.Entry(root, font=("Helvetica", 14), width=20)
        self.city_entry.pack(pady=10)
        
        # Search Button - DÜZELTİLEN SATIR BURASI
        self.search_btn = tk.Button(root, text="Get Weather", command=self.get_weather, font=("Helvetica", 12), bg="#007bff", fg="white")
        self.search_btn.pack(pady=10)

        # Results Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0", justify="left")
        self.result_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        # Using a public open API (Open-Meteo) which doesn't require an API Key for simplicity
        try:
            # First, get coordinates
            geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
            geo_response = requests.get(geocoding_url)
            geo_data = geo_response.json()

            if not geo_data.get("results"):
                messagebox.showerror("Error", "City not found.")
                return

            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]

            # Get weather
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()
            
            current = weather_data["current_weather"]
            temp = current["temperature"]
            wind = current["windspeed"]
            
            result_text = f"City: {city.title()}\nTemperature: {temp}°C\nWind Speed: {wind} km/h"
            self.result_label.config(text=result_text)

        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()