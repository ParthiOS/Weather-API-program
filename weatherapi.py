import requests

api_key = '6c70e32f5cdcf13580c77d998c997903'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)


# Add description here as well as a query for the forecast
## eventually create a graphical interface that shows all data on the same screen
if response.status_code == 200:
    dat = response.json()
    temp = dat['main']['temp']
    descr = dat['weather'][0]['description']
    print(f'Temperature: {temp} Kelvins')
    print(f'Temperature: {temp - 273.15} Celsius')
    print(f'Description: {descr}')
else:
    print('Error fetching weather data')