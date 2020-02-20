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
            res = requests.get(query_url)
            res = res.json()
            self.cache[query_url] = res
        return self.cache[query_url]
