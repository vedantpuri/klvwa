# import os
# import smtplib
# from email.message import EmailMessage
#
# EMAIL_ID = os.environ.get('EMAIL_ID')
# EMAIL_PASS = os.environ.get('EMAIL_PASS')
# msg = EmailMessage()
# msg['Subject'] = 'Discount on us'
# msg['From'] = EMAIL_ID
# msg['To'] = 'vedantpuri@umass.edu'
# msg.set_content('How about a discount on us')
#
#
# def decipher_weather():
#     pass
#
# # context manager snures connection is closed automatically
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
#     conn.login(EMAIL_ID, EMAIL_PASS)
#     conn.send_message(msg)
from weatherapp import settings
from django.core.management import setup_environ
setup_environ(settings)
from signup.models import Subscriber

if __name__ == "__main__":
    pass
    # base_url = "https://api.weatherbit.io/v2.0/"
    # query_type = "forecast/daily?"
    # args = {"days": "3"}
    # query_limit = 500
    # wr = WeatherReporter(os.environ.get("WEATHERBIT_KEY"), query_limit, base_url)
