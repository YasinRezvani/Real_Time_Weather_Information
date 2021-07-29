import requests
from pprint import pprint

API_key = "9fed8863a2be30ce1cbecb13f6b57d0b"
city = input("Enter the City: ")

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_key+"&lang = fa"

data = requests.get(url).json()

pprint(data)

# Made By Yasin Rezvani 