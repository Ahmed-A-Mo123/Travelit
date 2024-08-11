from openai import OpenAI
import requests
import time
import json
import math
from datetime import date


# ----------------------------------------------------------------------------------------------------------------
def chatgpt_request(prompt):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}],
        stream=True
    )

    return completion


def meta_data_flight_api(location):  # Gets the data needed to make further requests to the api
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

    querystring = {"query": location}

    headers = {
        "X-RapidAPI-Key": "6e6479f259mshd843a25a24806a4p115368jsnb1d58a9c3efa",
        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
    }

    chatgpt_response = requests.get(url, headers=headers, params=querystring)
    return chatgpt_response.json()


def skyscanner_main_request(url, querystring):  # api works
    url = url
    headers = {
        "X-RapidAPI-Key": "6e6479f259mshd843a25a24806a4p115368jsnb1d58a9c3efa",
        "X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
    }

    skyscanner_response = requests.get(url, headers=headers, params=querystring)
    return skyscanner_response.json()


# ----------------------------------------------------------------------------------------------------------------

class Chatgpt:

    def __init__(self, destination):
        self.destination = destination

    # destination info
    def destination_info(self):
        prompt = f'Give me bullet points about {self.destination}'
        return chatgpt_request(prompt)

    def things_to_do(self):
        prompt = f'tell me things to do in {self.destination}'
        return chatgpt_request(prompt)

    def best_time_to_go(self):
        prompt = f'When is the best time to go {self.destination}, give me just the months'
        return chatgpt_request(prompt)

    def other_recommended_places(self):
        prompt = f'Recommend 3 other cities similar to {self.destination}'
        return chatgpt_request(prompt)


class SkyscannerApi:

    def __init__(self, origin, destination, passengers, departure_date, return_date):
        self.destination = destination  # these must be cities and not countries make sure to handle if someone enters
        # a country
        self.origin = origin
        self.passengers = passengers
        self.departure_date = departure_date
        self.return_date = return_date
        self.status = ''

        origin_meta_data = meta_data_flight_api(origin)
        time.sleep(1)  # Api plan only allows me to make one request per second :(
        destination_meta_data = meta_data_flight_api(destination)

        self.origin_Skyid = origin_meta_data['data'][0]['skyId']
        self.destination_SkyId = destination_meta_data['data'][0]['skyId']

        self.origin_EntityId = origin_meta_data['data'][0]['entityId']
        self.destination_EntityId = destination_meta_data['data'][0]['entityId']

    def flights(self):
        url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"
        query_string = {"originSkyId": self.origin_Skyid,
                        "destinationSkyId": self.destination_SkyId,
                        "originEntityId": self.origin_EntityId,
                        "destinationEntityId": self.destination_EntityId,
                        "date": self.departure_date,
                        "returnDate": self.return_date,
                        "adults": self.passengers,
                        "sortBy": "best",
                        "limit": '1',
                        "market": "en-US", "countryCode": "UK"}
        time.sleep(1)
        return skyscanner_main_request(url, query_string)

    def hotels(self):
        rooms = math.ceil(int(self.passengers) / 2) # Adjusts the rooms according to how many guests (default 2 to a
        # room)
        url = "https://sky-scrapper.p.rapidapi.com/api/v1/hotels/searchHotels"
        querystring = {"entityId": self.destination_EntityId,
                       "checkin": self.departure_date,
                       "checkout": self.return_date,
                       "adults": self.passengers,
                       "rooms": rooms,
                       "limit": "3",
                       "currency": "GBP",
                       "market": "en-GB",
                       "countryCode": "UK"}
        time.sleep(1)
        return skyscanner_main_request(url, querystring)




# -----------------------------------------------------------------------------------------
# Current weather at destination

class WeatherApi:
    def __init__(self, destination) -> None:
        self.destination = destination

    def api_request(self):
        url = "https://yahoo-weather5.p.rapidapi.com/weather"

        querystring = {"location":self.destination,"format":"json","u":"c"}

        headers = {
            "x-rapidapi-key": "6e6479f259mshd843a25a24806a4p115368jsnb1d58a9c3efa",
            "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return type(response.json())
    
#------------------------------------------------------------------------------------------








# Testing Chatgpt API
# def main():
#     ai = Chatgpt('United Kingdom')
#
#     data = ai.destination_info()
#
#     for item in data:
#         print(item.choices[0].delta.content, end="")


# if __name__ == '__main__':
#     # main()
#
# gpt = Chatgpt('London')
#
# response = gpt.best_time_to_go()
#
# # display the chatgpt stream
# for chunk in response:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")




#testing SKY Scraper API
# def main():
#     test = SkyscannerApi('london', 'New york', '2', '2024-08-13', '2024-08-20')
#     flights = test.flights()
#     print(flights)

# if __name__ == '__main__':
#     main()