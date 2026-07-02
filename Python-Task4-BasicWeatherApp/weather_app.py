import tkinter as tk
from tkinter import messagebox
import requests

API_KEY="16297b64fb3a0ebcd51cbcd4e770526a"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"]

        result.config(
            text=f"""
City : {city_name}, {country}

Temperature : {temp} °C

Humidity : {humidity} %

Pressure : {pressure} hPa

Weather : {weather.title()}
""",
            fg="blue"
        )

    except Exception:
        messagebox.showerror("Error", "Check your Internet or API Key!")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Weather App")
root.geometry("450x450")
root.resizable(False, False)

title = tk.Label(root,
                 text="Weather Application",
                 font=("Arial",20,"bold"),
                 fg="darkblue")
title.pack(pady=15)

tk.Label(root,
         text="Enter City Name",
         font=("Arial",12)).pack()

city_entry = tk.Entry(root,
                      font=("Arial",14),
                      width=25)
city_entry.pack(pady=10)

tk.Button(root,
          text="Get Weather",
          font=("Arial",12,"bold"),
          bg="green",
          fg="white",
          command=get_weather).pack(pady=10)

result = tk.Label(root,
                  text="",
                  font=("Arial",12),
                  justify="left")

result.pack(pady=20)

root.mainloop()