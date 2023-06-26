import requests
import pickle
import json

class WeatherForecasting:
    def __init__(self, cityName):
        self.cityName = cityName

    def getWeatherData(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.cityName}&appid={self.__getApiKey()}&units=metric')
        if response.status_code == 200:
            dataJson = json.loads(response.text)
            return dataJson['main'], dataJson['weather'][0], dataJson['wind']['speed'] #, self.getGovernomentAlerts(dataJson['coord']['lat'], dataJson['coord']['lon'])
        raise Exception('Api call failed with status code - ' + str(response.status_code))
    
    def getGovernomentAlerts(self, lat, lon):
        response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={self.__getApiKey()}')
        if response.status_code == 200:
            return json.loads(response.text)["alerts"]
        raise Exception('Api call failed with status code - ' + str(response.status_code))

    def __getApiKey(self):
        with open('apiKey.pkl', 'rb') as file:
            return pickle.load(file)
