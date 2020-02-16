import json
import requests

API_KEY = "ac20a8222a3346caa840643f6fbeb419"
with open("locations.json") as f:
    data = json.load(f)
for d in data:
    city, state = d["fields"]['city'], d["fields"]['state']
    city = city.split()
    if len(city) > 1:
        city = "+".join(city)
    else:
        city = city[0]
    print(city, state)
    location = city + "," + state
    URL = f"https://api.weatherbit.io/v2.0/current?city={location}&key={API_KEY}"
    print(URL)
    # res = requests.get(URL).text
    print(res)
    print()
