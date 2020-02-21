# Weather App
Welcome to my implementation of the weather powered email assignment by Klaviyo.

## Requirements
The following libraries have been used and can be installed using ```pip install -r requirements.txt```
- Django == 3.0.3
- Python == 3.6
- requests == 2.22.0
- beautifulsoup4 == 4.8.2
- lxml == 4.5.0

Please ensure that your PythonPath etc are configured properly. I would advise using a virtual environment to run this program.

Apart from the above, I used certain environment variables to ensure sensetive data never gets exposed as a measure of security. Please set the following:
- Subscribe to weatherbit.io and upon obtaining the key, set the environment variable with the name: ```WEATHERBIT_KEY```
- For the purposes of this assignment, I used my email to send out emails and hence used environment variables for the credentials and hence, you would need to set these for proper functioning: ```EMAIL_ID``` as your email-id and ```EMAIL_PASS``` for the password.

## Admin Credentials
If you would like to inspect deeper under the hood, I have provided with the admin credentials of the website
```
Username: kvadmin
Email: vedantpuri13@gmail.com
PW: kvweatherapp
```

## Steps to Run
- Satisfy Requirements
- Create Fixture by scraping top populated cities. To do this navigate to ```weatherapp/utilities``` and run:
```
python scrape_cities.py
```
- Navigate one directory up and now load this fixture into django by running:
```
python manage.py loaddata locations.json
```
- Migrate these changes:
```
python manage.py makemigrations
python manage.py migrate
```
- Run the server:
```
python manage.py runserver
```
- Use the app and make subscriptions. Once done quit the server.
- To send the emails of all subscribers as of now run:
```
python mail_sender.py
```

**NOTE:** It is unnecessary to scrape cities, load fixtures and make migrations everytime. I provided these instructions with the mindset of the project being run for the very first time after the code was written. Even in my submission, the sqlite files should be present which should resume from the state I left them in last.

In a real world setting, scraping cities can be run every year in order to update the list and then migrated into the DB.

## Assumptions
During this project I made some small assumptions, which I thought I would mention. Due to heavy semester load it was hard for me to implement/check some of these. I wanted to mention these to showcase that I am aware of them and would have implemented in a real world setting.
- **Email Existence:** For the purposes of this assignment I assumed that the emails being enter will exist. Ofcourse, while filling the form, there is a Django regex check to validate format, but currently there is no check for whether the email is actually a real one or not.
- **Weatherbit.io correctness:** It has been assumed that weatherbit returns accurate weather. I have tested it and verified for a few locations but still wanted to mention this as an assumption.
- **Weatherbit always returns:** The requests to weatherbit.io never fail. Ideally, there should be a check for this but due to the free subscription there is a cap on the number of calls I can make (so I cannot poll till I succeed) and the assignment asks us to set the content of the body of the email with the weather and description of the location, which is a hard field to have a default value and wouldn't suit the app.
wise). However there is a check before querying to see if there is an active internet connection or not.


## Scalability
Our app may have a million users but the configuration of the app allows only top 100 most populated cities in the US. Hence it is grossly inefficient to query the weather for every user. Therefore, I query only locations that have users corresponding to them in the database, hence worst case I will make only 100 calls to the weatherbit API. In my implementation, due to caching the locations, I also compute what email to send per location also once thereby having some minor computation savings there.

## Security
- **Django queries:** The only segment where there is interaction with data is when a user submits a form with his/her email and location. By default, Django querysets are protected against SQL injection since the queries are constructed using query parameterization. Source: https://docs.djangoproject.com/en/3.0/topics/security/
- **Sending emails:** In my project I use an SSL connection to login to my email and send mails and by virtue of SSL, all data sent within that session is private and encrypted.

## Design Choices

- **Usability:** To define my models, I created a subscriber and a location model, with subscriber having a foreign key to location. Now, since we use only top 100 most populated cities, it is very rare or unusual for the list to **drastically** change. Only the bottom few are vulnerable to change, hence it is very unlikely in the first place that a location will be deleted. In case it does, I have used ```on_delete=models.PROTECT```, which basically means, if any subscriber points to a location about to be deleted, don't delete it. The thinking behind this was that if we have a user with a location that is about to be deleted, we should keep that location since we are all about personalizing for customers. Without the location we wouldn't be able to send them personalized emails which I felt was incorrect. The tradeoff is that in the absolute worst case(very very unlikely to happen) we have all the cities of US in our database and I thought that if we decide to actually delete the location, we must have a mechanism to either: set the user's weather to the closest city to the one being deleted and ballpark the email OR send out an email notifying the user that the city has been deleted.

- **Weather API design choices:** There were a couple of ways to decide the subject of the email based on the weather and I chose a safer option, i.e.: using weather codes. WeatherBit has certain codes for the kind of weather. To check if it is sunny we have ```code==800```, to check for precipitation we have two things: ```300 <= code <= 623``` which is a range of some form of precipitation OR ```code==900``` which is code for unknown precipitation. Apart from this, Ofcourse temperature was also used in the constraints. I used this way because we want to cover wide range of precipitation and it is a nice plug and play way to determine the general weather of the day.

- **Within script security:** To adapt to best practices, I used environment variables to shield sensitive information such as: Email ID, Email Password and API keys.

## Sources
- [Abbreviations of states](http://worldpopulationreview.com/states/state-abbreviations/)
