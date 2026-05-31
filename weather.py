import requests
def get_weather(city):
    url = f"http://wttr.in/{city}?format=3"
    data = requests.get(url)
    print(data.text)

city = input("Enter city name: ")
get_weather(city)   

