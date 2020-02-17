import json
import math
import requests
# check calls limit 500/day
API_KEY = "ac20a8222a3346caa840643f6fbeb419"
# with open("locations.json") as f:
#     data = json.load(f)
# for d in data:
#     city, state = d["fields"]['city'], d["fields"]['state']
#     city = city.split()
#     if len(city) > 1:
#         city = "+".join(city)
#     else:
#         city = city[0]
#     print(city, state)
#     location = city + "," + state
#     URL = f"https://api.weatherbit.io/v2.0/current?city={location}&key={API_KEY}"
#     print(URL)
#     # res = requests.get(URL).text
#     print(res)
#     print()


url = f"https://api.weatherbit.io/v2.0/forecast/daily?city=Raleigh,NC&key={API_KEY}&days=3"
# res = requests.get(url).json()
# print(res)
# with open("dummy_weather.json", "w") as fout:
#     json.dump(res, fout)


with open("dummy_weather.json") as f:
    data = json.load(f)
for d in data['data']:
    print(d['weather']['code'])
    # print(int(round(d['temp'])), d['pop'])

# if d['weather']['code'] == 800 or d[i][temp] - d[i+1]['temp'] >= 5 :
# NICE EMAIL
# If it's nice outside, either sunny or 5 degrees warmer than tomorrow’s forecasted temperature for that location, the email's subject should be "It's nice out! Enjoy a discount on us." Otherwise, if it's not so nice out, either precipitating or 5 degrees cooler than tomorrow’s forecasted temperature, the subject should be "Not so nice out? That's okay, enjoy a discount on us." If the weather doesn't meet either of those conditions, the email subject should read simply "Enjoy a discount on us." In all cases the email should be sent to the recipient's entered email address and come from your email address.
