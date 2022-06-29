### News Reading Script  ###
"""
    Uses News API to read top 10 news daily between set time. This uses the endpoints from newsapi.org website to read
    news to the user between the set time.
"""

import datetime
import pyttsx3
import requests
import json
import time

# Setting pyttsx3 properties - voice and rate. for female voice, use Voices[1]. rate of speech has been reduced to 170
# from default rate i.e. 200.
ENGINE = pyttsx3.init()
Voices = ENGINE.getProperty('voices')
ENGINE.setProperty('voice', Voices[0].id)
ENGINE.setProperty('rate', 170)
# API key from newsapi.org. You need to login and create the the API key or use the same one if not expired.
# Country code is the 2 letter ISO 3166 country code. Endpoint you will get from newsapi.org. The endpoint that I have
# used is for getting top headlines of a country.
APIKEY = "fee271173988456b84e38a60ec297742"
COUNTRY = "in"
ENDPOINT = "https://newsapi.org/v2/top-headlines"
# News will be read only between start and end times
START_TIME = datetime.time(14, 0, 0)
END_TIME = datetime.time(15, 0, 0)


def speak(text):
    """
    :param text: str
    :return:
    This method uses the engine object of pyttssx3 module and allows the computer to speak that ext entered via text
    parameter.
    """
    ENGINE.say(text)
    ENGINE.runAndWait()


def get_top_headlines(endpoint, api_key, country_code):
    """
    :param endpoint: newsapi.org endpoint
    :param api_key:  newsapi.org api key
    :param country_code: 2 letter ISO 3166 country code
    :return: list - top headlines of the country for that day
    This method takes newsapi.org endpoint, api key and 2 letter ISO 3166 country code as input and returns a list of
    headline titles for that country on the day.
    """
    request = requests.get(endpoint, params={"country": country_code, "apiKey": api_key})
    response = json.loads(request.text)["articles"]
    top_headings = [heading["title"] for heading in response]
    return top_headings


if __name__ == '__main__':
    # getting headline list
    top_headlines = get_top_headlines(ENDPOINT, APIKEY, COUNTRY)
    # getting current time
    current_time = datetime.datetime.now().time()

    # Check if current time is between start and end times. read news if yes otherwise notify that time is over.
    if START_TIME <= current_time <= END_TIME:
        count = 1
        for item in top_headlines:
            speak(f"Headline {count}")
            speak(item)
            time.sleep(2)
            count += 1

    else:
        speak("News reading time is over.")
