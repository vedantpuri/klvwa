# ----- IMPORTS
import os
import django
import logging
import smtplib
from email.message import EmailMessage
from utilities.weather_request import WeatherReporter
from validate_email import validate_email

# ----- SCRIPT SETUP
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weatherapp.settings")
django.setup()
from signup.models import Subscriber

# ----- UTIL FUNCS
def get_users_locations():
    subscribers = Subscriber.objects.all()
    locations = {}
    for subscriber in subscribers:
        if (subscriber.location.city, subscriber.location.state) not in locations:
            # Even though emails are unique, set is used for O(1) insertion
            locations[(subscriber.location.city, subscriber.location.state)] = set()
        locations[(subscriber.location.city, subscriber.location.state)].add(
            subscriber.email
        )
    return locations


def dissassemble_weather(weather):
    today_weather, tomorrow_weather = weather['data'][0], weather['data'][1]
    ret_code, temp, desc = 0, today_weather['temp'], today_weather["weather"]["description"]
    if (today_weather["weather"]["code"] == 800) or (
        int(today_weather["temp"]) - int(tomorrow_weather["temp"]) >= 5
    ):
        ret_code = 1
    # codes 300 to 623 refer to some kind of precipitation (drizzle, rain, snow, sleet etc.).
    # 900 is unknown precip
    elif (
        (300 <= today_weather["weather"]["code"] <= 623)
        or (today_weather["weather"]["code"] == 900)
        or (int(tomorrow_weather["temp"]) - int(today_weather["temp"]) >= 5)
    ):
        ret_code = -1
    return ret_code, temp, desc


def form_emails(
    weather_to_email, weather_reporter_obj, locations, query_type, query_args
):
    loc_to_email = {}
    for location in locations:
        loc_weather = weather_reporter_obj.get_weather(
            location, query_type, query_args
        )
        coded_weather, temp, desc = dissassemble_weather(loc_weather)
        loc_to_email[location] = weather_to_email[coded_weather], temp, desc
    return loc_to_email

def generate_email_content(msg, subj, temp, desc):
    msg['Subject'] = 'Discount on us'
    msg['From'] = EMAIL_ID
    msg['To'] = 'vedantpuri@umass.edu'
    msg.set_content('How about a discount on us')

def send_mails(loc_em, locations):
    from_email = os.environ.get('EMAIL_ID')
    from_email_pass = os.environ.get('EMAIL_PASS')
    # context manager ensures connection is closed automatically
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
        conn.login(from_email, from_email_pass)
        for location in locations:
            subject, temp, desc = loc_em[location]
            for to_email in locations[location]:
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = from_email
                msg['To'] = to_email
                msg.set_content(f"{location[0]}, {location[1]}: {temp} degrees celsius, {desc}")
                conn.send_message(msg)

# ----- SCRIPT EXECUTION
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s : %(levelname)s : %(message)s"
    )
    logging.info("Fetching Subscriber Data ...")
    locs = get_users_locations()
    logging.info("Successfully fetched Subscriber Data.")

    # weather obj instantiation
    base_url = "https://api.weatherbit.io/v2.0/"
    query_type = "forecast/daily?"
    query_args = {"days": "2"}
    query_limit = 500
    wr = WeatherReporter(os.environ.get("WEATHERBIT_KEY"), query_limit, base_url)

    # Initialize weather to email mapping
    weather_to_email = {
        -1: "Not so nice out? That's okay, enjoy a discount on us.",
        0: "Enjoy a discount on us.",
        1: "It's nice out! Enjoy a discount on us.",
    }

    logging.info("Fetching weather data for locations ...")
    loc_emails = form_emails(weather_to_email, wr, locs, query_type, query_args)
    logging.info("Successfully fetched weather data.")

    logging.info("Sending out emails ...")
    send_mails(loc_emails, locs)
    logging.info("Successfully sent emails.")
