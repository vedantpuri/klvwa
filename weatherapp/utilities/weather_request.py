import os
import json
import math
import requests


class WeatherReporter:
    def __init__(self, api_key, call_limit, base_url):
        self.cache = {}
        self._api_key = api_key
        self.call_limit = call_limit
        self.base_url = base_url

    @staticmethod
    def format_location(location):
        city, state = location
        city = city.split()
        if len(city) > 1:
            city = "+".join(city)
        else:
            city = city[0]
        location = city + "," + state
        return location

    def construct_url(self, location, query_type, query_args):
        return (
            self.base_url
            + query_type
            + f"city={WeatherReporter.format_location(location)}&"
            + f"key={self._api_key}&"
            + "&".join([k + "=" + query_args[k] for k in query_args])
        )

    def get_weather(self, location, query_type, query_args):
        query_url = self.construct_url(location, query_type, query_args)
        if query_url not in self.cache:
            # Error checking !!
            res = requests.get(query_url)
            res = res.json()
            self.cache[query_url] = res
        return self.cache[query_url]

#
# # base_url = "https://api.weatherbit.io/v2.0/"
# # query_type = "forecast/daily?"
# # args = {"days": "3"}
# # check calls limit 500/day
# API_KEY = os.environ.get("WEATHERBIT_KEY")
# wr = WeatherReporter(API_KEY, 500, base_url)
# print(wr.construct_url("raileigh,nc", query_type, args))
#
# url = f"https://api.weatherbit.io/v2.0/forecast/daily?city=Raleigh,NC&key={API_KEY}&days=3"
# # res = requests.get(url).json()
# # print(res)
# # with open("dummy_weather.json", "w") as fout:
# #     json.dump(res, fout)
#
#
# with open("dummy_weather.json") as f:
#     data = json.load(f)
# for d in data["data"]:
#     print(d["weather"]["code"])
#     # print(int(round(d['temp'])), d['pop'])
#
# # if d['weather']['code'] == 800 or d[i][temp] - d[i+1]['temp'] >= 5 :
# # NICE EMAIL
# # If it's nice outside, either sunny or 5 degrees warmer than tomorrow’s forecasted temperature for that location, the email's subject should be "It's nice out! Enjoy a discount on us." Otherwise, if it's not so nice out, either precipitating or 5 degrees cooler than tomorrow’s forecasted temperature, the subject should be "Not so nice out? That's okay, enjoy a discount on us." If the weather doesn't meet either of those conditions, the email subject should read simply "Enjoy a discount on us." In all cases the email should be sent to the recipient's entered email address and come from your email address.
