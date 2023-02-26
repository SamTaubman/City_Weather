import tkinter as tk
import requests
import time
import os

API_KEY = os.getenv(‘WEATHER_API_KEY’)
def getWeather(canvas):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']

    #outputted in Kelvin
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temperature = int(json_data['main']['temp_min'] - 273.15)
    max_temperature = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    condition_info =  condition
    temp_data = str(temperature) + "°C"
    maxtemp_data = "Max Temperature: " + str(max_temperature) + "°C"
    mintemp_data = "Min Temperature: " + str(min_temperature) + "°C"
    final_data = " Pressure: " + str(pressure) + " mmHg"\
         + "\n" + "Humidity: " + str(humidity) + "%"\
         + "\n" + "Wind Speed: " + str(wind) + " mph"
    sunrise_data = "Sunrise: " + sunrise + " AM"
    sunset_data = "Sunset: " + sunset + " PM"
    
    label1.config(text = condition_info)
    label2.config(text = temp_data)
    label3.config(text = maxtemp_data)
    label4.config(text = mintemp_data)
    label5.config(text = final_data)
    label6.config(text = sunrise_data)
    label7.config(text = sunset_data)
    
def main():
    canvas = tk.Tk()
    canvas.title("Weather App")
    canvas.geometry("1000x700")

    f = ("Bell MT", 15, "bold")
    t = ("Bell MT", 35, "bold")

    textfield = tk.Entry(canvas, font = t)
    textfield.pack(pady = 20)
    textfield.focus()
    textfield.bind('<Return>', getWeather)

    label1 = tk.Label(canvas, font = t)
    label1.pack()

    label2 = tk.Label(canvas, font = t)
    label2.pack()

    label3 = tk.Label(canvas, font = t, fg='red')
    label3.pack()

    label4 = tk.Label(canvas, font = t, fg='blue')
    label4.pack()

    label5 = tk.Label(canvas, font = t)
    label5.pack()

    label6 = tk.Label(canvas, font = t, fg='goldenrod2')
    label6.pack()

    label7 = tk.Label(canvas, font = t, fg='firebrick2')
    label7.pack()

    canvas.mainloop()
    
if __name__ == "__main__":
    main()
