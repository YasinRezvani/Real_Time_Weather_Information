from time import timezone
import requests
from tkinter import * 
from tkinter import ttk

root= Tk()

root.title("Real_Time_Weather_Information")
root.geometry("500x290")
root.resizable(False, False)

label=Label(root, text="Enter the City: ", font=("Arial 18 bold"))
label.pack()

entry= Entry(root, width= 40)
entry.pack()

def get_data():
    API_key = "9fed8863a2be30ce1cbecb13f6b57d0b"
    city = entry.get()
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_key+"&lang = fa"
    data = requests.get(url).json()
    weather =  "Clouds: "+str(data["weather"][0]["description"])
    wind_speed = "Wind Speed: "+str(data["wind"]["speed"]) + " m/s"
    temp = "Temperature: "+str(round(data["main"]["temp"] - 273.15)) + " °C"
    humidity = "Humidity: "+str(data["main"]["humidity"]) + " %"
    timezone = "Time Zone: "+str(data["timezone"] / 3600) + " h"

    weather_.configure(text=weather)
    wind_speed_.configure(text=wind_speed)
    temp_.configure(text=temp)
    humidity_.configure(text=humidity)
    timezone_.configure(text=timezone)


ttk.Button(root, text= "Search",width= 20,command=get_data).pack(pady=10)
lbl = Label(root, font=("Arial 15"))
lbl.pack()
weather_ = Label(root , font=("Arial 15") ,bg ="blue" , fg="white")
weather_.pack()
wind_speed_ = Label(root , font=("Arial 15") ,bg ="blue" , fg="white")
wind_speed_.pack()
temp_ = Label(root , font=("Arial 15") ,bg ="blue" , fg="white")
temp_.pack()
humidity_ = Label(root , font=("Arial 15") ,bg ="blue" , fg="white")
humidity_.pack()
timezone_ = Label(root , font=("Arial 15") ,bg ="blue" , fg="white")
timezone_.pack()

root.mainloop()    

