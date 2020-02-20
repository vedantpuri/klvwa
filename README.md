# Weather App (Klaviyo)
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

## Assumptions
During this project I made some small assumptions, which I thought I would mention. Due to heavy semester load it was hard for me to implement/check some of these.
- Email Existence: For the purposes of this assignment I assumed that the emails being enter will exist. Ofcourse, while filling the form, there is a Django regex check to validate format, but currently there is no check for whether the email is actually a real one or not.
- weatherbit.io returns weather correctly
- The requests to weatherbit.io never fail. Ideally, there should be a check for this but due to the free subscription there is a cap on the number of calls I can make (so I cannot poll till I succeed) and the assignment asks us to set the content of the body of the email with the weather and description of the location, which is a hard field to have a default value and wouldn't suit the app.
wise)


## Scalability
- Caching weather API calls (O(100))
- No recomputation of what kind to email to send, going by locations and storing the email

## Security
- SMTP SSL reason
- no cookies(no pass)
- csrf token Django

## Design Choices
- Linking Models with Foreign Key. FIRSTLY VERY RARE THAT population list will change, only ones at bottom, secondly want to keep customers that we already have with their weather. ON delete Protect because want customer to stay UNLESS unsubscribe (because population change). Even in the worst case 350 cities. Send email that location has been removed (don’t think that is good from a customer perspective)

- Weather API code(sunny 800 etc) design choices: because want to cover wide range

- Environment variables(Repeated)

## Sources
- Abbreviations of states http://worldpopulationreview.com/states/state-abbreviations/
