import requests
from beautifultable import  BeautifulTable
table = BeautifulTable()
API_key = "9fed8863a2be30ce1cbecb13f6b57d0b"
city = input("\nEnter the City: ")
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_key+"&lang = fa"
data = requests.get(url).json()

weather = data["weather"][0]["description"]
wind_speed = str(data["wind"]["speed"]) + " m/s"
temp = str(round(data["main"]["temp"] - 273.15)) + " °C"
humidity = str(data["main"]["humidity"]) + " %"
timezone = str(data["timezone"] / 3600) + " h"

print("")
table.columns.header = [city.title()]
table.rows.append([weather])
table.rows.append([temp])
table.rows.append([humidity])
table.rows.append([timezone])
table.rows.append([wind_speed])
table.rows.header = ["Clouds:", "Temperature:", "Humidity:", "Time Zone:" , "Wind Speed:"]
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
print(table)
input()

# Made By Yasin Rezvani 