# ----- IMPORTS
import re
import csv
import json
import logging
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# ----- CONSTANTS
FIXTURE_OUT = "../locations.json"
ABBREVIATION_FILE = "abbreviations.csv"
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s : %(levelname)s : %(message)s"
)
URL = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population#United_States"


# ----- SCRAPING
def get_html_data(url):
    try:
        res = requests.get(url)
        # If the response was successful, no Exception will be raised
        res.raise_for_status()
    except HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err} \n\nQuitting ...")
        exit()
    except Exception as err:
        logging.error(f"Other error occurred: {err} \n\nQuitting ...")
        exit()
    else:
        logging.info(f"Successfully Downloaded HTML from: {URL}")
    return res.text


# ----- CLEANING
def clean_data(data):
    soup = BeautifulSoup(data, "lxml")
    locations = []
    logging.info("Extracting city list ...")
    for items in soup.find("table", class_="wikitable sortable").find_all("tr")[1::1]:
        data = items.find_all(["th", "td"])
        try:

            city = re.sub(r"\[.*?\]", "", data[1].text.strip())
            state = data[2].text.strip()
        except IndexError:
            pass
        locations += [(city, state)]
    logging.info("Extraction complete.")
    return locations


# ----- ABBREVATION
def create_abbrev_mapping(abrev_file):
    codes = {}
    logging.info("Forming Abbreviation mapping ...")
    with open(abrev_file, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            codes[row[0][1:-1]] = row[2][1:-1]
    logging.info("Abbreviation mappingcomplete.")
    return codes


# ----- DUMPING
def dump_data(out_file, locations, codes):
    locations = locations[:100]
    model_name = "signup.location"
    pk = 0
    json_arr = []
    logging.info("Forming fixture ...")
    for k in locations:
        json_dict = {}
        json_dict["model"] = model_name
        json_dict["pk"] = pk
        data = {}
        data["city"] = k[0]
        data["state"] = codes[k[1]]
        json_dict["fields"] = data
        json_arr += [json_dict]
        pk += 1
    logging.info("Fixture complete.")

    with open(FIXTURE_OUT, "w") as fout:
        json.dump(json_arr, fout)
    logging.info(f"Fixture dumped to {out_file}")


if __name__ == "__main__":
    try:
        response = requests.get("http://www.google.com")
    except requests.ConnectionError:
        logging.error(f"No network connection. Try again later.")
        exit()
    html_text = get_html_data(URL)
    locations = clean_data(html_text)
    codes = create_abbrev_mapping(ABBREVIATION_FILE)
    dump_data(FIXTURE_OUT, locations, codes)
