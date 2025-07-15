import requests
from tkinter import *
from tkinter import messagebox

# <-- جایگزین کن با کلید API خودت -->
API_KEY = '44146a57b32dec0fe3301f821f3e5714'

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=de"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        return f"Stadt: {city_name}\nTemperatur: {temp} °C\nLuftfeuchtigkeit: {humidity}%\nWetterlage: {description}"
    else:
        return None

def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        if weather:
            weather_label.config(text=weather)
        else:
            messagebox.showerror("Fehler", "Stadt nicht gefunden oder Verbindungsproblem.")
    else:
        messagebox.showwarning("Warnung", "Bitte geben Sie einen Stadtnamen ein.")

# GUI aufbauen
root = Tk()
root.title("Wetter-App")
root.geometry("300x200")

# Stadteingabe
city_entry = Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=10)

# Suchknopf
search_btn = Button(root, text="Wetter anzeigen", command=show_weather)
search_btn.pack()

# Wetteranzeige
weather_label = Label(root, text="", font=("Helvetica", 12), justify=LEFT)
weather_label.pack(pady=10)

root.mainloop()
