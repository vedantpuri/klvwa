# ----- IMPORTS
import re
import requests
from bs4 import BeautifulSoup

# ----- CONSTANTS
URL = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population#United_States"

# ----- SCRAPING
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
locations = []
for items in soup.find('table', class_='wikitable sortable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    try:

        city = re.sub(r'\[.*?\]', '', data[1].text.strip())
        state = data[2].text.strip()
    except IndexError:pass
    locations += [(city, state)]


import csv
import json
codes = {}
with open('abbreviations.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        codes[row[0][1:-1]] = row[2][1:-1]
 # {
 #    "model": "myapp.person",
 #    "pk": 1,
 #    "fields": {
 #      "first_name": "John",
 #      "last_name": "Lennon"
 #    }
 #  }
locations = locations[:100]
model_name = "signup.location"
pk = 0
json_arr = []
# print(len(locations))
for k in locations:
    json_dict = {}
    json_dict["model"] = model_name
    json_dict["pk"] = pk
    data = {}
    data['city'] = k[0]
    data['state'] = codes[k[1]]
    json_dict['fields'] = data
    # json_dict["fields"]["city"] = k[0]
    # json_dict["fields"]["state"] = codes[k[1]]
    json_arr += [json_dict]
    pk += 1


with open('test.json', 'w') as fout:
    json.dump(json_arr , fout)
